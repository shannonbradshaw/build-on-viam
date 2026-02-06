# Project: Rod Hockey Robot

## Overview

**One-line description:** A robot controlled rod hockey game that plays against humans

**Project Lead:** Travis Gritter
**Team Members:** TBD
**Status:** Proposed

## Description

It's a robotic rod hockey game that uses motors, camera and motion planning to play rod hockey (the hockey version of foosball). The purpose is for users to play rod hockey against a robot and also demonstrate the Viam capabilities. It is a good demonstration of Viam capabilities because it uses a number of different built in components. For example, it uses cameras to see the puck.

**What does this robot/system do?**  
The robot plays rod hockey against human opponents using motorized player rigs controlled by computer vision and motion planning.

**Why is it compelling?**  
It combines demo appeal through interactive gameplay, utility as a showcase piece for office visitors, and learning value through its integration of multiple robotics concepts. The use of Islanders players (Viam sponsored) adds brand appeal.

**What Viam capabilities does it showcase?**  
The project demonstrates hardware integration, vision processing, motion planning, fleet management, and module development in a fun, interactive format.

## Viam Capabilities Demonstrated

### Core Capabilities

- [x] **Hardware Integration** — Cameras, Motors (stepper motors for player control)
- [x] **Motion Planning** — Uses Pygame - a Python game engine that plugs into the Viam SDK
- [x] **Vision / ML Inference** — Uses Viam's built in color and image detection
- [ ] **Data Capture & Sync** — Not primary focus
- [x] **Remote Operation** — Can be controlled remotely, but plan is for it to be automated
- [x] **Module Development** — Will create modules for players (e.g. movement distance, curve distance)
- [x] **Fragments** — Will use a fragment for players (e.g. stepper motors, player modules, etc.)

### Scale & Fleet Capabilities

- [x] **Fleet Management** — Yes there are 5 players plus goalie
- [x] **OTA Updates** — Yes can do this to test
- [x] **Provisioning** — Will have to provision raspberry Pis

### Operational Capabilities

- [ ] **Scheduled Tasks** — Not applicable
- [ ] **Monitoring & Alerting** — Not applicable
- [x] **Data Pipeline (ML Training)** — Can do ML on improving play, although I've found search with subproblems a better approach

### Customer-Facing Capabilities

- [x] **Customer Delivery** — Users can play when they come to the office, reuse modules/components to make their own games (e.g. foosball)
- [ ] **Web/Mobile Apps** — Not primary focus. Could make a simple app to control settings.

## Hardware Requirements

| Component        | Description                                                               | Options                                   |
| ---------------- | ------------------------------------------------------------------------- | ----------------------------------------- |
| Rod Hockey Board | Physical game board for rod hockey                                        | Standard rod hockey table                 |
| Camera           | Detect position of puck and players                                       | Built-in Camera components                |
| Compute          | Main controller for vision and motion planning                            | Raspberry Pi 4                            |
| Player Rigs      | Control player movement (stepper motors, cable system, mounting hardware) | Custom rigs with stepper motor components |

**Remote-Friendly:** Partially - Can work on motion planning remotely. But need to be at the board to test

---

## MVP Options

Select one for hackathon scope:

### Option A: Single Player (Already Done)

Create a single player that can score a puck

- **Scope:** A single rig (two stepper motors), camera & vision detection, motion planning
- **Complexity:** Medium - High
- **Demo Appeal:** High

### Option B: Two Players (In Progress)

Create two players that can pass to each other

- **Scope:** Two rigs, camera & vision detection, motion planning
- **Complexity:** Medium
- **Demo Appeal:** Medium

### Option C: 3-5 Players

Full game implementation with multiple players

- **Scope:** 3-5 rigs, camera, motion planning
- **Complexity:** High
- **Demo Appeal:** Very High

**Selected MVP:** **\*\***Option B**\*\***

---

## Backlog

### Core Functionality

- [ ] Player rig controllers (2 stepper motors, will customize length and curve)
- [ ] Camera with color detection
- [ ] Puck tracking and position detection
- [ ] Player position control and calibration

### Motion Planning

- [ ] Pygame motion planning integration
- [ ] Collision detection and avoidance
- [ ] Defensive positioning logic

### Integration & Testing

- [ ] Module development for player control
- [ ] Fragment configuration for multiple units
- [ ] End-to-end gameplay testing

---

## Stretch Goals

- [ ] Ability to react to defense
- [ ] Control a goalie
- [ ] Play type selection (defensive, aggressive, etc.)

---

## Links

- **Jira Epic:** [TBD]
- **GitHub Repo:**
  https://github.com/tgritter/rod-hockey-robot
- **Viam Organization:** [TBD]
- **Hardware BOM:**
  https://drive.google.com/file/d/1NEblp5ecSdEtv-9z2P_65eEUC6_Ns1IS/view?usp=sharing

---

## Technical Details

**Hardware Architecture:**

- Up to 5 player rigs, each consisting of 2 stepper motors with a cable/conveyor belt system for horizontal and rotational movement
- Camera positioned above the playing surface for puck and player tracking
- Raspberry Pi 4 as the main compute unit for vision processing and motion control

**Software Stack:**

- Pygame game engine integrated with Viam SDK for motion planning and game logic
- Viam's built-in color detection and image processing for puck tracking
- Custom modules for player movement control (distance, curve, speed)
- Fragment-based configuration for reusable player rig setup across multiple units

**Control Flow:**

1. Camera captures real-time position of puck and players
2. Vision system processes image and detects puck location using color detection
3. Motion planning algorithm calculates optimal player movements
4. Stepper motors execute coordinated movements to intercept and shoot puck

---

## Notes

**Why this project is compelling:**

- Uses a wide variety of Viam components
- It's a fun interactive game
- Features Islanders players (Viam sponsored)

**Risk Factors:**

- Being too slow to react to changes
- Handling noise (board or camera moves)

---

## Images

Board: https://drive.google.com/file/d/1Sp_Uv9UCN_rr33VJpFsHluUOX431l9E_/view?usp=drive_link

Rig: https://drive.google.com/file/d/1slypq6oUyvG1TR7LG_pJrvmxSbNH6Xn6/view?usp=sharing
