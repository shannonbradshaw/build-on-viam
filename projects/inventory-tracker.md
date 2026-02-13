# Project: Lab Inventory Tracker

## Overview

**One-line description:** Track lab equipment checkout and return using RFID and cameras

**Project Lead:** TBD
**Team Members:** TBD
**Status:** New

## Description

Lab Inventory Tracker solves the "where's the hex wrench?" problem using RFID readers and cameras at checkout stations near lab doors. Users wave RFID-tagged items near a reader to check them out or return them, and the system captures photos for an audit trail.

The system tracks item status (checked out / in lab), syncs data to Viam cloud, and sends Slack notifications when items are overdue — providing accountability and visibility into lab equipment usage.

---

## MVP

Detect hex wrench checkout events and capture photos for audit trail. Checkout stations at both doors to the lab.

### Checkout Flow
- User waves object close to checkout station with RFID reader and gets confirmation with a beep
- System captures: tag_id, timestamp, station_id + picture(s)
- Data syncs to Viam cloud
- Item marked as "checked out" in inventory DB

### Return Flow
- User returns item, waves it near RFID reader
- RFID reader detects tag at return location
- Item status updated to "in lab"
- Optionally, capture a picture

### Late Notice
- Items that have been checked out too long trigger a message in a Slack channel with the item name, picture of person who carried it out, and request to return the item

---

## Viam Capabilities Demonstrated

### Core Capabilities
- [x] **Hardware Integration** — RFID reader, camera, Raspberry Pi
- [ ] **Motion Planning** — Not applicable
- [ ] **Vision / ML Inference** — Stretch: item recognition from captured images
- [x] **Data Capture & Sync** — Checkout images synced to cloud with offline resilience
- [x] **Remote Operation** — Full remote monitoring and development
- [x] **Module Development** — Checkout station module
- [x] **Fragments** — Checkout station configuration as reusable fragment

### Scale & Fleet Capabilities
- [x] **Fleet Management** — Multiple checkout stations with centralized view
- [x] **OTA Updates** — Module and configuration updates via Registry
- [x] **Provisioning** — Fragment-based configuration reuse

### Operational Capabilities
- [x] **Scheduled Tasks** — Daily summaries, weekly utilization reports
- [ ] **Monitoring & Alerting** — Backlog: station health, low activity alerts
- [ ] **Data Pipeline (ML Training)** — Stretch: captured images → labeling → item models → deploy

### Customer-Facing Capabilities
- [x] **Customer Delivery** — Dashboard for viewing checkouts and audit trail
- [x] **Web/Mobile Apps** — Web dashboard, mobile-friendly checkout status

### Multi-Machine Coordination
- [x] **Stations report to central system** — Centralized view across all locations

## Hardware Requirements

| Component | Description | Options |
|-----------|-------------|---------|
| Compute | Checkout station controller | Raspberry Pi |
| Camera | Capture person + item for audit trail | USB webcam, Pi Camera |
| RFID Reader | Detect tagged items | RFID reader |
| RFID Tags | Applied to tracked items | RFID tags |

**Stations:** Checkout stations at both doors to the lab

**Remote-Friendly:** Yes - app development remote, physical setup minimal

---

## Backlog

### Phase 1: RFID Checkout & Notify
- [ ] **RFID reader integration** - Read RFID tags at checkout stations
- [ ] **Checkout confirmation** - Audible beep on successful tag read
- [ ] **Photo capture** - Capture image on checkout/return event
- [ ] **Cloud storage** - Save tag_id, timestamp, station_id, and images to Viam data management
- [ ] **Inventory DB** - Track item status (checked out / in lab)
- [ ] **Slack notification** - Send photo + item info to channel on each checkout
- [ ] **Late notice** - Alert in Slack when items are overdue with photo of person who checked it out

### Phase 2: Item Recognition
- [ ] **Training data export** - Export labeled images for model training
- [ ] **Item classifier** - Train model to recognize common lab equipment
- [ ] **Auto-labeling** - Apply model to new checkouts
- [ ] **Confidence thresholds** - Flag low-confidence detections for review
- [ ] **Unknown item handling** - Queue unrecognized items for labeling
- [ ] **Model retraining pipeline** - Improve model as more data collected

