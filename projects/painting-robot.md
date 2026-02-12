# Project: Painting Robot

## Overview

**One-line description:** A robotic arm that creates paintings on canvas by translating digital images or user-drawn sketches into physical brushstrokes.

**Project Lead:** Khari
**Team Members:** Khari, Robin
**Status:** Proposed

## Description

The Painting Robot uses a robotic arm equipped with a brush to paint on a physical canvas. Users could submit an image or simple sketch and the robot would make a painting out of it. We are considering approaches for brush-path planning, paint color selection, and stroke execution to build up artwork layer by layer. For the Hackathon, painting may actually be drawing.
 
This project is compelling because it produces a tangible, visually striking output that is immediately understandable to any audience — everyone can appreciate watching a robot create art. It could exercise Viam's motion planning, vision, data pipeline, and remote operation capabilities in a tightly integrated way. It also has potential as a strong live demo: attendees could request a painting and watch the robot work in real time.

The Painting Robot could showcase several advanced Viam capabilities working together. We are considering using motion planning to translate brush paths into smooth arm trajectories, and vision/ML to detect and locate the canvas, brushes, and paint colors in the workspace. Data capture could log each painting session for replay, analysis, and iterative improvement. We are also exploring the idea of a web app that would allow remote users to submit artwork requests and watch a livestream of the robot painting.

Additionally, the Painting Robot allows for growth in the Viam platform. Currently, we have no framework for reinforcement learning, a large and growing field in robotics that is generating a lot of excitement. After "hacking" together a quick project, we are considering extending the robot into a larger, quarter-long project exploring how sensor fusion and reinforcement learning could be incorporated into Viam.

## Viam Capabilities Demonstrated

### Core Capabilities
- [x] **Hardware Integration** — Robotic arm (e.g., xArm or similar), mounted camera for canvas inspection; we may also explore a servo or linear actuator for brush pressure control and an optional color-mixing pump system.
- [x] **Motion Planning** — We are considering converting vector brush paths into smooth, collision-free arm trajectories with controlled speed and pressure along the canvas surface.
- [x] **Vision / ML Inference** — We plan to explore using vision to detect and locate the canvas, brushes, and paint colors in the workspace so the robot can orient itself, select the correct brush, and identify which paint to use.
- [x] **Data Capture & Sync** — Data capture to consider visual and arm inputs simultaneously (optional for now, may become more necessary if we pursue reinforcement learning)
- [ ] **Module Development** — We may develop modules for brushing and/or vision and planning.
- [ ] **Fragments** — Configuration fragment for the arm + camera + brush setup could allow easy replication.

### Scale & Fleet Capabilities
- [ ] **Fleet Management** — Not applicable for MVP; future option to run multiple painting stations in parallel.
- [x] **OTA Updates** — Could be used to update brush-path planning algorithms and ML models via the Registry.
- [ ] **Provisioning** — Not applicable for MVP.

### Operational Capabilities
- [ ] **Scheduled Tasks** — We could explore a queue system for painting jobs or scheduled demonstration paintings.
- [ ] **Monitoring & Alerting** — Could potentially alert on arm faults, paint supply levels, or stalled painting jobs.
- [ ] **Data Pipeline (ML Training)** — We are considering a capture → label → train → deploy workflow for improving stroke-planning or style-transfer models over time.

### Customer-Facing Capabilities
- [x] **Customer Delivery** — Attendees and remote users could submit painting requests and receive the finished artwork (physically or as a high-res photo).
- [x] **Web/Mobile Apps** — We are considering a web app for image upload, sketch drawing, job queue status, and possibly a live painting stream.

## Hardware Requirements

| Component | Description | Options |
|-----------|-------------|---------|
| Robotic Arm | 5-6 DOF arm for brush manipulation | xArm 6 or similar |
| Camera | 3d | intel realsense or similar |
| Brush Holder | End-effector to hold a paintbrush | Custom 3D-printed or gripper adapter |
| Canvas & Easel | Painting surface, fixed in arm workspace | Standard canvas on tabletop easel |
| Paint Supply | Acrylic or watercolor paints | Palette with 6-8 colors + water cup |
| Compute | Main controller | Raspberry Pi 5 or Jetson Orin Nano |


---

## MVP Options

Select one for hackathon scope:


### Option B: Multi-Color Draw
Given an image, the robot will detect the canvas, and draw upon it a simplified image (posterized to 3-4 colors), using the closest/appropriate color available.
- **Scope:** Everything in Option A plus color segmentation, paint dipping routine, multi-pass execution
- **Complexity:** High
- **Demo Appeal:** Very High

**Selected MVP:** _______________

Option B 
---

## Backlog

### Core Painting Functionality
- [ ] Image-to-vector path conversion (edge detection, contour extraction)
- [ ] Brush/marker-path optimization (minimize travel, avoid smearing)
- [ ] Arm calibration routine for canvas coordinate mapping
- [ ] Brush/marker pressure control for varying line thickness (w/ path optimization)
- [ ] Multi-color paint dipping and cleaning routine or multi-color marker selection

### Vision & Intelligence
- [ ] Camera-based canvas inspection (compare progress to target)
- [ ] Adaptive stroke correction based on visual feedback
- [ ] Text-to-image integration (eventually generate painting target from a prompt)


### Data & Analytics
- [ ] Time-lapse capture of each painting session
- [ ] Arm telemetry logging (joint positions, speeds)
- [ ] Painting quality scoring (target vs. result comparison)

---

## Stretch Goals

- [ ] Generative AI integration — paint entirely new artwork from text prompts
- [ ] Portrait mode — use a camera to photograph a person and paint their portrait
- [ ] Collaborative painting with multiple arms on a single large canvas
- [ ] Integration with other projects (e.g., Barista delivers coffee while you wait for your painting)
- [ ] Incorporate reinforcement learning

---

## Links

- **Jira Epic:** [TBD]
- **GitHub Repo:** [TBD]
- **Viam Organization:** [TBD]
- **Hardware BOM:** [TBD]

---

## Technical Details

**Architecture Overview (under consideration):**

1. **Input Processing** — A user would upload an image or enter a text prompt via a web app. The image could be preprocessed (e.g., edge detection, posterization, or style transfer) to produce a set of vector paths or fill regions.
2. **Path Planning** — Vector paths would be converted into ordered brush strokes, potentially optimized for minimal travel and paint usage. Each stroke would be a sequence of waypoints in canvas coordinates.
3. **Motion Execution** — Waypoints would be transformed into arm joint trajectories using Viam's motion planning service. We are considering various approaches for controlling stroke speed and z-axis pressure.
4. **Visual Feedback** — A camera could periodically capture the canvas state, compare it to the target, and potentially re-plan strokes to correct missed areas.

---

## Notes

[Additional context, considerations, or explanations that help evaluators understand the proposal]

**Why this project is compelling:**
- Could produce a physical, lasting artifact that people can take home — a robot-painted picture would be a memorable keepsake
- Visually captivating live demo potential — watching a robot paint is mesmerizing for any audience
- Has the potential to exercise a broad range of Viam capabilities in a single, cohesive system (motion planning, vision, ML, data, web apps)
- Naturally extensible from a simple MVP to increasingly sophisticated painting techniques as we explore new methods

**Risk Factors:**
- Paint is inherently messy — brush cleaning, dripping, and drying times may add real-world complexity
- Arm precision requirements could be high; small calibration errors may produce visible artifacts on canvas
- Multi-color workflows would significantly increase complexity (dipping, cleaning, drying between colors)
- Real paint behavior (blending, absorption, drying) may be hard to simulate and predict programmatically
