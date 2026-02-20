# Project: Smart Office Lighting

## Overview

**One-line description:** Intelligent lighting that responds to occupancy, daylight, and schedules

**Project Lead:** TBD
**Team Members:** TBD
**Status:** Existing module with backlog

## Description

Smart Office Lighting uses the existing [`lutron-bacnet`](https://github.com/viam-labs/lutron-bacnet) module to integrate Viam with the building's commercial Lutron lighting system over the BACnet protocol. The office already has a production deployment: ~30 configured devices spanning 5 BACnet networks, with discovery, sensor, and switch components covering conference rooms, corridors, the cafeteria, the robotics room, and meeting rooms.

The hackathon goal is to harden the existing module, extend it with automation features, and build out the control experience. The module is published to the Viam Registry as `hipsterbrown:lutron-bacnet` and the codebase is Python (BAC0 + bacpypes3 libraries).

This project demonstrates event-driven automation, scheduled tasks, IoT integration, and module development - capabilities that manipulation-heavy projects don't emphasize.

---

## MVP

- More user-friendly light control app
- Implement presets for lighting in different areas of the office
- Automatically adjust office lighting in an area based on ambient light levels
- Some scheduled tasks (morning/evening)
- Motion-sensing to override.

Stretch: Enable individuals to personalize light settings for meeting rooms. 

## Hardware Requirements

| Component | Description | Notes |
|-----------|-------------|-------|
| Lutron Commercial System | Building-wide lighting control | Already installed; areas, zones, RF daylight sensors, occupancy sensors |
| BACnet Network | Protocol layer | Devices span networks 1, 175, 177, 178, 179 |
| Compute | Viam machine | Raspberry Pi 5 (deployed) |
| Light Sensor | Daylight harvesting | BH1750 (for ambient lux measurement, backlog) |

**Remote-Friendly:** Yes - module development fully remote, physical install minimal

---

## Backlog

### Module Quality (Hackathon Priority)
- [ ] **Fix ref counting bug** - `BacnetController` has a double-decrement between `__del__` and `weakref._cleanup`; can cause premature disconnection or crashes
- [ ] **Rename `BacnetSensor` in switch.py** - Class is misnamed; should be `BacnetSwitch` for clarity
- [ ] **Add concurrency control to sensor reads** - Discovery uses a semaphore but sensor `get_readings` fires all reads concurrently with no throttle; can overwhelm the BAC0 client
- [ ] **Fix hardcoded Python path in build.sh** - `python3.11` path is hardcoded for bundling `device.json`; will break on version change
- [ ] **Add config validation** - All three models return empty from `validate_config`; should check required attributes
- [ ] **Remove dead code** - `utils.py` (`get_available_port`) is unused
- [ ] **Update README** - Fix "occupany" typo, document `max_query_concurrency` attribute, fix trailing comma in JSON example, update `meta.json` description

### Scene & Preset Control
- [ ] **Scene definitions** - Named presets (work mode, meeting, presentation, away, emergency) that set multiple zones at once
- [ ] **Scene activation via DoCommand** - Trigger scenes through the Viam SDK
- [ ] **Teleop dashboard integration** - Control panel for switching between scenes
- [ ] **Fade transitions** - Smooth level changes when switching scenes

### Event-Driven Automation (Gap Feature)
- [ ] **Occupancy-based control** - Use BACnet occupancy state objects (already exposed) to activate/dim lights
- [ ] **Vacancy timeout** - Dim/off after occupancy state goes unoccupied for N minutes
- [ ] **Daylight threshold** - Adjust artificial light based on ambient lux readings from RF daylight sensors
- [ ] **After hours behavior** - Different lighting behavior outside work hours
- [ ] **Manual override detection** - Detect manual lighting changes, pause automation temporarily

### Scheduled Tasks (Gap Feature)
- [ ] **Morning startup** - Lights to work mode at 7 AM
- [ ] **Evening shutdown** - Lights off at 8 PM
- [ ] **Weekend mode** - Reduced lighting Saturday/Sunday
- [ ] **Daylight harvesting loop** - Continuous adjustment based on ambient light sensor readings
- [ ] **Cleaning mode** - Full brightness for cleaning crew (scheduled)

### Daylight Harvesting
- [ ] **Ambient light sensor** - BH1750 integration for additional lux measurement
- [ ] **Per-zone adjustment** - Window zones dim more than interior zones
- [ ] **Target lux maintenance** - Maintain consistent light level regardless of outside conditions
- [ ] **Energy tracking** - Log savings from harvesting

### Data & Analytics
- [ ] **Event logging** - All light changes captured via data capture
- [ ] **Energy usage** - Estimate based on lighting power used/available objects (already exposed via BACnet)
- [ ] **Occupancy patterns** - Analyze occupancy state data over time
- [ ] **Dashboard** - Real-time lighting status across all zones

---

## Stretch Goals

- [ ] Color temperature control (if using tunable fixtures)
- [ ] Circadian rhythm lighting (warm morning/evening, cool midday)
- [ ] Voice control integration
- [ ] Calendar integration (meeting room auto-adjust based on bookings)
- [ ] Energy reporting and optimization recommendations
- [ ] Loadshed automation using BACnet loadshed objects

---

## Links

- **Jira Epic:** [TBD]
- **GitHub Repo:** [viam-labs/lutron-bacnet](https://github.com/viam-labs/lutron-bacnet)
- **Viam Registry:** `hipsterbrown:lutron-bacnet`
- **Hardware BOM:** N/A (building system already installed)

---

## Technical Details

### Existing Module Architecture

The `lutron-bacnet` module is a Python-based Viam module that communicates with Lutron commercial lighting systems over the BACnet building automation protocol. It uses the [BAC0](https://github.com/ChristianTrworworthy/BAC0) library for BACnet communication and [bacpypes3](https://github.com/JoelBender/BACpypes3) for low-level property reads/writes.

**Module structure:**
```
lutron-bacnet/
├── src/
│   ├── main.py           # Entry point: Module.run_from_registry()
│   ├── controller.py     # BacnetController singleton (wraps BAC0 client)
│   ├── discovery.py      # DiscoverDevices service (BACnet network scan)
│   ├── sensor.py         # BacnetSensor component (read/write device objects)
│   ├── switch.py         # Switch component (position-based lighting control)
│   └── utils.py          # Unused port utility
├── meta.json             # Module registration (3 models)
├── requirements.txt      # viam-sdk, BAC0, typing-extensions
├── build.sh              # PyInstaller packaging
├── setup.sh              # uv-based environment setup
└── Makefile
```

### Three Models

| Model | API | Purpose |
|-------|-----|---------|
| `hipsterbrown:lutron-bacnet:discover-devices` | `rdk:service:discovery` | Scans BACnet networks, returns configs for all discovered devices and switchable objects |
| `hipsterbrown:lutron-bacnet:lutron-sensor` | `rdk:component:sensor` | Reads all BACnet objects for a device area (lighting level, occupancy, daylighting, power, etc.) |
| `hipsterbrown:lutron-bacnet:lutron-switch` | `rdk:component:switch` | Controls a single BACnet object as a Viam switch (analog-value mapped to 5 positions, binary-value to 2) |

### BACnet Device Model

Each Lutron area is exposed as a BACnet "device" with multiple "objects" representing properties:

| Object Name | Type | Description |
|------------|------|-------------|
| Lighting Level | analog-value | Current dimming level (0-100) |
| Lighting State | binary-value | On/off state |
| Lighting Scene | multi-state-value | Active scene preset |
| Occupancy State | multi-state-value | Current occupancy status |
| Daylighting Enabled | binary-value | Whether daylight harvesting is active |
| Daylighting Level | analog-value | Current daylight-adjusted level |
| Occupied/Unoccupied Level | analog-value | Target levels for each state |
| Loadshed Allowed/Goal | binary/analog | Demand response settings |
| Lighting Power Used | analog-value | Current power consumption |
| RF Daylight Sensor | analog-value | Ambient light readings |

### Current Production Deployment

The machine currently has:
- **3 active switches:** Eliot-Overhead, Cafeteria, Robotics Room (all controlling Lighting Level)
- **7 sensor components** (disabled): Conference room, corridors, and area sensors capturing 25-30 objects each
- **1 discovery service** (disabled): Used for initial network scan
- **Data capture** configured at 0.003 Hz (~once per 5.5 minutes) on all sensors
- Devices span **5 BACnet networks** (1, 175, 177, 178, 179)

### Known Issues in Current Module

1. **Double-decrement ref counting** — `controller.py` has both `__del__` and a `weakref._cleanup` callback that each decrement `_ref_count` and call `client.disconnect()`. This can cause premature disconnection.
2. **No concurrency control in sensor** — `get_readings` fires `asyncio.gather` across all objects with no semaphore. With 25-30 objects per sensor, this can overwhelm the BAC0 client. Discovery correctly uses a semaphore.
3. **Class naming** — `switch.py` defines `class BacnetSensor(Switch)` instead of `BacnetSwitch`.
4. **Build fragility** — `build.sh` hardcodes `python3.11` in the path to BAC0's `device.json`.
5. **Switch do_command is a no-op** — Logs warnings for all commands and returns `False`. Sensor supports `update` via DoCommand but switch does not.

### Daylight Harvesting Architecture (Backlog)

```
┌─────────────────────────────────────────────────────────────┐
│                    Lighting Machine                          │
│                                                              │
│  ┌──────────────┐     ┌──────────────┐     ┌─────────────┐  │
│  │ BH1750       │────▶│ Harvesting   │────▶│ BACnet      │  │
│  │ Light Sensor │     │ Logic        │     │ Controller  │  │
│  └──────────────┘     └──────────────┘     └─────────────┘  │
│         +                    │                     │         │
│  ┌──────────────┐            ▼                     ▼         │
│  │ RF Daylight  │  ┌──────────────┐        ┌─────────────┐  │
│  │ Sensors      │  │ Data Capture │        │ Lutron      │  │
│  │ (via BACnet) │  │ (lux levels) │        │ Dimmers     │  │
│  └──────────────┘  └──────────────┘        └─────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## Notes

**Gap Features This Project Addresses:**
- **Event-Driven Automation** — Occupancy detection, daylight thresholds, after-hours behavior
- **Scheduled Tasks** — Time-based scenes, daylight harvesting loop
- **Module Development** — Improving and extending an existing Python module
- **IoT Integration** — Extends Viam beyond robotics into building automation

**Why this project is valuable:**
- Demonstrates IoT and building automation use case
- Practical energy savings in the office
- Different skillset than manipulation projects
- Immediately useful - lights actually work better
- Already deployed - hackathon builds on working foundation

**Existing module context:**
- Module authored by HipsterBrown, published to Viam Registry
- Uses BACnet protocol (UDP-based building automation standard), not Telnet
- The building has a commercial Lutron system (not Caseta consumer hardware)
- BACnet devices expose rich object sets: lighting, occupancy, daylighting, loadshed, power metrics, RF sensors
- Occupancy and daylight data is already available via BACnet objects — no additional sensors required for basic automation

**References:**
- [Lutron BACnet Reference](./lutron-bacnet-reference.md) — BACnet protocol, Lutron product lines, network addressing, the Python stack, and how the module uses it all
- [BACnet Protocol (Wikipedia)](https://en.wikipedia.org/wiki/BACnet)
- [BAC0 Python Library](https://bac0.readthedocs.io/)
- [BACpypes3 Documentation](https://bacpypes3.readthedocs.io/)
- [Viam Module Registry](https://app.viam.com/registry)

---

## Viam Capabilities Demonstrated

### Core Capabilities
- [x] **Hardware Integration** — Lutron commercial lighting system via BACnet protocol
- [ ] **Motion Planning** — Not applicable
- [ ] **Vision / ML Inference** — Not applicable
- [x] **Data Capture & Sync** — Lighting levels, occupancy, energy usage synced to cloud (configured at 0.003 Hz)
- [x] **Remote Operation** — Full remote control and development
- [x] **Module Development** — Primary: improve and extend the lutron-bacnet Python module
- [x] **Fragments** — Zone configurations as reusable fragments

### Scale & Fleet Capabilities
- [x] **Fleet Management** — Multiple light zones managed as fleet
- [x] **OTA Updates** — Module and configuration updates via Registry
- [x] **Provisioning** — Fragment-based configuration reuse

### Operational Capabilities
- [x] **Scheduled Tasks** — Primary: time-based scenes, daylight harvesting loop
- [ ] **Monitoring & Alerting** — Backlog: zone status dashboard
- [ ] **Data Pipeline (ML Training)** — Not applicable

### Customer-Facing Capabilities
- [ ] **Customer Delivery** — Not applicable
- [ ] **Web/Mobile Apps** — Backlog: lighting control dashboard
