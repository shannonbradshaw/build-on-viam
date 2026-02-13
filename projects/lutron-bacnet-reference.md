# Lutron BACnet Reference

This document covers the BACnet protocol, how Lutron commercial lighting systems expose themselves over BACnet, and how the [`lutron-bacnet`](https://github.com/viam-labs/lutron-bacnet) Viam module ties it all together. It is reference material for the [Smart Lighting](./smart-lighting.md) project.

---

## What is BACnet?

BACnet (Building Automation and Control network) is an ASHRAE standard protocol (Standard 135) for building automation systems. It is the common language of commercial building management -- how HVAC controllers, lighting systems, access control, and fire systems talk to each other and to a centralized BMS (Building Management System).

### Protocol Basics

- **Transport:** UDP on port **47808** (0xBAC0 in hex -- which is where the BAC0 Python library gets its name)
- **Why UDP, not TCP:** BACnet messages are small request-response pairs. UDP avoids TCP connection overhead. Reliability is handled at the application layer via "confirmed services" that expect acknowledgments.
- **OSI Model:** BACnet uses a collapsed 4-layer model (Physical, Data Link, Network, Application), deliberately omitting layers 4-6 to reduce overhead for resource-constrained embedded controllers.

### Device Discovery

Discovery is broadcast-based:

1. **Who-Is:** A device broadcasts a request, optionally specifying a device instance range. A global Who-Is (no range) asks every device to respond.
2. **I-Am:** Matching devices reply with their instance number, MAC address, and identification info.
3. **Who-Has / I-Have:** Similar, but searches for devices containing a specific named object.

Discovery can be targeted or global. Lutron documentation warns that Who-Is requests should be separated by at least 10 seconds to avoid response storms on large networks.

### The Object Model

BACnet represents everything as **objects with properties**. This is the core abstraction.

- Every BACnet device contains one or more objects
- Each object has an **Object_Identifier** (a 32-bit code encoding the object type and instance number)
- Each object has properties that can be read or written
- Three properties are mandatory on every object: `Object_Identifier`, `Object_Name`, `Object_Type`

Common object types relevant to lighting:

| Object Type | Code | Description |
|-------------|------|-------------|
| Analog Value (AV) | `analog-value` | A virtual analog value (no direct hardware mapping) |
| Binary Value (BV) | `binary-value` | A virtual binary point (on/off) |
| Multi-State Value (MSV) | `multi-state-value` | A virtual enumerated value with named states |
| Device | `device` | Mandatory object describing the BACnet device itself |

The key distinction: **Input/Output** types represent physical hardware points (a real sensor or actuator). **Value** types represent virtual or calculated points. Lutron uses Value types because the BACnet objects are virtual representations of the lighting system state, not direct hardware connections.

### The objectList

Every BACnet device has a Device object with an `Object_List` property -- an array of Object_Identifiers for every object the device contains. This is the master inventory. To enumerate what a device offers, you read its objectList, then read properties (like `objectName` and `presentValue`) from each object.

---

## Network Addressing

### The Three-Part Address System

1. **Network Number** (1-65534): Identifies a physical or logical network segment. Devices on the same segment share a network number.
2. **MAC Address**: The layer-2 address on a specific network. For BACnet/IP, this encodes the IP address and UDP port as a hex value.
3. **Device Instance** (0-4,194,302): A globally unique 22-bit logical identifier that uniquely identifies a device across the entire BACnet internetwork.

### Reading Addresses

Addresses like `1:0x00000035b9f6` use `network:mac` notation:

- `1` = BACnet network number 1
- `0x00000035b9f6` = the MAC address (encoding IP:port for BACnet/IP)

The office deployment spans networks **1, 175, 177, 178, and 179** -- these are different BACnet network segments, likely corresponding to different floors or wings, each with its own Lutron subsystem.

### Routing and BBMDs

A **BACnet router** connects two or more BACnet networks. When a device on Network 1 needs to talk to a device on Network 177, the router forwards the message based on its routing table. Routers announce their connectivity via I-Am-Router-To-Network messages.

On IP networks, UDP broadcasts don't cross subnet boundaries. A **BBMD (BACnet Broadcast Management Device)** solves this by maintaining a Broadcast Distribution Table and forwarding broadcasts between subnets. A device can also register as a **Foreign Device** with a BBMD to receive forwarded broadcasts without being a BBMD itself.

### BACnet/IP vs. MS/TP

| | BACnet/IP | BACnet MS/TP |
|---|-----------|-------------|
| **Physical** | Standard Ethernet | RS-485 twisted pair |
| **Transport** | UDP port 47808 | Token-passing at layer 2 |
| **Speed** | 100 Mbps+ | 9.6-115.2 kbps |
| **Topology** | Star (switches/routers) | Daisy-chain bus, max 4000 ft |
| **Device Limit** | Effectively unlimited | ~128 per trunk |
| **Use case** | Supervisory controllers, servers, BMS | Field-level controllers, VAV boxes, sensors |

Lutron Quantum and Vive systems use **BACnet/IP exclusively**. MS/TP is common for HVAC field devices but not relevant to the lighting integration.

---

## Lutron Product Lines and BACnet

BACnet is a commercial building automation protocol. Only Lutron's commercial product lines support it:

| Product Line | Market | BACnet Support | Notes |
|-------------|--------|----------------|-------|
| **Quantum** | Large commercial | Yes -- native | Built into the Quantum processor. Requires a BACnet software license. BTL-certified. |
| **Vive** | Small-to-mid commercial | Yes -- native | Built into the Premium Vive Hub (HNS-2-XX). Enabled via Vive Vue Dashboard. BTL-certified. |
| **Athena** | Scalable commercial | Yes | Newer Lutron commercial platform. |
| **myRoom** | Hotel/hospitality | Yes | Has its own BACnet PIC statement. |
| **Caseta** | Residential | No | Uses LEAP, HomeKit, SmartThings. No BACnet. |
| **RadioRA 2/3** | Residential | No | Uses LEAP protocol. |
| **HomeWorks QSX** | Luxury residential | No | Uses LEAP. |

The office has a **commercial Lutron system** (Quantum or Vive). This is a completely different product family than Caseta.

### Lutron Integration Protocols Compared

| Protocol | Transport | Product Lines | Audience |
|----------|-----------|---------------|----------|
| **BACnet/IP** | UDP 47808 | Quantum, Vive, Athena | Facility managers, BMS integrators |
| **LEAP** | TCP/TLS | Caseta, RadioRA 3, HomeWorks QSX | Home automation, smart home platforms |
| **Telnet Integration** | TCP 23 | Legacy HomeWorks QS, Quantum (legacy) | AV integrators (**being discontinued**) |

These protocols can coexist. A Quantum system can serve BACnet to a Siemens BMS while simultaneously accepting LEAP commands from a Crestron controller.

---

## How Lutron Maps to BACnet

### The Lutron Hierarchy

```
Quantum/Vive System
  └── Subsystem (typically one per floor)
        └── Area (a room or space)
              ├── Zone 1 (group of fixtures, e.g. "overhead lights")
              ├── Zone 2 (e.g. "accent lights")
              └── Zone 3 (e.g. "wall sconces")
```

### Virtual Device Architecture

Each **area** (room) becomes its own **virtual BACnet device**. A building with 50 rooms presents 50+ virtual devices on the network. There is also one physical device per subsystem.

This is what you see in the machine config: components like `Conference--Room-Area-004-3521007` or `East-Corridor-Area-005-3521008` are each one Lutron area exposed as a virtual BACnet device. The numeric suffix (e.g. `3521007`) is the BACnet device instance number, calculated from a base value configured during Lutron setup.

### BACnet Objects per Area

Each area virtual device contains objects representing its properties:

| Object Name | Type | Description |
|------------|------|-------------|
| Lighting Level | analog-value | Overall dimming level (0-100%) |
| Lighting State | binary-value | On/off state |
| Lighting Scene | multi-state-value | Active scene preset (named states) |
| Occupancy State | multi-state-value | Unoccupied / Occupied / Inactive / Unknown |
| Occupancy Mode | multi-state-value | How sensors control lights (auto on/off, manual on/auto off, etc.) |
| Daylighting Enabled | binary-value | Whether daylight harvesting is active |
| Daylighting Level | analog-value | Current daylight-adjusted level |
| Occupied Level | analog-value | Target level when occupied |
| Unoccupied Level | analog-value | Target level when unoccupied |
| Loadshed Allowed | binary-value | Whether demand response is permitted |
| Loadshed Goal | analog-value | Target reduction percentage |
| Lighting Power Used | analog-value | Current power consumption (watts) |
| Maximum Lighting Power Available | analog-value | Connected load ceiling |
| RF Daylight Sensor | analog-value | Ambient light readings from wireless sensors |
| Power Savings By ... | analog-value | Savings attributed to loadshed, tuning, daylighting, occupancy, schedules, personal control |

Not every area has every object. The exact set depends on what's configured in the Lutron system. The Conference Room sensor in the production config has 28 objects; corridor sensors have 28-32.

---

## The BACnet Priority Array

BACnet commandable objects have a **16-slot priority array**. The Present_Value is always determined by the highest-priority (lowest-numbered) non-NULL slot:

| Priority | Standard Use |
|----------|-------------|
| 1 | Manual Life Safety (fire override, emergency lighting) |
| 2 | Automatic Life Safety (fire alarm commands) |
| 5 | Critical Equipment Control |
| 8 | Manual Operator Override (BMS operator) |
| 15 | Scheduling |
| **16** | **Default / lowest priority** |

The lutron-bacnet module writes at **priority 16** -- the lowest, most deferential level. This means: "set this lighting level, but any fire alarm, operator override, or schedule should take precedence." This is correct for a BMS integration client.

To release control at a priority level, write **NULL** to that slot. If all 16 slots are NULL, the value reverts to the object's `Relinquish_Default`.

---

## The Python Stack: BAC0 and bacpypes3

```
Module code (lutron-bacnet)
       │
      BAC0  ← High-level scripting (simplified read/write/discover)
       │
   bacpypes3  ← Low-level BACnet protocol (PDU encoding, segmentation, networking)
       │
    asyncio
       │
   UDP sockets on port 47808
```

### bacpypes3

[GitHub](https://github.com/JoelBender/BACpypes3) | [Docs](https://bacpypes3.readthedocs.io/)

The raw BACnet protocol implementation in Python. Handles PDU encoding/decoding, network connections, segmentation, and all BACnet services. Python 3.8+, fully async. Powerful but low-level -- you need to understand BACnet internals to use it directly.

### BAC0

[GitHub](https://github.com/ChristianTremblay/BAC0) | [Docs](https://bac0.readthedocs.io/)

A higher-level library built on bacpypes3 that provides simplified commands for common operations. Named after port 47808 (0xBAC0). Python 3.10+.

**Starting a connection:**
```python
import BAC0

bacnet = BAC0.start(ip='192.168.1.10/24', deviceId=1234)
```

**Discovering devices:**
```python
await bacnet._discover()
devices = await bacnet._devices(_return_list=True)
# Returns: [(deviceName, vendorName, devId, address, networkNumber), ...]
```

**Reading a property:**
```python
# Format: 'address objectType objectInstance propertyName'
value = await bacnet.read('1:0x00000035b9f6 analogValue 2 presentValue')
name = await bacnet.read('1:0x00000035b9f6 analogValue 2 objectName')
```

**Reading the object list:**
```python
objects = await bacnet.read('1:0x00000035b9f6 device 3521007 objectList')
# Returns list of (objectType, objectInstance) tuples
```

**Writing with priority (via bacpypes3 directly):**
```python
from bacpypes3.primitivedata import ObjectIdentifier
from bacpypes3.basetypes import PropertyIdentifier
from bacpypes3.pdu import Address

await app.write_property(
    address=Address("1:0x00000035b9f6"),
    objid=ObjectIdentifier(("analog-value", 2)),
    prop=PropertyIdentifier("presentValue"),
    value=75,
    priority=16,
)
```

The lutron-bacnet module uses BAC0 for reads and discovery, and drops down to bacpypes3 for writes (because BAC0's write API didn't offer the exact interface needed for priority-aware writes).

---

## How the lutron-bacnet Module Uses All of This

### Discovery Flow

1. `BacnetController` starts a BAC0 client, binding to UDP 47808
2. `DiscoverDevices.discover_resources()` calls `bacnet.client._discover()` -- broadcasts Who-Is
3. Collects I-Am responses via `bacnet.client._devices()`
4. For each device, reads its `objectList` to enumerate all BACnet objects
5. For each object, reads `objectName` to get human-readable names
6. Generates Viam `ComponentConfig` entries: one sensor per area, plus switches for objects in the `SWITCHABLE_OBJECT_NAMES` list

### Sensor Reads

`BacnetSensor.get_readings()` fires `asyncio.gather` across all objects in the area, reading `presentValue` from each. A single sensor with 28 objects produces 28 concurrent BACnet read requests.

### Switch Control

`BacnetSwitch` (the switch component) maps the Viam Switch API to BACnet writes:
- **analog-value** objects: positions 0-4 map to dimming levels 0, 20, 40, 60, 80 (value = position * 20)
- **binary-value** objects: positions 0-1 map directly to off/on
- Writes use bacpypes3's `write_property` at **priority 16**

### What Gets Exposed as a Switch

The discovery service only generates switch configs for objects whose names appear in:
```python
SWITCHABLE_OBJECT_NAMES = [
    "Lighting Level",
    "Lighting State",
    "Daylighting Enabled",
    "Daylighting Level",
    "Occupied Level",
    "Unoccupied Level",
]
```

All other objects (occupancy, power, scenes, loadshed, etc.) are only readable via the sensor component.

---

## Further Reading

- [BACnet Protocol (Wikipedia)](https://en.wikipedia.org/wiki/BACnet)
- [BACnet PIC Statement for Quantum Area Virtual Devices (PDF)](https://assets.lutron.com/a/documents/3691115.pdf)
- [BACnet PIC Statement for Vive (PDF)](https://assets.lutron.com/a/documents/369996.pdf)
- [Lutron / Schneider Electric BACnet Integration App Note (PDF)](https://assets.lutron.com/a/documents/048617.pdf)
- [Lutron / Siemens BACnet Integration App Note (PDF)](https://assets.lutron.com/a/documents/048524.pdf)
- [Lutron BACnet/IP with Quantum App Note (PDF)](https://assets.lutron.com/a/documents/bacnet_ip_annex_j_with_quantum_048492.pdf)
- [Building Management System Integration for Lutron Lighting (PDF)](https://assets.lutron.com/a/documents/048538.pdf)
- [BAC0 Documentation](https://bac0.readthedocs.io/)
- [BACpypes3 Documentation](https://bacpypes3.readthedocs.io/)
- [Viam Module Registry](https://app.viam.com/registry)
