# Project: Vino

## Overview

**One-line description:** Wine service robot that pours and serves wine on demand

**Project Lead:** TBD
**Team Members:** TBD
**Status:** Existing (has backlog)

## Description

Vino is a robotic wine service system using an arm and gripper to handle bottles and pour wine. The robot can retrieve bottles from a rack, identify wines, pour measured amounts, and potentially serve guests.

This project demonstrates manipulation capabilities, vision-based detection, and creates a highly engaging demo suitable for events and visitors.

## Viam Capabilities Demonstrated

- [x] Motion / Arm Control
- [x] Gripper Manipulation
- [x] Vision / ML (pour level detection, glass detection)
- [x] Data Management (pour analytics)
- [ ] Fleet Management
- [x] Remote Operation
- [x] Modular Resources
- [ ] Multi-machine Coordination
- [x] Cloud Integration
- [x] Customer Delivery ← **Primary customer-facing demo**
- [x] Triggers ← **Glass placement, bottle empty**
- [x] Scheduled Tasks ← **Cleaning cycles**

## Hardware Requirements

| Component | Description | Options |
|-----------|-------------|---------|
| Arm | 6-DOF robot arm | xArm 6, xArm 5 Lite, UFactory Lite 6 |
| Gripper | Bottle/glass handling | Parallel jaw, soft gripper |
| Camera | Bottle/glass detection | Intel RealSense, USB camera |
| Wine Rack | Bottle storage | Custom with known positions, or vision-based |
| Compute | Main controller | Raspberry Pi 4, Intel NUC |

**Estimated Hardware Cost:** $TBD (arm is primary cost)

**Remote-Friendly:** Partially - can develop control logic remotely, physical testing requires hardware

---

## MVP Options

Select one for hackathon scope:

### Option A: Pour on Demand (Recommended)
Arm picks bottle from rack, pours measured amount into glass at fixed location.
- **Complexity:** Medium
- **Demo Appeal:** High
- **Scope:** Single bottle type, fixed glass position, timed pour

### Option B: Glass Detection Pour
Vision detects glass placement, arm pours into detected glass.
- **Complexity:** Medium-High
- **Demo Appeal:** High
- **Scope:** Adds vision requirement, flexible glass positioning

### Option C: Wine Selector
User selects wine via app/voice, arm retrieves correct bottle from rack.
- **Complexity:** Medium
- **Demo Appeal:** Medium
- **Scope:** Multiple bottles, selection interface, retrieval logic

### Option D: Sommelier Display
Camera reads wine label, displays pairing suggestions and tasting notes.
- **Complexity:** Low-Medium
- **Demo Appeal:** Medium
- **Scope:** Vision + ML for label reading, database integration

**Selected MVP:** _______________

---

## Backlog

Select 3-5 items for post-hackathon development:

### Manipulation & Pouring
- [ ] **Multiple bottle types** - Handle different bottle shapes/sizes
- [ ] **Pour level detection** - Camera monitors fill level, stops at right amount
- [ ] **Glass handoff** - Robot hands glass to person or mobile robot

### Data & Monitoring
- [ ] **Temperature monitoring** - Track wine storage temps, alert if out of range
- [ ] **Inventory tracking** - Track bottles consumed, sync to cloud
- [ ] **Pour analytics** - Track pours by wine type, time, etc.

### User Interaction
- [ ] **Voice commands** - "Pour me a glass of the Pinot"
- [ ] **Mobile app** - Wine selection and service interface
- [ ] **Guest preferences** - Remember what guests like

### Scale & Fleet
- [ ] **Multi-station fleet** - Multiple Vino units in different locations
- [ ] **Centralized inventory** - Unified wine inventory across stations

### Customer Delivery (Gap Feature)
- [ ] **Web ordering interface** - TypeScript SDK web app for ordering pours
- [ ] **Guest authentication** - Simple login for tracking preferences
- [ ] **Order queue display** - Show pending orders on screen
- [ ] **Pour history** - Track what each guest has ordered
- [ ] **Event mode** - Pre-configured for specific events/tastings
- [ ] **Billing demo** - Demonstrate per-pour billing capability

### Triggers (Gap Feature)
- [ ] **Glass placement trigger** - Weight sensor detects glass, starts pour sequence
- [ ] **Bottle empty alert** - Trigger alert when bottle weight indicates empty
- [ ] **Temperature alert** - Alert if wine storage temp out of range
- [ ] **Order received trigger** - Start pour sequence when order placed via app

### Scheduled Tasks (Gap Feature)
- [ ] **End-of-day cleaning** - Scheduled cleaning cycle for gripper/pour area
- [ ] **Inventory check** - Daily inventory snapshot for tracking
- [ ] **Temperature log** - Periodic temperature readings to cloud

---

## Stretch Goals

- [ ] Wine recommendation engine based on preferences/history
- [ ] Decanting with timed aeration
- [ ] Label scanning with vintage database lookup
- [ ] Party mode: queue up orders from multiple guests
- [ ] Integration with wine cellar management systems

---

## Success Criteria

**MVP Complete When:**
- [ ] Robot can pick up a bottle from rack
- [ ] Robot can pour wine into a glass
- [ ] Pour amount is reasonably consistent
- [ ] Demo runs reliably 3+ times in a row

**Project Complete When:**
- [ ] All selected backlog items implemented
- [ ] Documentation complete
- [ ] Can be operated by someone not on the team

---

## Documentation Deliverables

- [ ] README with setup instructions
- [ ] Hardware assembly guide
- [ ] Configuration reference
- [ ] Demo operation guide
- [ ] Video of system in operation

---

## Links

- **Existing Code:** ~/viam/vino
- **Jira Epic:** [TBD]
- **GitHub Repo:** [TBD]
- **Viam Organization:** [TBD]
- **Hardware BOM:** [TBD]

---

## Notes

**Gap Features This Project Addresses:**
- **Customer Delivery** - Primary demo of customer-facing SDK (TypeScript web app for ordering)
- **Triggers** - Glass placement sensor, bottle empty alerts, order-received triggers
- **Scheduled Tasks** - End-of-day cleaning, inventory snapshots

**Why customer delivery fits here:**
- Vino has natural guest appeal - visitors want to interact
- Web ordering interface demonstrates TypeScript SDK
- Per-pour billing demonstrates Viam's billing capabilities
- Event mode shows configuration for specific use cases
