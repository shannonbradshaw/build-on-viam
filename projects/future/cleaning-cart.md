# Project: Cleaning Cart

## Overview

**One-line description:** Mobile robot that collects dishes, cups, and trash from around the office

**Project Lead:** TBD
**Team Members:** TBD
**Status:** Future

## Description

Cleaning Cart is a mobile robot that patrols the office collecting dirty dishes, cups, and trash left on desks. It navigates autonomously, identifies items to collect, and either alerts humans or collects items directly. Collected dishes are brought to the kitchen for handoff to the dishwasher robot.

This project demonstrates navigation, SLAM, vision detection, and multi-robot coordination.

## Viam Capabilities Demonstrated

### Core Capabilities
- [x] **Hardware Integration** — Mobile base, lidar, camera, optional arm/gripper
- [ ] **Motion Planning** — Stretch: arm manipulation for item collection
- [x] **Vision / ML Inference** — Item detection and classification
- [x] **Data Capture & Sync** — Patrol data, detection logs synced to cloud
- [x] **Remote Operation** — Remote monitoring and control
- [ ] **Module Development** — Not primary focus
- [x] **Fragments** — Patrol route configs as reusable fragments

### Scale & Fleet Capabilities
- [x] **Fleet Management** — Multiple carts, coordination with dishwasher robot
- [x] **OTA Updates** — Module and configuration updates via Registry
- [x] **Provisioning** — Fragment-based configuration reuse

### Operational Capabilities
- [x] **Event-Driven Automation** — Motion-based pause, low battery return, tray full alert
- [x] **Scheduled Tasks** — Primary: multiple daily patrols (morning, post-lunch, end-of-day)
- [ ] **Monitoring & Alerting** — Backlog: patrol status dashboard
- [ ] **Data Pipeline (ML Training)** — Backlog: detection improvement

### Customer-Facing Capabilities
- [ ] **Customer Delivery** — Not applicable
- [ ] **Web/Mobile Apps** — Backlog: patrol monitoring dashboard

### Additional Capabilities
- [x] **Navigation / SLAM** — Office mapping, autonomous patrol routes
- [x] **Multi-Machine Coordination** — Dishwasher handoff, multi-cart fleet

## Hardware Requirements

| Component | Description | Options |
|-----------|-------------|---------|
| Mobile Base | Navigation platform | Create 3, Husarion ROSbot, custom base |
| Lidar | Mapping & navigation | RPLidar A1/A2, Velodyne Puck |
| Camera | Item detection | Intel RealSense D435, USB camera |
| Arm | Item collection (optional) | xArm Lite, small manipulator |
| Gripper | Item handling (optional) | Parallel jaw, tray carrier |
| Tray/Bins | Item storage | Mounted bins for dishes, trash |
| Compute | Main controller | Raspberry Pi 4, Jetson Nano |

**Remote-Friendly:** Partially - navigation and vision can be developed with simulation/recordings, full testing requires office environment

---

## MVP Options

Select one for hackathon scope:

### Option A: Patrol + Detect (Recommended)
Navigate office, detect and report dish/trash locations.
- **Complexity:** Medium
- **Demo Appeal:** High
- **Scope:** Navigation, mapping, detection - no manipulation

### Option B: Patrol + Alert
Above plus alert humans (Slack/notification) to collect items.
- **Complexity:** Medium
- **Demo Appeal:** Medium-High
- **Scope:** Adds notification integration

### Option C: Patrol + Collect (Simple)
Navigate to known stations, wait for humans to load items onto tray.
- **Complexity:** Medium
- **Demo Appeal:** High
- **Scope:** Navigation + transport, human-assisted loading

### Option D: Full Collection
Navigate, detect, pick up items autonomously.
- **Complexity:** Very High
- **Demo Appeal:** Very High
- **Scope:** Full mobile manipulation - very ambitious for hackathon

**Selected MVP:** _______________

---

## Backlog

Select 3-5 items for post-hackathon development:

