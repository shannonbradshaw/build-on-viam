# Project: Automated Storage and Retrieval System

## Overview

**One-line description:** Modular lab storage system that retrieves and returns bins on demand via a 3-axis gantry, with RFID identification and a searchable inventory.

**Project Lead:** Petr Novikov
**Team Members:** TBD
**Status:** Proposed

## Description

Automated Storage and Retrieval System is a modular lab storage solution that works like a reversible vending machine. Users select an item on a screen (e.g., M4 nuts), and the machine delivers the bin containing that item. When done, they place the bin in a return slot and the machine puts it back in its assigned position. Bins are identified by RFID tags stuck to their bottoms; a 3-axis gantry with a gripper handles all pick-and-place without additional actuators. The machine maintains an internal state of bin positions and can reindex via RFID if bins are ever reshuffled. A camera takes a picture of bin's contents when it is returned, so that users can see the latest state of the contents in the app from their desks.

The system addresses real pain for lab managers—who today manually maintain inventory and reorder—and for lab users—who often don’t know if an item exists, where it is, or who has it. It keeps an automatic digital twin of inventory, a searchable database with up-to-date bin status (stored vs. in use), content snapshots on each return, and optional tracking of who retrieved which bin. That combination of physical automation and data visibility makes it compelling both as a utility and as a demo.

This project showcases Viam’s hardware integration (gantry, RFID reader, camera, screen, ultrasonic distance sensor), motion planning for reliable bin handling, data capture and sync for inventory and status, and remote operation for development and monitoring. Optional extensions (bulk return, vision-based quantity or content validation) would further exercise vision and ML pipelines.

## Viam Capabilities Demonstrated

### Core Capabilities

- [x] **Hardware Integration** — 2-3 axis gantry, RFID reader, ultrasonic distance sensor, camera, screen
- [ ] **Motion Planning** — Not applicable
- [?] **Vision / ML Inference** — Optional: possible parsing of bin contents to text, item counting
- [x] **Data Capture & Sync** — Logging bin in-out flow. Storing bin content images
- [x] **Remote Operation** — Monitoring inventory state, possibly machine status (e.g. fetching, returning, idle)
- [x] **Module Development** — RFID module, overall control module
- [?] **Fragments** — Overall machine fragment, with variables for number of rows and columns

### Scale & Fleet Capabilities

- [?] **Fleet Management** — Stretch: multiple units across the lab with centralized inventory view
- [x] **OTA Updates** — Module and configuration updates via Registry
- [?] **Provisioning** — Stretch: fragment with row/column variables reused across units

### Operational Capabilities

- [x] **Scheduled Tasks** — RFID reindexing routine, daily inventory summary reports
- [x] **Monitoring & Alerting** — Bin jam detection, stretch: low-stock alerts
- [ ] **Data Pipeline (ML Training)** — Backlog: bin content images → label → train quantity estimation / content validation models → deploy

### Customer-Facing Capabilities

- [x] **Customer Delivery** — Touchscreen item selection,
- [x] **Web/Mobile Apps** — Searchable inventory dashboard with bin status, content snapshots

## Hardware Requirements

