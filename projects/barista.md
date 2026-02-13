# Project: Barista

## Overview

**One-line description:** Single-arm robot that operates an espresso station like a human barista

**Project Lead:** TBD
**Team Members:** TBD
**Status:** New

## Description

Barista is a robotic coffee preparation system where a single UFACTORY 850 arm performs all the steps a human barista would: grabbing the portafilter, holding it under the grinder, placing it on an auto-tamper, locking it into the espresso machine, brewing the shot, steaming milk, and assembling drinks. Customers order via a tablet interface and watch their drink being prepared.

Unlike systems that use fully-automatic espresso machines, this project uses a semi-automatic machine with a robot performing the manipulation. This approach mirrors commercial robotic baristas like [Rozum Cafe](https://cafe.rozum.com/) while demonstrating advanced manipulation skills.

This project combines manipulation complexity (multi-step beverage preparation), customer-facing interaction (ordering interface), and operational features (inventory tracking, scheduling, quality monitoring).

## Viam Capabilities Demonstrated

### Core Capabilities
- [x] **Hardware Integration** — Arm, gripper, espresso machine, grinder, auto-tamper, cameras
- [x] **Motion Planning** — Complex multi-step manipulation workflow
- [x] **Vision / ML Inference** — Cup detection, fill level, foam quality assessment
- [x] **Data Capture & Sync** — Order history, drink analytics synced to cloud
- [x] **Remote Operation** — Develop control logic remotely
- [x] **Module Development** — Custom barista service module
- [x] **Fragments** — Hardware configuration as reusable fragment

### Scale & Fleet Capabilities
- [x] **Fleet Management** — Multiple coffee stations with centralized monitoring
- [x] **OTA Updates** — Module and configuration updates via Registry
- [x] **Provisioning** — Fragment-based configuration reuse

### Operational Capabilities
- [x] **Scheduled Tasks** — Morning warmup, cleaning cycles, inventory check
- [x] **Monitoring & Alerting** — Bean level, water, temperature, usage metrics
- [x] **Data Pipeline (ML Training)** — Drink quality images, shot timing for grind tuning

### Customer-Facing Capabilities
- [x] **Customer Delivery** — Tablet ordering interface, guest profiles
- [x] **Web/Mobile Apps** — TypeScript/Flutter SDK ordering apps

## Hardware Requirements

| Component | Description | Specific Model |
|-----------|-------------|----------------|
| Arm | 6-DOF robot arm | UFACTORY 850 (850mm reach, 5kg payload) |
| Gripper | Portafilter/pitcher handling | UFACTORY Gripper |
| Auto-tamper | Consistent 30lb tamp pressure | PUQpress Gen 5 Q2 |
| Espresso Machine | Semi-automatic, rocker switches | Gaggia RI9380/46 E24 |
| Grinder | Portafilter-activated, 60mm flat burrs | Eureka Atom |
| Wrist Camera | Close-up detection | Intel RealSense D405 |
| Overview Camera | Workspace monitoring | USB webcam |
| Tablet | Order interface | TBD |
| Knockbox | Puck disposal | Standard knockbox |
| Milk Pitcher | Steaming vessel | Standard 12oz pitcher |
| Compute | Main controller | System76 Meerkat |

**Remote-Friendly:** Partially - control logic can be developed remotely, physical testing requires hardware

---

## MVP

Brew a shot of espresso. Robot can place an empty portafilter under the grinder, wait for the grind to finish, and withdraw it; move the portafilter to the tamper, get a tamp, and withdraw it; insert the portafilter into the espresso machine and lock into place.

---

## Backlog

Select 3-5 items for post-hackathon development:

### Core Workflow
- [ ] **Portafilter handling** - Grab, hold, lock-in, remove
- [ ] **Grinder operation** - Position under grinder, activate, dose
- [ ] **Auto-tamper integration** - Place on Puqpress, retrieve
- [ ] **Shot pulling** - Lock portafilter, start brew, monitor
- [ ] **Puck disposal** - Knock out puck, clean portafilter

### Milk Steaming
- [ ] **Pitcher handling** - Grab pitcher, position under wand
- [ ] **Steam wand operation** - Hold during steaming
- [ ] **Pour milk** - Pour steamed milk into cup
- [ ] **Foam quality detection** - ML model assesses microfoam

### Drink Variations
- [ ] **Multiple drink types** - Espresso, Americano, Latte, Cappuccino
- [ ] **Size variations** - Small, Medium, Large cups
- [ ] **Strength options** - Single, double shots
- [ ] **Milk alternatives** - Different pitchers for oat, almond

### Customer Delivery (Gap Feature)
- [ ] **Tablet ordering interface** - TypeScript SDK app
- [ ] **Mobile app** - Flutter SDK for remote ordering
- [ ] **Guest profiles** - Remember regular orders
- [ ] **Order queue display** - Show pending orders
- [ ] **Order status** - Real-time prep progress

### Event-Driven Automation (Gap Feature)
- [ ] **Order received** - Start preparation sequence
- [ ] **Brew complete** - Detect shot done, proceed to next step
- [ ] **Low beans alert** - Weight sensor activates refill alert
- [ ] **Temperature alert** - Alert if brew temp out of range

### Scheduled Tasks (Gap Feature)
- [ ] **Morning warmup** - Pre-heat machine before office opens
- [ ] **Cleaning cycle** - Daily backflush routine
- [ ] **Inventory check** - Daily bean/water level report

### Data Pipeline (Gap Feature)
- [ ] **Drink image capture** - Photo of every finished drink
- [ ] **Shot time tracking** - Extraction times for grind tuning
- [ ] **Quality labeling** - Rate drinks for training data

---

## Stretch Goals

- [ ] Voice ordering ("Hey Barista, make me a latte")
- [ ] Latte art pour patterns
- [ ] Grind size auto-adjustment based on shot timing
- [ ] Multiple bean hoppers with selection
- [ ] Calendar integration (coffee ready when meeting ends)

---

## Links

- **Jira Epic:** [TBD]
- **GitHub Repo:** [TBD]
- **Viam Organization:** [TBD]
- **Hardware BOM:** [TBD]

---

## Technical Details

### Single-Arm Workflow Sequence

```
1. RECEIVE ORDER
   └── Event: Order placed via tablet

2. PREPARE PORTAFILTER
   ├── Grab portafilter from holder
   ├── Move to grinder
   ├── Push portafilter against fork (auto-activates grind)
   └── Hold until dose complete

3. TAMP
   ├── Move to Puqpress
   ├── Place portafilter on tamper
   ├── Wait for tamp completion (~1.3 sec)
   └── Retrieve portafilter

4. BREW
   ├── Move to espresso machine group head
   ├── Lock portafilter (twist motion)
   ├── Position cup under spout
   ├── Activate brew (button or lever)
   └── Wait for shot completion (~25-30 sec)

5. STEAM MILK (if latte/cappuccino)
   ├── Grab milk pitcher
   ├── Position under steam wand
   ├── Activate steam
   ├── Hold for steaming duration
   └── Pour milk into cup

6. SERVE
   ├── Move cup to pickup location
   └── Signal order ready

7. CLEANUP
   ├── Remove portafilter from group head
   ├── Knock out puck into knockbox
   └── Return portafilter to holder
```

### Workspace Layout

```
        [Grinder]     [Espresso Machine]
            │              │
            ▼              ▼
    ┌───────────────────────────────────┐
    │                                   │
    │           [UFACTORY 850]          │
    │                │                  │
    │    ┌───────────┼───────────┐      │
    │    │           │           │      │
    │    ▼           ▼           ▼      │
    │ [Puqpress]  [Cups]    [Knockbox]  │
    │                                   │
    │         [Milk Pitcher]            │
    │                                   │
    │      [Pickup] ← Customer          │
    └───────────────────────────────────┘
```

### Key Manipulation Challenges

| Task | Challenge | Solution |
|------|-----------|----------|
| Portafilter lock-in | Requires twist motion under spring pressure | Compliant motion, force feedback |
| Grinder activation | None - portafilter-activated | Push against fork, auto-grinds |
| Tamping | None - auto-tamps | Place on Puqpress, auto-tamps |
| Steam wand positioning | Hold steady during steaming | Fixed wand angle, move pitcher |
| Puck knockback | Firm tap required | Controlled velocity impact |

### Minimal Button Workflow

Both the Eureka Atom grinder and Puqpress Q2 are sensor-activated:
- **Grinder:** Portafilter fork switch triggers grinding when pressed
- **Tamper:** Sensor detects portafilter placement, auto-tamps in 1.3 sec

The only button the robot needs to press is the **Gaggia E24 brew rocker switch**. The rocker switch design is easier for a robot arm to actuate than push buttons.

### Espresso Machine

**Selected:** Gaggia RI9380/46 E24 - rocker switches are easy for robot to press, 58mm commercial portafilter, well-documented Pi mods available.

### References

- [Rozum Cafe](https://cafe.rozum.com/) - Commercial robotic barista
- [Cafe X](https://www.cafexapp.com/) - Single-arm robotic coffee bar
- [Artly Coffee](https://artly.coffee/) - AI-trained robotic barista
- [Eureka Atom](https://www.eureka.co.it/en/products/espresso_line_home/atom.aspx) - Portafilter-activated grinder
- [Puqpress Q2](https://puq.coffee/) - Automatic tamper with 22-66lb adjustable pressure
- [Gaggia Classic Pro](https://www.gaggia.com/manual-machines/new-classic/) - Semi-automatic with rocker switches
- [Gaggia Classic Pi Mods](https://github.com/esrice/piggia) - Open source Pi control for Gaggia

---

## Notes

**Why single arm works:**
- Sequential workflow is natural for coffee making
- One arm is sufficient for all manipulation tasks
- Simpler development
- Commercial systems (Cafe X) use single arm successfully

**Why Puqpress instead of robot tamping:**
- UFACTORY 850 payload (5kg/11lb) < required tamp force (30lb)
- Auto-tamper ensures consistent pressure
- This is what commercial robotic baristas do
- Robot still does all other manipulation

**Gap Features This Project Addresses:**
- **Customer Delivery** - Ordering interface with TypeScript/Flutter SDKs
- **Event-Driven Automation** - Order received, brew complete, inventory alerts
- **Scheduled Tasks** - Morning warmup, cleaning cycles
- **Monitoring/Alerting** - Bean level, water, temperature, usage
- **Data Pipeline** - Drink quality images, shot timing data

**Risk Factors:**
- Portafilter lock-in requires precise force control
- Steam wand manipulation is complex
- Hot liquids require safety considerations
- Espresso quality depends on many variables
