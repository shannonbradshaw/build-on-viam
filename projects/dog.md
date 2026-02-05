Project: Robot Dog Follows Human

Overview

One-line description: Autonomous quadruped robot that uses computer vision to detect and follow a designated human operator

Project Lead: John Nicholson & Miko Franczak
Team Members: 
Status: Proposed

## Description

This project demonstrates an autonomous human following base/rover service that uses computer vision and motion control to follow a human operator through various environments. The service maintains a safe following distance, adjusts its speed to match the human's pace, and navigates around obstacles while keeping the target person in view. In this particular project, the base/rover service is implemented on a robot dog, a Unitree G02.

The demo is compelling because it showcases a natural, intuitive human-robot interaction that's immediately understandable to any audience. Unlike stationary demos or pre-programmed routines, a robot dog following someone around creates an engaging, dynamic experience that highlights real-time decision-making and adaptive behavior. It has strong visual appeal for trade shows, customer demos, and social media content.

This project showcases Viam's end-to-end robotics platform capabilities: hardware integration with commercial robot platforms (Unitree SDK), real-time vision processing and ML inference for person detection/tracking, motion planning for dynamic following behavior, data capture for improving model performance, and remote monitoring/control. It demonstrates how Viam can rapidly prototype sophisticated behaviors on complex hardware platforms.

## Viam Capabilities Demonstrated

