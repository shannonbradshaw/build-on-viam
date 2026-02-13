# Project: Salad Maker

## Overview

**One-line description:** Dual-arm robot that assembles custom salads from a refrigerated prep station

**Project Lead:** TBD
**Team Members:** TBD
**Status:** New

## Description

Salad Maker is a dual-arm robotic system that assembles salads on demand. Two UFACTORY 850 arms work together to grab ingredients from a refrigerated prep rail using tongs-style grippers, building salads in bowls. Customers order via app or kiosk, selecting from preset recipes or customizing their own combination.

The dual-arm configuration enables parallel ingredient handling and bimanual coordination - one arm can hold the bowl while the other adds ingredients, or both arms can grab different ingredients simultaneously for faster assembly.

This project demonstrates advanced manipulation with dual-arm coordination, vision-based ingredient detection, customer-facing ordering, and real-time order fulfillment.

---

## MVP

Right arm picks up a bowl from a known pose and moves the bowl to a known pose. Left arm assembles a salad from a simple 3 ingredient recipe.

**Stretch:** Be consistent (within a given range) for the amount of each ingredient. Easiest would be by weight.

---

## Viam Capabilities Demonstrated

### Core Capabilities
- [x] **Hardware Integration** — Dual arms, grippers, cameras, prep station sensors
- [x] **Motion Planning** — Dual-arm coordination, collision avoidance
- [x] **Vision / ML Inference** — Ingredient detection, portion estimation
- [x] **Data Capture & Sync** — Order history, ingredient usage synced to cloud
- [x] **Remote Operation** — Develop coordination logic remotely
- [x] **Module Development** — Custom salad service module
- [x] **Fragments** — Hardware configuration as reusable fragment

### Scale & Fleet Capabilities
- [ ] **Fleet Management** — Stretch: multiple prep stations
- [x] **OTA Updates** — Module and configuration updates via Registry
- [ ] **Provisioning** — Stretch: multiple prep stations

### Operational Capabilities
- [x] **Scheduled Tasks** — Morning prep check, cleaning cycles, inventory checks
- [ ] **Monitoring & Alerting** — Backlog: ingredient levels, temperature
- [x] **Data Pipeline (ML Training)** — Portion images for grab consistency training

### Customer-Facing Capabilities
- [x] **Customer Delivery** — Ordering kiosk/app, order status display
- [x] **Web/Mobile Apps** — Flutter SDK for mobile ordering

### Multi-Machine Coordination
- [x] **Two arms working together** — Parallel grab, hold-and-add, collision avoidance

## Hardware Requirements

