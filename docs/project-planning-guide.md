# Project Planning Guide

This guide captures the strategic thinking behind Build on Viam project selection and design. Use it when proposing new projects or evaluating how well our portfolio demonstrates Viam's capabilities.

## Goals

Build on Viam projects should collectively:

1. **Demonstrate all major Viam capabilities** - Every significant platform feature should be showcased by at least one project
2. **Provide reference implementations** - Projects serve as examples for customers and internal teams
3. **Exercise the full lifecycle** - From prototype to fleet deployment and maintenance
4. **Be compelling demos** - Visitors, customers, and executives should be impressed

## Viam Platform Capabilities

These are the capabilities we want to demonstrate across our project portfolio:

### Core Capabilities (must be covered)

| Capability | Description |
|------------|-------------|
| **Hardware Integration** | Consistent APIs across cameras, arms, motors, sensors |
| **Motion Planning** | Arm movement, obstacle avoidance, frame system |
| **Vision / ML Inference** | Object detection, classification, custom models |
| **Data Capture & Sync** | Edge-to-cloud data pipelines with offline resilience |
| **Remote Operation** | Control and monitor robots through firewalls |
| **Module Development** | Custom components and services via Registry |

### Scale & Fleet Capabilities

| Capability | Description |
|------------|-------------|
| **Fragments** | Reusable configuration blocks for fleet management |
| **Fleet Management** | Managing multiple machines with shared configs |
| **OTA Updates** | Deploying module and model updates to fleet |
| **Provisioning** | Automatic setup of new machines |

### Operational Capabilities

| Capability | Description |
|------------|-------------|
| **Event-Driven Automation** | Event-driven automation (sensor thresholds, detections) |
| **Scheduled Tasks** | Periodic operations without custom schedulers |
| **Monitoring & Alerting** | Fleet health visibility and notifications |
| **Data Pipeline (ML Training)** | Capture → Label → Train → Deploy workflow |

### Customer-Facing Capabilities

| Capability | Description |
|------------|-------------|
| **Customer Delivery** | White-label auth, TypeScript/Flutter SDKs, billing |
| **Web/Mobile Apps** | Customer-facing interfaces using Viam SDKs |

## Current Feature Coverage

As of the current project portfolio, here's how capabilities are covered:

**Projects:** Chess, Vino, Salad Maker, Greenhouse, Barista, Inventory Tracker, Retro Roomba, Smart Lighting

| Capability | Projects |
|------------|----------|
| Hardware Integration | All projects |
| Motion Planning | Chess, Vino, Salad Maker, Barista |
| Vision / ML Inference | Chess, Vino, Salad Maker, Barista, Inventory Tracker, Greenhouse |
| Data Capture & Sync | All projects |
| Remote Operation | All projects |
| Module Development | Chess, Vino, Salad Maker, Barista, Inventory Tracker, Retro Roomba, Smart Lighting |
| Fragments | All projects |
| Fleet Management | Vino, Greenhouse, Barista, Inventory Tracker, Smart Lighting |
| OTA Updates | Retro Roomba |
| Provisioning | — |
| Event-Driven Automation | All projects |
| Scheduled Tasks | Vino, Salad Maker, Greenhouse, Barista, Inventory Tracker, Smart Lighting |
| Monitoring & Alerting | Vino, Greenhouse, Barista |
| Data Pipeline (ML Training) | Vino, Salad Maker, Greenhouse, Barista, Inventory Tracker |
| Customer Delivery | Vino, Salad Maker, Barista, Inventory Tracker |
| Web/Mobile Apps | Vino, Salad Maker, Barista, Inventory Tracker |


## Proposing New Projects

When proposing a new project, consider:

### 1. Feature Coverage

- Does this project demonstrate capabilities not well-covered elsewhere?
- Which "gap features" could this project address?
- Would this be the PRIMARY demo for any capability?

### 2. Natural Fit

- Do the gap features fit naturally, or are they forced?
- Example: Fleet management fits Greenhouse naturally (multiple sensor stations) but not Chess (single board)
- Example: Customer delivery fits Vino naturally

### 3. Demo Appeal

- Is this compelling to watch?
- Would visitors/customers be impressed?
- Does it have a clear "wow" moment?

### 4. Feasibility

- What are the hardware needs?
- What is the MVP for the hackathon?
- Is the MVP achievable in hackathon timeframe?

### 5. Lifecycle Coverage

- Does this project exercise multiple lifecycle stages?
- Prototype → Deploy → Scale → Fleet → Maintain
- Greenhouse scores highly because it naturally progresses through all stages

### 6. Maintenance

- Can this project be maintained long-term?
- Is the hardware reliable?
- Will someone own it after the hackathon?

If you have a project you'd like to propose, write it up following the template used by the projects already defined and submit as a pull request.