### Navigation & Mapping
- [ ] **Office mapping** - Complete SLAM map of office space
- [ ] **Desk locations** - Named locations for each desk/area
- [ ] **Route optimization** - Efficient patrol routes based on data
- [ ] **Dynamic obstacles** - Handle people, moved chairs, etc.
- [ ] **Elevator integration** - Multi-floor operation

### Detection & Classification
- [ ] **Item classification** - ML distinguishes cups vs plates vs trash
- [ ] **Desk state detection** - Identify desks that need attention
- [ ] **Person detection** - Avoid interrupting people at desks
- [ ] **Spill detection** - Alert on spills for manual cleanup

### Collection & Transport
- [ ] **Arm manipulation** - Pick up items autonomously
- [ ] **Tray management** - Track tray capacity, know when full
- [ ] **Trash disposal** - Navigate to and use trash bins
- [ ] **Dishwasher handoff** - Coordinate with dishwasher robot

### Operations
- [ ] **Scheduled patrols** - Run routes at set times (after lunch, end of day)
- [ ] **Battery management** - Return to charge, resume patrol
- [ ] **Remote monitoring** - Live view of patrol status
- [ ] **Patrol reports** - Summary of items found/collected

### Scheduled Tasks (Gap Feature)
- [ ] **Morning patrol** - 8am sweep before employees arrive
- [ ] **Post-lunch patrol** - 1pm sweep after lunch rush
- [ ] **End-of-day patrol** - 6pm comprehensive sweep
- [ ] **Weekly deep clean** - Saturday full-office patrol
- [ ] **Meeting room check** - Scheduled check after calendar meetings end

### Event-Driven Automation (Gap Feature)
- [ ] **Motion sensor pause** - When person detected nearby, pause and wait
- [ ] **Low battery return** - Return to charger when battery < 20%
- [ ] **Tray full alert** - When tray capacity reached, alert and return to kitchen
- [ ] **Spill detection alert** - Alert facilities when spill detected
- [ ] **Calendar integration** - Start patrol when meeting ends (calendar API)

---

## Stretch Goals

- [ ] Voice interaction ("I have dishes for you")
- [ ] Calendar integration (patrol after meetings end)
- [ ] Guest mode (office tours, wayfinding)
- [ ] Package delivery to desks
- [ ] Multi-robot fleet (multiple carts)

---

## Success Criteria

**MVP Complete When:**
- [ ] Robot can navigate office without collisions
- [ ] Robot detects dishes/cups on desks via camera
- [ ] Robot completes a patrol route and reports findings
- [ ] Works reliably for 3+ patrol runs

**Project Complete When:**
- [ ] Full office map with named locations
- [ ] Detection accuracy >90% for common items
- [ ] All selected backlog items implemented
- [ ] Documentation complete

---

## Documentation Deliverables

- [ ] README with setup instructions
- [ ] Hardware assembly guide
- [ ] SLAM mapping guide
- [ ] Office configuration guide (locations, routes)
- [ ] Detection model training guide
- [ ] Operations guide (scheduling, monitoring)

---

## Links

- **Jira Epic:** [TBD]
- **GitHub Repo:** [TBD]
- **Viam Organization:** [TBD]
- **Hardware BOM:** [TBD]

---

## Notes

**Risk factors:**
- Mobile manipulation is very ambitious - consider MVP without arm
- Office environment is dynamic (people, chairs, obstacles)
- Navigation in cluttered space requires tuning
- May need to start with controlled/simplified environment

**Scope management:**
- Option A (patrol + detect) is achievable for hackathon
- Manipulation should be post-hackathon backlog
- Dishwasher handoff requires both projects to be working

**Alternative MVP approach:**
- Use existing mobile base (Create 3) if available
- Focus on navigation + detection only
- Mount camera and tray, no arm
- Human places items on tray, robot transports

**Gap Features This Project Addresses:**
- **Scheduled Tasks** - Primary demo of Viam's scheduling capabilities with multiple daily patrols
- **Event-Driven Automation** - Motion-based pause, battery alerts, capacity alerts
- **Fleet** - Potential for multiple carts in larger facility (stretch)