### Core Capabilities
- [x] **Hardware Integration** — Integration with Unitree G02 quadruped via SDK, onboard cameras (front-facing wide-angle), IMU for orientation sensing
	- some work has already been done [here](https://github.com/viam-modules/unitree) 
- [x] **Motion Planning** — Dynamic velocity planning to maintain following distance (1.5-3m), adaptive speed control matching human walking speed (0-1.5 m/s), basic obstacle avoidance using depth sensing
- [x] **Vision / ML Inference** — Person detection and tracking using YOLOv8 or MobileNet SSD models, depth estimation for distance calculation, continuous person re-identification to handle occlusions
- [x] **Data Capture & Sync** — Capture camera frames, detection bounding boxes, tracking metrics, and movement telemetry for model refinement and behavior analysis
- [x] **Remote Operation** — Live video feed with detection overlays, real-time telemetry dashboard, emergency stop capability, and ability to switch between autonomous and manual control modes
- [x] **Module Development** — Custom Unitree control module for Viam integration, person tracking service module with Kalman filtering for smooth tracking

### Scale & Fleet Capabilities
- [x] **Fleet Management** — wrap the planner in a fragment to switch between different rovers easily
- [x] **OTA Updates** — Model updates for improved person detection, configuration tuning for following behavior parameters, module updates for Unitree integration
- [ ] **Provisioning** — Not primary focus for single-robot demo, but configuration could be templated for future fleet deployment

### Operational Capabilities
- [ ] **Scheduled Tasks** — Not applicable (continuous real-time operation)
- [x] **Monitoring & Alerting** — Battery level monitoring with low-battery alerts, tracking confidence monitoring with alerts when target is lost, collision detection alerts
- [x] **Data Pipeline (ML Training)** — Capture diverse following scenarios (indoor/outdoor, different lighting, various people) → Label challenging detection cases → Fine-tune detection model → Deploy improved model via OTA

### Customer-Facing Capabilities
- [x] **Customer Delivery** — Public-facing demo suitable for trade shows and customer visits; spectator-safe with configurable safety zones
- [x] **Web/Mobile Apps** — Web dashboard showing live camera feed with detection overlays, robot status, telemetry, and emergency controls; mobile app for monitoring and basic control

## Hardware Requirements

| Component | Description | Options |
|-----------|-------------|---------|
| Unitree G02 | Quadruped robot platform | Unitree G02 (includes onboard cameras, IMU, compute) |
| Camera | Front-facing person detection | Built-in Unitree cameras, or optional USB wide-angle camera for improved FOV |
| Compute | Main controller and ML inference | Unitree onboard computer (sufficient for initial demo), or Raspberry Pi 5 / NVIDIA Jetson Orin Nano for enhanced performance |
| Depth Sensor | Distance measurement (optional) | RealSense D435i or use stereo vision from dual cameras |
| Battery | Runtime extension (optional) | Extended battery pack for >45min runtime |

**Remote-Friendly:** Partially - Core vision and tracking algorithms can be developed and tested with recorded datasets or simulator. Unitree SDK integration and motion control tuning require hardware access. 

---

## MVP Options

Select one for hackathon scope:

### Option A: Basic Visual Following (Recommended)
Simple person detection and following in controlled indoor environment
- **Scope:** Detect single person using pre-trained model, maintain 2m following distance, basic forward/backward/turning motion, stop when person stops
- **Complexity:** Medium
- **Demo Appeal:** High - immediately impressive and easy to demonstrate

### Option B: Interactive Following with Gestures
Following behavior with basic gesture recognition for commands
- **Scope:** Option A + recognize stop/go/follow hand gestures, respond to wave for attention, acknowledge commands with robot motion (head nod, sit)
- **Complexity:** High
- **Demo Appeal:** Very High - strong audience interaction element

**Selected MVP:** Option A (Basic Visual Following)

---

## Backlog

### Tracking Service
- [ ] Develop following behavior state machine (searching, tracking, following, stopped)
- [ ] Implement distance estimation and velocity control

### Vision & ML
- [ ] Collect training data for person re-identification
- [ ] Fine-tune detection model for varying lighting
- [ ] Implement tracking smoothing
- [ ] Add multi-person detection with designated target selection
- [ ] Develop person re-identification for occlusion recovery
- [ ] Add gesture detection which would allow the dog to heel, spin, roll, stand on hind legs, do a backflip
- [ ] Implement person detection pipeline with YOLOv8
- [ ] Natural language command integration ("Heel", "Stay", "Come")

### User Interface
- [ ] Build web dashboard with live video feed
- [ ] Add telemetry visualization (speed, distance, battery)
- [ ] Implement emergency stop button
- [ ] Add manual override control mode
- [ ] Change following distance
- [ ] Speed with which robot moves
- [ ] Add follow state indicator (SEARCHING / TRACKING / FOLLOWING / LOST)

### Data & Analytics
- [ ] Set up automated data capture during operation
- [ ] Create annotation pipeline for detection refinement
- [ ] Implement A/B testing for control parameters

### Hardware

- [ ] Integrate Unitree SDK with Viam movement-sensor component
- [ ] Integrate Unitree SDK with Viam audio component
- [ ] Integrate Unitree SDK with Viam pointclouds

### Naivgation
- [ ] Add basic obstacle avoidance using front sensors
- [ ] Build a map of the office
- [ ] Allow robot to navigate from or between april tags
- [ ] Autonomous return-to-base when battery is low
- [ ] Social navigation behaviors (navigate through crowds without disturbing people)
- [ ] Integration with office automation projects (follow person while carrying items)
- [ ] Try to add in jump over small obstacle feature

## Stretch Goals
- [ ] Research other bases like humanoid or drone
- [ ] Perform SLAM and monitor base position on map/GUI
- [ ] Mobile App

---

## Links

- **Jira Epic:** [TBD]
- **GitHub Repo:** [TBD]
- **Viam Organization:** [TBD]
- **Hardware BOM:** [TBD - Unitree G02 unit, optional accessories]
- **Unitree Documentation:** https://www.unitree.com/g02

---

## Technical Details

**Architecture:**
```
┌─────────────────┐
│  Camera Feed    │
└────────┬────────┘
         │
    ┌────▼──────┐
    │  camera denoise │  
    │  			 │
    └────┬──────┘
         │
    ┌────▼──────┐
    │  Person   │
    │ Detection │  (YOLOv8 / MobileNet)
    └────┬──────┘
         │
    ┌────▼──────┐
    │  Tracking │  
    │  Service  │
    └────┬──────┘
         │
    ┌────▼──────────┐
    │   Following   │  (State Machine)
    │  Controller   │
    └────┬──────────┘
         │
    ┌────▼──────────┐
    │    Unitree    │
    │    Base     │
    │   Component   │
    └───────────────┘
```

**Control Algorithm:**
- Detection confidence threshold: >0.6
- Target following distance: 2.0m (±0.5m tolerance)
- Max following speed: 1.2 m/s
- Angular correction: Proportional to target offset from center
- Update rate: 10 Hz for vision, 50 Hz for motion control

**Safety Features:**
- Minimum obstacle distance: 0.5m
- Emergency stop via remote command
- Automatic stop if target lost for >3 seconds
- Battery monitoring with automatic slowdown at <20%
- Collision detection via IMU monitoring

---

## Notes

**Why this project is compelling:**
- High "wow factor" - people immediately connect with robot dog behavior
- Demonstrates sophisticated real-time AI + robotics integration
- Highly visual and social-media friendly (great for marketing content)
- Scalable from demo to practical applications (security patrol, warehouse following, luggage transport)
- Platform for showcasing multiple Viam capabilities in one cohesive demo

**Risk Factors:**

- Person detection robustness in varying lighting conditions - can use pre-trained models initially and refine later
- Indoor/outdoor transitions may require lighting adaptation - scope to indoor-only for MVP
- Battery runtime (~30-45 min) requires planning for demo duration - can have charging schedule between demos
- Crowded environments may confuse tracking - start with controlled environments, expand gradually

**Dependencies:**
- Unitree G02 hardware availability and SDK access
- Compute resources for real-time ML inference (may need external compute if onboard is insufficient)
- Access to varied environments for testing and data collection

**Success Metrics:**
- Successfully follow designated person for >5 minutes without losing track
- Maintain target distance within ±30cm
- Handle 90% of common occlusions (person turns corner, walks behind obstacle)
- Operate safely with no collisions during demo runs