| Component | Description | Specific Model |
|-----------|-------------|----------------|
| Arms (2) | 6-DOF robot arms | UFACTORY 850 (850mm reach, 5kg payload) |
| Grippers (2) | Tongs-style end effectors | Custom or Robotiq Hand-E with tong fingers |
| Wrist Cameras (2) | Ingredient detection | Intel RealSense D405 (compact) |
| Overview Camera | Workspace monitoring | Intel RealSense D435 or USB webcam |
| Compute | Main controller | System76 Meerkat |
| Prep Station | Refrigerated ingredient rail | Avantco CPT-60-HC (59", 6x 1/3 pans) |
| Bowl Dispenser | Automated bowl dispensing | Cup/bowl dispenser mechanism |
| Handoff Station | Customer pickup area | Custom shelf/window |
| Dressing Station | Self-serve dressings | Pump bottles on counter |
| Mounting | Arm mounting structure | Custom gantry or dual pedestals |

**Remote-Friendly:** Partially - dual-arm coordination logic can be developed in simulation, physical testing requires full setup

---

## Backlog

Select 3-5 items for post-hackathon development:

### Dual-Arm Coordination
- [ ] **Parallel ingredient grab** - Both arms grab different ingredients simultaneously
- [ ] **Bowl handoff** - One arm passes bowl to the other
- [ ] **Hold and add** - One arm holds bowl while other adds ingredients
- [ ] **Collision avoidance** - Coordinated motion planning for shared workspace
- [ ] **Toss and catch** - One arm tosses salad while other holds bowl (stretch)

### Manipulation & Gripping
- [ ] **Tongs calibration** - Consistent grip force for different ingredients
- [ ] **Portion control** - Grab consistent amounts each time
- [ ] **Leafy greens handling** - Special technique for lettuce/spinach
- [ ] **Crouton/nut handling** - Small item gripping
- [ ] **Tool change** - Swap between tongs and scoop attachments

### Vision & Detection
- [ ] **Ingredient identification** - ML model identifies ingredient type
- [ ] **Pan level detection** - Estimate remaining ingredient quantity
- [ ] **Portion estimation** - Vision-based portion size verification
- [ ] **Bowl position detection** - Find bowl for flexible placement
- [ ] **Quality detection** - Identify wilted or expired ingredients

### Customer Delivery (Gap Feature)
- [ ] **Ordering kiosk** - Touchscreen interface for ordering
- [ ] **Mobile app** - Flutter SDK for remote ordering
- [ ] **Recipe browser** - Browse preset salad recipes
- [ ] **Custom builder** - Select ingredients for custom salad
- [ ] **Order status display** - Show order progress to customer
- [ ] **Pickup notification** - Alert when salad is ready

### Event-Driven Automation (Gap Feature)
- [ ] **Order received** - Start assembly when order placed
- [ ] **Bowl dispensed** - Start assembly sequence when bowl ready
- [ ] **Low ingredient alert** - Alert staff when pan needs refill
- [ ] **Empty pan alert** - Stop accepting orders with that ingredient
- [ ] **Assembly complete** - Start handoff sequence

### Scheduled Tasks (Gap Feature)
- [ ] **Morning prep check** - Verify all ingredients stocked
- [ ] **Midday inventory** - Capture ingredient levels
- [ ] **End-of-day cleaning** - Cleaning sequence for grippers/workspace
- [ ] **Temperature logging** - Periodic prep station temp capture

### Data Pipeline (Gap Feature)
- [ ] **Portion image capture** - Photo each grab for training
- [ ] **Grab success tracking** - Record successful vs failed grabs
- [ ] **Train portion model** - ML model for consistent portions
- [ ] **Ingredient usage analytics** - Track popular ingredients

---

## Stretch Goals

- [ ] Salad tossing with coordinated arm motion
- [ ] Voice ordering ("I'd like a Caesar salad")
- [ ] Dietary restriction filtering (vegan, gluten-free options)
- [ ] Calorie/nutrition calculation display
- [ ] Integration with Inventory Tracker for ingredient management
- [ ] Multiple prep stations (salad bar fleet)

---

## Links

- **Jira Epic:** [TBD]
- **GitHub Repo:** [TBD]
- **Viam Organization:** [TBD]
- **Hardware BOM:** [TBD]

---

## Technical Details

### Hardware Specifications

**UFACTORY 850 Arms:**
- Payload: 5 kg
- Reach: 850 mm
- Repeatability: ±0.02 mm
- Degrees of freedom: 6
- Supports: ROS2, Python, C++, Viam SDK

**Avantco CPT-60-HC Prep Station:**
- Dimensions: 59" W x 15.5" D x 17.125" H
- Capacity: 6x 1/3 pans (6" deep) or 12x 1/6 pans
- Temperature: 33-40°F
- Power: 115V, 1.3A

### Workspace Layout

```
                    [Overview Camera]
                          │
    ┌─────────────────────┴─────────────────────┐
    │                                           │
    │   [Arm 1]                     [Arm 2]     │
    │      │                           │        │
    │      ▼                           ▼        │
    │  ┌───────────────────────────────────┐    │
    │  │     Avantco CPT-60 Prep Rail      │    │
    │  │  [Pan][Pan][Pan][Pan][Pan][Pan]   │    │
    │  └───────────────────────────────────┘    │
    │                                           │
    │        [Bowl]        [Handoff Station]    │
    │          │                   │            │
    │    [Dispenser]         [To Customer]      │
    │                                           │
    └───────────────────────────────────────────┘
                          │
                  [Dressing Station]
                  (self-serve bottles)
```

### Ingredient Pan Layout (Example)

| Pan Position | Size | Ingredient | Category |
|--------------|------|------------|----------|
| 1 | 1/3 | Mixed greens | Base |
| 2 | 1/3 | Romaine | Base |
| 3 | 1/3 | Cherry tomatoes | Topping |
| 4 | 1/3 | Cucumber | Topping |
| 5 | 1/3 | Shredded carrots | Topping |
| 6 | 1/3 | Croutons | Topping |

Or with 1/6 pans for more variety:

| Pans 1-2 | Pans 3-4 | Pans 5-6 | Pans 7-8 | Pans 9-10 | Pans 11-12 |
|----------|----------|----------|----------|-----------|------------|
| Greens | Tomatoes | Cucumber | Carrots | Cheese | Protein |

### Preset Recipe Examples

| Recipe | Ingredients |
|--------|-------------|
| Garden Salad | Mixed greens, tomatoes, cucumber, carrots |
| Caesar | Romaine, croutons, parmesan, (dressing self-serve) |
| Greek | Mixed greens, tomatoes, cucumber, feta, olives |
| Chef's | Romaine, tomatoes, egg, ham, cheese |

### Dual-Arm Coordination Patterns

**Pattern 1: Parallel Grab**
```
Arm 1: Grab ingredient A from pan 1
Arm 2: Grab ingredient B from pan 4  (simultaneously)
Arm 1: Place in bowl
Arm 2: Place in bowl
```

**Pattern 2: Hold and Add**
```
Arm 1: Grab bowl from dispenser
Arm 2: Grab ingredient, place in bowl (Arm 1 holds steady)
Arm 2: Grab next ingredient, place in bowl
...
Arm 1: Move bowl to handoff station
```

**Pattern 3: Assembly Line**
```
Arm 1: Handles all ingredients from pans 1-3
Arm 2: Handles all ingredients from pans 4-6
Bowl moves between arms or stays in shared workspace
```

---

## Notes

**Gap Features This Project Addresses:**
- **Customer Delivery** - Ordering kiosk/app, order status, pickup notification
- **Event-Driven Automation** - Order received, bowl ready, low ingredient alerts
- **Scheduled Tasks** - Morning prep check, cleaning cycles
- **Data Pipeline** - Portion images, grab success tracking, ML training
- **Multi-machine** - Dual-arm coordination as multi-machine pattern

**Why dual arms:**
- Faster assembly with parallel operations
- One arm can stabilize bowl while other adds ingredients
- Demonstrates advanced multi-machine coordination
- More visually impressive for demos
- Pathway to more complex bimanual tasks

**Gripper considerations:**
- Tongs work well for leafy greens and chunky items
- May need scoop attachment for small items (croutons, nuts)
- Consider food-safe materials (stainless steel, silicone)
- Washable/removable for cleaning

**Food safety notes:**
- Prep station maintains 33-40°F
- Grippers should be food-safe and cleanable
- Consider sneeze guard modifications for robot access
- Staff should handle ingredient restocking

**References:**
- [UFACTORY 850 Specs](https://www.ufactory.us/product/850)
- [Avantco CPT-60-HC Product Page](https://www.webstaurantstore.com/avantco-59-cpt-60-hc-countertop-refrigerated-prep-rail-with-sneeze-guard/360CPT60GLS.html)
