# Project: Automated Storage and Retrieval System

## Overview

**One-line description:** Modular lab storage system that retrieves and returns bins on demand via a 3-axis gantry, with RFID identification and a searchable inventory.

**Project Lead:** Petr Novikov
**Team Members:** TBD
**Status:** Proposed

## Description

Automated Storage and Retrieval System is a modular lab storage solution that works like a reversible vending machine. Users select an item on a screen (e.g., M4 nuts), and the machine delivers the bin containing that item. When done, they place the bin in a return slot and the machine puts it back in its assigned position. Bins are identified by RFID tags; a 3-axis gantry with a gripper handles all pick-and-place without additional actuators. The machine maintains an internal state of bin positions and can reindex via RFID if bins are ever reshuffled.

The system addresses real pain for lab managers—who today manually maintain inventory and reorder—and for lab users—who often don’t know if an item exists, where it is, or who has it. It keeps an automatic digital twin of inventory, a searchable database with up-to-date bin status (stored vs. in use), content snapshots on each return, and optional tracking of who retrieved which bin. That combination of physical automation and data visibility makes it compelling both as a utility and as a demo.

This project showcases Viam’s hardware integration (gantry, gripper, RFID), motion planning for reliable bin handling, data capture and sync for inventory and status, and remote operation for development and monitoring. Optional extensions (bulk return, vision-based quantity or content validation) would further exercise vision and ML pipelines.

## Viam Capabilities Demonstrated

### Core Capabilities

- [ ] **Hardware Integration** — [Describe hardware: cameras, arms, sensors, etc.]
- [ ] **Motion Planning** — [Describe if applicable, or "Not applicable"]
- [ ] **Vision / ML Inference** — [Describe vision/ML usage, or "Not applicable"]
- [ ] **Data Capture & Sync** — [Describe data capture needs, or "Not primary focus"]
- [ ] **Remote Operation** — [Describe remote operation capabilities]
- [ ] **Module Development** — [Describe custom modules, or "Not primary focus"]
- [ ] **Fragments** — [Describe fragment usage for configuration reuse]

### Scale & Fleet Capabilities

- [ ] **Fleet Management** — [Describe if managing multiple machines, or "Not applicable"]
- [ ] **OTA Updates** — [Module and configuration updates via Registry]
- [ ] **Provisioning** — [Fragment-based configuration reuse, or "Not applicable" if not fleet-oriented]

### Operational Capabilities

- [ ] **Scheduled Tasks** — [Describe scheduled operations, or "Not applicable"]
- [ ] **Monitoring & Alerting** — [Describe monitoring needs, or "Not applicable"]
- [ ] **Data Pipeline (ML Training)** — [Describe capture → label → train → deploy workflow, or "Not applicable"]

### Customer-Facing Capabilities

- [ ] **Customer Delivery** — [Describe guest/customer-facing features, or "Not applicable"]
- [ ] **Web/Mobile Apps** — [Describe app interfaces, or "Not applicable"]

## Hardware Requirements

| Component       | Description       | Options                |
| --------------- | ----------------- | ---------------------- |
| [e.g., Arm]     | [Purpose]         | [Specific models]      |
| [e.g., Camera]  | [Purpose]         | [Specific models]      |
| [e.g., Compute] | [Main controller] | [Raspberry Pi 5, etc.] |

**Remote-Friendly:** [Yes/Partially/No] - [Explain what can be developed remotely]

---

## MVP Options

Select one for hackathon scope:

### Option A: [Name] (Recommended)

[Brief description of minimal viable demo]

- **Scope:** [What's included]
- **Complexity:** [Low/Medium/High]
- **Demo Appeal:** [Medium/High/Very High]

### Option B: [Name]

[Brief description]

- **Scope:** [What's included]
- **Complexity:** [Low/Medium/High]
- **Demo Appeal:** [Medium/High/Very High]

### Option C: [Name]

[Brief description]

- **Scope:** [What's included]
- **Complexity:** [Low/Medium/High]
- **Demo Appeal:** [Medium/High/Very High]

**Selected MVP:** **\*\***\_\_\_**\*\***

---

## Backlog

### [Category 1, e.g., Core Functionality]

- [ ] [Feature 1]
- [ ] [Feature 2]
- [ ] [Feature 3]

### [Category 2, e.g., Data & Analytics]

- [ ] [Feature 1]
- [ ] [Feature 2]

### [Category 3]

- [ ] [Feature 1]
- [ ] [Feature 2]

---

## Stretch Goals

- [ ] [Ambitious future capability 1]
- [ ] [Ambitious future capability 2]
- [ ] [Integration with other projects]

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
