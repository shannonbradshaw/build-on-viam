# Project: Apple Processing

## Overview

**One-line description:** One or more arms capable of picking up, coring, and peeling each of a basket of apples.

**Project Lead:** Peter LoVerso
**Team Members:** TBD
**Status:** New

## Description

Applesauce is a robotic apple processing system using at least one arm with a soft gripper to pick apples from a basket, core them using a coring tool, and peel them using a benchtop peeler.

Coring is done by locating the stem and calyx of the apple, ensuring the apple is gripped in such a way that neither are occluded, and piercing the apple with a corer on the stem-calyx trajectory.

This project combines manipulation complexity (multi-step processing workflow), vision/ML (apple detection and orientation), and operational features (throughput tracking, quality monitoring).

---

## MVP Options

Select one for hackathon scope:

### Option A: Peel and core apples
Recognize, grasp, correctly core, and peel apples
- **Complexity:** Medium
- **Demo Appeal:** High
- **Scope:** Place a basket of apples in a defined part of the arm's workspace. Hit "go". Wind up with a bin of apple cores, a bin of apple peels, and a bin of cored, peeled apples.


### Option B: Full Processing + Slicing
Recognize, grasp, core, peel, and slice apples into segments
- **Complexity:** High
- **Demo Appeal:** Deliciously high
- **Scope:** Adds slicing mechanism and additional manipulation step

**Selected MVP:** _______________

---

## Viam Capabilities Demonstrated

### Core Capabilities
- [x] **Hardware Integration** — Arm, gripper, peeler, corer, depth camera
- [x] **Motion Planning** — Complex multi-step manipulation workflow
- [x] **Spatial mathematics** — Determination of optimal coring trajectory based on location of apple's stem and calyx
- [x] **Vision / ML Inference** — Identification of individual apples, identification of location of stem and calyx for core removal
- [x] **Data Capture & Sync** — Capture and store images and pointclouds of apples for debugging
- [x] **Module Development** — Apple grabbing, image processing, peeler actuation, etc will be distributed as a module
- [x] **Fragments** — Hardware configuration as reusable fragment
- [x] **Multi-Component Coordination** — The arm must coordinate with the coring mechanism and the peeling mechanism.

### Scale & Fleet Capabilities
- [x] **Fleet Management** — Multiple processing stations with centralized monitoring
- [x] **OTA Updates** — Module and configuration updates via Registry
- [x] **Provisioning** — Fragment-based configuration reuse

### Operational Capabilities
- [x] **Scheduled Tasks** — Batch processing runs, cleaning cycles
- [x] **Monitoring & Alerting** — Throughput tracking, error detection, bin full alerts
- [x] **Data Pipeline (ML Training)** — Apple images for detection model improvement

## Hardware Requirements

| Component | Description | Specific Model |
|-----------|-------------|----------------|
| Arm(s) | 6/7-DOF robot arm | UFACTORY xArm 6 or 7 |
| Gripper | Apple selection | Soft robotics 3-finger pneumatic gripper |
| Wrist Camera | Close-up detection | Intel RealSense D415 |
| Overview Camera | Workspace monitoring | USB webcam |
| Apple Corer | Apple Corer | TBD |
| Apple Peeler | Apple Peeler | Benchtop apple peeler |
| Stepper motor | Apple Peeler Actuation | Power for benchtop peeler actuation |
| Apples | Apples | Apples |
| Compute | Main controller | TBD |

**Remote-Friendly:** Partially - control logic can be developed remotely, physical testing requires hardware. All needed hardware exists with Peter in the Bend office, but it would be neat to build a twin in NYC

---

## Backlog

Select 3-5 items for post-hackathon development:

### Vision & ML
- [ ] **Apple detection model** - Detect and localize apples in basket
- [ ] **Ripeness assessment** - Grade apple readiness by color/texture
- [ ] **Defect detection** - Identify bruises, rot, damage
- [ ] **Stem/calyx localization** - Precise orientation for optimal coring

### Process Optimization
- [ ] **Grip force calibration** - Optimize grip to avoid bruising
- [ ] **Path optimization** - Minimize cycle time between stations
- [ ] **Speed tuning** - Balance throughput vs. quality
- [ ] **Error recovery** - Handle dropped apples, missed cores

### Fleet & Monitoring
- [ ] **Multi-station dashboard** - Monitor multiple processing lines
- [ ] **Throughput tracking** - Apples per hour, yield metrics
- [ ] **Quality alerts** - Notify on high defect rates
- [ ] **Maintenance scheduling** - Track blade wear, cleaning cycles



---

## Stretch Goals

- [ ] Multi-apple batching (process multiple apples in parallel)
- [ ] Apple quality sorting before processing
- [ ] Cooking system integration (handoff to applesauce pot)
- [ ] Variety detection (identify apple type for recipe adjustment)
- [ ] Automated bin management (detect full bins, swap containers)

---

## Links

- **Jira Epic:** [TBD]
- **GitHub Repo:** [TBD]
- **Viam Organization:** [TBD]
- **Hardware BOM:** [TBD]

---

## Technical Details

### Processing Workflow Sequence

```
1. DETECT APPLE
   ├── Scan basket with wrist camera
   ├── Identify apple location and orientation
   └── Plan grasp approach

2. PICK APPLE
   ├── Move arm to apple location
   ├── Soft grip apple (avoid bruising)
   └── Lift from basket

3. CORE APPLE
   ├── Position apple at coring station
   ├── Detect stem/calyx orientation via camera
   ├── Align coring tool with optimal trajectory
   ├── Execute coring motion
   └── Deposit core in waste bin

4. PEEL APPLE
   ├── Move to benchtop peeler
   ├── Mount apple on peeler spindle
   ├── Actuate stepper motor for rotation
   └── Collect peels in peel bin

5. OUTPUT
   ├── Remove peeled/cored apple
   └── Place in output bin

6. REPEAT
   └── Return to step 1 for next apple
```

### Workspace Layout

```
     [Apple Basket]
           │
           ▼
    ┌─────────────────────────────────┐
    │                                 │
    │      [UFACTORY xArm 6/7]        │
    │             │                   │
    │   ┌─────────┼─────────┐         │
    │   │         │         │         │
    │   ▼         ▼         ▼         │
    │ [Corer]  [Peeler]  [Output Bin] │
    │                                 │
    │   [Core Bin]  [Peel Bin]        │
    └─────────────────────────────────┘
```

### Key Manipulation Challenges

| Task | Challenge | Solution |
|------|-----------|----------|
| Apple grasp | Varying sizes, avoid bruising | Soft pneumatic gripper with force sensing |
| Orientation detection | Find stem/calyx for coring | Wrist camera + ML model |
| Coring grasping | Gripper must not occlude coring trajectory | Vision-guided positioning |
| Coring alignment | Precise trajectory needed | Vision-guided positioning |
| Peeler mounting | Secure apple on spindle | Controlled insertion force |
| Peel removal | Continuous spiral peel | Stepper motor speed control |

---

## Notes

**Why this project is compelling:**
- Demonstrates complex multi-step manipulation workflow
- Vision/ML integration for detection and orientation
- Tangible, relatable output (everyone understands apple processing)
- Good demo appeal (satisfying to watch)
- Exercises spatial math for coring trajectory

**Risk Factors:**
- Apple size variation requires adaptive grasping
- Bruising risk with improper grip force
- Core trajectory depends on accurate stem/calyx detection
- Peeler mounting may require custom fixture
- Sticky apple residue may require periodic cleaning