| Component                | Description                   | Options                                                                                                                                               |
| ------------------------ | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stepper Motors (x3)      | Gantry axis drive             | [NEMA 23 Bipolar 1.5A](https://www.omc-stepperonline.com/nema-23-bipolar-1-8deg-1-16nm-164-3oz-in-1-5a-5-4v-57x57x56mm-4-wires-23hs22-1504s)          |
| Stepper Drivers (x3)     | Motor control                 | [Adafruit stepper driver](https://www.adafruit.com/product/6121)                                                                                      |
| RFID Reader              | Bin identification            | [Adafruit PN532 NFC/RFID board](https://www.adafruit.com/product/364)                                                                                 |
| IR Distance Sensors (x2) | Bin presence detection        | [Sharp GP2Y0A21YK](https://www.sparkfun.com/infrared-proximity-sensor-sharp-gp2y0a21yk.html)                                                          |
| Touchscreen Display      | User item selection interface | [Official Raspberry Pi 7" Touch Display](https://www.pishop.us/product/official-raspberry-pi-7-touch-screen-display-with-10-finger-capacitive-touch/) |

**Remote-Friendly:** Partially - Touchscreen app and web app can be developed remotely.

---

## MVP Options

Select one for hackathon scope:

### Option A: 2-Axis Retrieve & Return (Recommended)

2-axis gantry (X + Z) retrieves and returns bins from a single column of slots. User selects a bin on the touchscreen, the gantry fetches it to a pickup window. Return works in reverse. RFID identifies bins on pickup and return. All state is local.

- **Scope:** 2-axis gantry control, RFID identification, ultrasonic distance sensor for bin empty/full status, touchscreen UI for bin selection, local state tracking
- **Complexity:** Medium
- **Demo Appeal:** High

### Option B: 3-Axis Full Grid + Database

3-axis gantry (X + Y + Z) serves a full grid of bins. Adds a remote searchable inventory database so users can check bin status and contents from their laptop or phone. Bin status (stored / in use) syncs to the cloud.

- **Scope:** 3-axis gantry control, RFID, touchscreen UI, cloud-synced inventory database, web dashboard
- **Complexity:** Medium-High
- **Demo Appeal:** Very High

### Option C: 3-Axis + User Tracking + Vision

Everything in Option B, plus a camera captures a photo of the user on each retrieval (for audit trail / who-has-what tracking), and bin contents are photographed on every return for a visual inventory log.

- **Scope:** 3-axis gantry, RFID, touchscreen UI, cloud database, web dashboard, user photo capture, bin content snapshots, bin contents parsing
- **Complexity:** High
- **Demo Appeal:** Very High

**Selected MVP:** **\*\***\_\_\_**\*\***

---

## Backlog

### Core Gantry & Retrieval

- [ ] **2-axis gantry control** — X + Z movement, homing, position calibration
- [ ] **3rd axis (Y) expansion** — Extend to full grid access
- [ ] **Bin gripper mechanism** — Reliable grab and release of bins from slots
- [ ] **RFID read on pickup/return** — Identify bin at gripper position
- [ ] **RFID reindexing routine** — Scan all slots to rebuild bin position state
- [ ] **Bin presence detection** — IR sensors confirm bin seated in slot or pickup window

### User Interface

- [ ] **Touchscreen item selection** — Browse / search items, request retrieval
- [ ] **Return flow** — User places bin in return slot, machine re-shelves it
- [ ] **Status display** — Show machine state (idle, fetching, returning, error)
- [ ] **Bin labels** — Human-readable labels on bin sides matching database entries

### Inventory & Data

- [ ] **Local bin state tracking** — Map of which bin is in which slot
- [ ] **Cloud inventory database** — Bin contents, status, timestamps synced to Airtable or similar
- [ ] **Searchable web dashboard** — Employees look up items, see bin status and availability
- [ ] **Bin content snapshots** — Camera photographs bin contents on every return
- [ ] **User photo on retrieval** — Camera captures who retrieved each bin (audit trail)

### Monitoring & Alerts

- [ ] **Gantry health monitoring** — Track motor errors, stalls, position drift
- [ ] **Bin jam detection** — Alert when bin isn't seated or gripper fails
- [ ] **Low-stock alerts** — Flag bins that are frequently empty or not returned

---

## Stretch Goals

- [ ] **Bulk return mechanism** — Accept multiple bins in a queue instead of one-by-one
- [ ] **Vision-based quantity estimation** — Estimate item count from return photo, record in database
- [ ] **Vision-based content validation** — Alert if wrong items are placed in a bin (e.g., screw in washer bin)
- [ ] **3D model content parsing** — Generate 3D model of bin contents for richer inventory records
- [ ] **Additional bin sizes** — Support larger bins (e.g., 8" x 12") alongside standard 6" x 8"
- [ ] **Integration with Lab Inventory Tracker** — Share item database with the vision-based checkout system

---

## Links

- **Jira Epic:** [TBD]
- **GitHub Repo:** [TBD]
- **Viam Organization:** [TBD]
- **Hardware BOM:** [TBD]

---

## Technical Details

~1m x 1m x 0.5m V-slot aluminum frame. Up to 29 bins (4" x 6") in a grid. Gantry rides on V-wheels with GT2 belt drive, one NEMA 23 stepper per axis.

**Retrieval:** User selects item on touchscreen → controller looks up bin slot → gantry moves to slot, grips bin → delivers to pickup window → IR sensor confirms position, RFID verifies identity → status set to "in use."

**Return:** User places bin in return slot → IR detects, RFID identifies → (Option C: camera snapshots contents) → gantry returns bin to its slot → status set to "stored."

**State:** Each bin has a unique RFID tag. Controller maintains a `slot (row, col) → bin ID` map. Reindexing routine scans all slots to rebuild the map if needed.

**Comms:** Steppers via GPIO/motor controller, RFID over I2C/SPI (PN532), IR sensors via ADC, touchscreen via DSI, cloud sync via Viam data management.

---

## Notes

**Why RFID over fixed slot assignment:** Bins can be physically rearranged without breaking the system — just reindex. Tags are ~$0.50 each.

**Why this project is compelling:**

- Solves a real daily problem — will actually be used after the hackathon
- Visually impressive demo (bins moving autonomously in a grid)
- Broad Viam coverage (hardware, data, remote monitoring, modules) without needing an expensive robot arm
- Modular — start with one column (Option A), scale to full grid

**Risk Factors:**

- Mechanical tolerances for reliable gripper engagement
- RFID read reliability through bin material
- Protruding bin contents can collide with the gripper or frame during transport
