# Project: Etch-a-Sketch

## Overview

**One-line description:**
A machine to draw on an Etch-a-Sketch given user input (e.g. photo)

**Project Lead:** TBD
**Team Members:** TBD
**Status:** Proposed

## Description

A fun, artsy, interactive demo where people can walk up to the machine and provide input for it to draw on the Etch-a-Sketch. The first iteration will allow for users to select basic shapes (circles, stars, etc.). Future iterations will user-input drawings to be sketched, and further versions will include a camera that can be used to take an arbitrary image (including a photo of the user) and have the machine trace them on an Etch-a-Sketch. This would be a fun demo to have in a showcase somewhere (similar to the Claw Machine or Chess) for users to play with -- an ephemeral robotic photobooth.

The first version would include a web app for users to interact with the machine and a few basic shapes and motors to manipulate the Etch-a-Sketch knobs, as well as a mechanism for shake-to-erase. The version with a camera will include a vision service/ML model to extract only the human subjects from the image and convert that photo to a single-line tracing for the motors to sketch.

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

| Component | Description                        | Options              |
| --------- | ---------------------------------- | -------------------- |
| Motor x2  | Manipulate the Etch-a-Sketch dials | non-stepper          |
| Camera    | Take picture of users              | any general camera   |
| Compute   | Main controller                    | Raspberry Pi 5, etc. |

**Remote-Friendly:** Yes - Vision and ML models can be created remotely, and additional Etch-a-Sketch and motors are relatively inexpensive.

---

## MVP Options

Select one for hackathon scope:

### Option A: Basic

Use 2 motors to sketch a pre-defined shape

- **Scope:** Users use a web app to select a basic shape which the motors draw
- **Complexity:** Low
- **Demo Appeal:** Low

### Option B: Sketchy Motors (Recommended)

Use 2 motors and a touch-screen/mouse to sketch a user-input shape

- **Scope:** Users use a web app to make a continuous-line drawing, which the motors draw
- **Complexity:** Medium
- **Demo Appeal:** Medium

### Option C: Photo-Booth

Use a camera to take a photo of the user(s) and sketch an image of them

- **Scope:** Users use a web app to take a photo of themselves, which gets fed into a vision service/ML model to extract the subjects and turn them into a line drawing, which is then sketched.
- **Complexity:** High
- **Demo Appeal:** Very High

**Selected MVP:** Option B: Sketchy Motors

---

## Backlog

### Core Functionality

- [ ] Create an algorithm to draw basic shapes
  - [ ] straight line
  - [ ] anti-aliased diagonal line
  - [ ] star
  - [ ] circle
- [ ] Create web app to have users draw a shape
- [ ] Feed algorithm to motors to actually sketch the user-generated shape
- [ ] Implement shake-to-clear

### Further Iterations

- [ ] Add a camera to the machine
- [ ] Add person-extraction ML model
- [ ] Convert person to line drawing ([see academic example](https://www.math.uwaterloo.ca/tsp/data/art/index.html))
- [ ] Display line drawing to user on webapp and await confirmation

---

## Stretch Goals

- [ ] Real-time following of the user's drawing
- [ ] Pressure-sensitive drawings (harder pressure equates to line thickness)

---

## Links

- **Jira Epic:** [TBD]
- **GitHub Repo:** [TBD]
- **Viam Organization:** [TBD]
- **Hardware BOM:** [TBD]

---

## Technical Details

[Include any technical details that help understand the implementation approach, architecture diagrams, protocol specifications, etc.]

### Hardware

Basic hardware requirements -- a large Etch-a-Sketch, two motors to manipulate the knobs, a sufficiently-powerful computer for vision, a camera, and an external display capable of touch input.

### Image-conversion algorithm

Various academic papers exist outlining algorithms that we could implement. An example is [here](https://www.math.uwaterloo.ca/tsp/data/art/index.html). Considerations include minimum distance between lines, since that is determined by the Etch-a-Sketch itself.

---

## Notes

**Why this project is compelling:**

- Really impressive demo (see [examples](https://princessetch.com/gallery/))
- Can be iterated on from basic to complex
- Setup is very easy, so this demo can travel well to events
- User-interaction with the machine provides a certain "wow" factor
- Everything except the core algorithm can be solved by Viam, so it's a good use of a lot of platform features.
- Can be expanded to other forms of line-tracing
  - Spray painting
  - Actual painting