### Phase 3: Face Recognition
- [ ] **User consent flow** - Opt-in for face recognition
- [ ] **Face database** - Store face embeddings for enrolled users
- [ ] **Face matching** - Identify person during checkout
- [ ] **Privacy controls** - Users can delete their data, opt out
- [ ] **Unknown person handling** - Prompt for identification or flag for review

### Event-Driven Automation (Gap Feature)
- [ ] **Checkout detected** - Capture + notification on RFID tag read
- [ ] **Overdue reminder** - Item not returned after N days, notify via Slack
- [ ] **Escalating alerts** - 3 days, 7 days, then notify manager
- [ ] **Return detected** - RFID tag read at return station

### Scheduled Tasks (Gap Feature)
- [ ] **Daily summary** - Morning report of previous day's checkouts
- [ ] **Weekly utilization** - Most checked-out items, longest holds
- [ ] **Shelf audit** - Periodic shelf camera capture for reconciliation

### Customer Delivery (Gap Feature)
- [ ] **Web dashboard** - View all checkouts, search, filter
- [ ] **Mobile-friendly** - Check inventory status from phone
- [ ] **Per-team views** - Filter by team or location
- [ ] **Admin tools** - Manage items, users, locations

### Data Pipeline (Gap Feature)
- [ ] **Image capture** - Every checkout builds training dataset
- [ ] **Labeling interface** - Easy annotation of item + person
- [ ] **Model training** - Train/retrain in Viam
- [ ] **Model deployment** - Push updated models to stations
- [ ] **A/B testing** - Compare model versions

### Fleet & Scale
- [ ] **Multiple stations** - Hardware lab, supply closet, kitchen
- [ ] **Centralized view** - All stations in one dashboard
- [ ] **Station fragments** - Reusable config per checkout station
- [ ] **Cross-location search** - "Where's the RealSense?" across all locations

---

## Stretch Goals

- [ ] Return detection via shelf camera (item reappears)
- [ ] Voice assistant ("Where's the soldering iron?")
- [ ] Reservation system for high-demand items
- [ ] Integration with procurement (auto-reorder on low stock)
- [ ] Mobile app for checking inventory on the go

---

## Links

- **Jira Epic:** [TBD]
- **GitHub Repo:** [TBD]
- **Viam Organization:** [TBD]
- **Hardware BOM:** [TBD]

---

## Technical Details

### Checkout Flow

```
1. User waves RFID-tagged item near checkout station reader
2. RFID reader detects tag, system emits confirmation beep
3. Camera captures photo of person + item
4. System records: tag_id, timestamp, station_id, image
5. Data syncs to Viam cloud
6. Item marked as "checked out" in inventory DB
```

### Return Flow

```
1. User waves item near RFID reader at return station
2. RFID reader detects tag
3. Item status updated to "in lab"
4. Optionally capture return photo
```

### Data Schema

```
checkouts:
  - id: string (uuid)
  - tag_id: string (RFID tag identifier)
  - timestamp: datetime
  - image_url: string (cloud storage path)
  - station_id: string
  - event_type: enum (checkout, return)
  - status: enum (checked_out, in_lab)

items:
  - id: string
  - tag_id: string (RFID tag)
  - name: string
  - category: string
  - location: string (home station)

stations:
  - id: string
  - name: string
  - location: string (e.g., "east door", "west door")
```

### Notification Format

**Slack checkout message:**
```
Checkout detected
Hardware Lab - East Door
10:32 AM

[Photo of person with item]

Item: Hex Wrench Set #3 (tag: RF-0042)
```

**Slack late notice:**
```
Overdue item - please return
Hex Wrench Set #3 checked out 3 days ago

[Photo from checkout]

Please return to any checkout station.
```

---

## Notes

**Why RFID:**
- Reliable, deterministic identification — no ML required for core functionality
- Low friction for users — just wave and go
- Works immediately with tagged items
- Photo capture provides audit trail and supports late notices

**Gap Features This Project Addresses:**
- **Event-Driven Automation** - RFID checkout detection, overdue alerts
- **Data Pipeline** - Stretch: captured images → labeling → item recognition
- **Scheduled Tasks** - Daily summaries, weekly reports
- **Customer Delivery** - Dashboard with audit trail

**Why this approach is valuable:**
- Works on day one with zero training
- Deterministic item identification via RFID tags
- Photo audit trail adds accountability
- Slack integration for overdue items solves a real team problem
- System will actually be used after hackathon
