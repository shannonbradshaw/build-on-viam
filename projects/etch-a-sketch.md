# Project: [Project Name]

## Overview

**One-line description:** [Brief description of what this robot/system does]
Take a photo and have a machine draw it on an Etch-a-Sketch

**Project Lead:** TBD
**Team Members:** TBD
**Status:** Proposed

## Description

[2-3 paragraphs describing the project, its purpose, and why it's a good demonstration of Viam's capabilities. Include:]

A fun, artsy, interactive demo where people can walk up to the machine (which has a camera), take a photo of themselves, and have the machine trace them on an Etch-a-Sketch. This would be a fun demo to have in a showcase somewhere (similar to the Claw Machine or Chess) for users to play with -- an ephemeral robotic photobooth.

The first version would include a web app for users to interact with the machine, a camera to take the photo, vision service/ML model to extract only the humans from the image, edge detect and convert that photo to a tracing, and then motors to manipulate the Etch-a-Sketch. A future version could use 2 arms and motion planning to manipulate the dials on the Etch-a-Sketch.

## Viam Capabilities Demonstrated

### Core Capabilities
- [x] **Hardware Integration** — Camera to take the image, Motors to manipulate the Etch-a-Sketch
- [ ] **Motion Planning** — n/a
- [x] **Vision / ML Inference** — Human detection, edge detection and converting the image to a line trace
- [ ] **Data Capture & Sync** — Not primary focus
- [ ] **Remote Operation** — Not primary focus
- [x] **Module Development** — New modular service for actually turning the trace into an Etch-a-Sketch drawing
- [x] **Fragments** — The two motors for manipulating an Etch-a-Sketch will have similar configs, but with overrides for axis

### Scale & Fleet Capabilities
- [ ] **Fleet Management** — n/a
- [x] **OTA Updates** — Updating module and fragments
- [ ] **Provisioning** — n/a

### Operational Capabilities
- [ ] **Scheduled Tasks** — n/a
- [ ] **Monitoring & Alerting** — n/a
- [x] **Data Pipeline (ML Training)** — Potentially to train an edge-detection model (one likely already exists so this is probably not needed)

### Customer-Facing Capabilities
- [ ] **Customer Delivery** — n/a
- [x] **Web/Mobile Apps** — App for users to view and take their picture to be sketched

## Hardware Requirements

| Component | Description | Options |
|-----------|-------------|---------|
| Motor x2 | Manipulate the Etch-a-Sketch dials | non-stepper |
| Camera | Take picture of users | any general camera |
| Compute | Main controller | Raspberry Pi 5, etc. |

**Remote-Friendly:** Yes - Vision and ML models can be created remotely

---

## MVP Options

Select one for hackathon scope:

### Option A: Sketchy Motors (Recommended)
Use 2 motors to sketch
- **Scope:** Users use a web app to take a photo, the vision service extract the humans and turns them into a trace, and finally use motors to draw
- **Complexity:** Medium
- **Demo Appeal:** High

### Option B: Sketchy Arms
Use 2 arms to sketch
- **Scope:** All of the above, but instead of using motors to manipulate the Etch-a-Sketch, you use 2 arms and motion planning
- **Complexity:** High
- **Demo Appeal:** Very High

### Option C: Humans-Schumans
Rise of the machines
- **Scope:** Same as above, but no human detection -- simply draw the entire image as is
- **Complexity:** Low
- **Demo Appeal:** High

**Selected MVP:** Sketchy Motors

---

## Backlog

### Core Functionality
- [ ] Add camera to machine
- [ ] Create web app to show image preview and capture image
- [ ] Create Vision Service/ML Models to do human and edge detecting
- [ ] Feed captured image to Vision Service
- [ ] Create algorithm to draw convert image tracing to coordinate movements
- [ ] Feed algorithm to motors to actually sketch the image

### Sketchy Arms
- [ ] Use motion planning to move end-effector properly to sketch image
- [ ] Add "Shake to clear" functionality

---

## Stretch Goals

- [ ] Show sketch preview to user with the web app

---

## Links

- **Jira Epic:** [TBD]
- **GitHub Repo:** [TBD]
- **Viam Organization:** [TBD]
- **Hardware BOM:** [TBD]

---

## Technical Details

[Include any technical details that help understand the implementation approach, architecture diagrams, protocol specifications, etc.]

---

## Notes

[Additional context, considerations, or explanations that help evaluators understand the proposal]

**Why this project is compelling:**
- [Reason 1]
- [Reason 2]

**Risk Factors:**
- [Potential challenge 1]
- [Potential challenge 2]
