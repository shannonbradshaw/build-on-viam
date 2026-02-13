# Project: Lab Inventory Tracker

## Overview

**One-line description:** Track lab equipment checkout and return using RFID and cameras

**Project Lead:** TBD
**Team Members:** TBD
**Status:** New

## Description

Lab Inventory Tracker solves the "where's the hex wrench?" problem using RFID readers and cameras at checkout stations near lab doors. Users wave RFID-tagged items near a reader to check them out or return them, and the system captures photos for an audit trail.

The system tracks item status (checked out / in lab), syncs data to Viam cloud, and sends Slack notifications when items are overdue — providing accountability and visibility into lab equipment usage.

## Viam Capabilities Demonstrated

### Core Capabilities
- [ ] **Hardware Integration** — Camera, optional button, display
- [ ] **Motion Planning** — Not applicable
- [x] **Vision / ML Inference** — Item recognition, face recognition (phased)
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
- [x] **Data Pipeline (ML Training)** — Primary: captured images → labeling → item/face models → deploy

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

**Remote-Friendly:** Yes - ML training fully remote, app development remote, physical setup minimal

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

## Backlog

### Phase 1: Capture & Notify
- [ ] **Checkout zone detection** - Define camera FOV region for checkout gestures
- [ ] **Motion/gesture detection** - Detect when someone holds up an item
- [ ] **Photo capture** - High-quality image of person + item together
- [ ] **Cloud storage** - Save images with timestamps to Viam data management
- [ ] **Slack notification** - Send photo + timestamp to channel on each checkout
- [ ] **Basic dashboard** - View recent checkouts with images
- [ ] **Manual labeling UI** - Add item name and person to captured checkouts

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
- [ ] **Checkout detected** - Capture + notification on gesture detection
- [ ] **Overdue reminder** - Item not returned after N days, notify (requires Phase 3)
- [ ] **Escalating alerts** - 3 days, 7 days, then notify manager
- [ ] **Return detected** - Item reappears on shelf camera (stretch)

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

### Checkout Detection

**Approach 1: Motion + Pose Detection**
```
1. Camera monitors checkout zone continuously
2. Motion detected → start analyzing frames
3. Detect "person holding object" pose
4. Capture high-res frame
5. Save + notify
```

**Approach 2: Simple Button**
```
1. Person holds up item
2. Presses physical button
3. Camera captures frame
4. Save + notify
```

**Approach 3: Dwell Time**
```
1. Camera monitors checkout zone
2. Person + object detected in zone
3. If stable for 2 seconds → capture
4. Save + notify
```

Recommendation: Start with Approach 2 (button) for reliability, evolve to Approach 1 or 3.

### Data Schema

```
checkouts:
  - id: string (uuid)
  - timestamp: datetime
  - image_url: string (cloud storage path)
  - item_name: string (nullable - manual or ML)
  - item_confidence: float (nullable - ML confidence)
  - person_name: string (nullable - manual or ML)
  - person_confidence: float (nullable - ML confidence)
  - station_id: string
  - status: enum (pending_review, labeled, auto_labeled)

items:
  - id: string
  - name: string
  - category: string
  - location: string (home station)
  - image_urls: array (reference images for training)

users:
  - id: string
  - name: string
  - email: string
  - team: string
  - face_enrolled: boolean
  - face_embedding: blob (nullable)
```

### Notification Format

**Slack message:**
```
📦 Checkout detected
📍 Hardware Lab Station
🕐 10:32 AM

[Embedded photo of person holding item]

Item: [Unknown - click to label] or [Intel RealSense D435]
Person: [Unknown - click to label] or [Shannon]
```

### ML Pipeline

**Item Recognition:**
1. Export labeled checkout images
2. Crop to item region (manual or detected)
3. Train classifier (transfer learning from ImageNet)
4. Deploy to checkout stations
5. Monitor accuracy, retrain as needed

**Face Recognition:**
1. Collect face images during enrollment (multiple angles)
2. Generate face embeddings (e.g., using face_recognition library)
3. Store embeddings in user database
4. On checkout, extract face → find nearest embedding
5. Apply confidence threshold for match

---

## Notes

**Why no tagging:**
- Zero friction for users - just hold up and go
- No inventory of tags to manage
- Works with any item immediately
- System improves over time through use

**Gap Features This Project Addresses:**
- **Event-Driven Automation** - Checkout detection, overdue alerts
- **Data Pipeline** - Images → labels → training → deployment
- **Scheduled Tasks** - Daily summaries, weekly reports
- **Customer Delivery** - Dashboard with audit trail

**Privacy Considerations:**
- Face recognition requires explicit opt-in
- Users can view and delete their data
- Option to use system without face recognition (photo audit only)
- Clear signage at checkout stations

**Why this approach is valuable:**
- Works on day one with zero ML training
- Builds its own training data through normal use
- Each phase adds value incrementally
- Solves real problem the team faces
- System will actually be used after hackathon
