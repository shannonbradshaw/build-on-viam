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
| **Triggers** | Event-driven automation (sensor thresholds, detections) |
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

| Capability | Primary Project | Secondary |
|------------|-----------------|-----------|
| Hardware Integration | All projects | - |
| Motion Planning | Chess, Vino, Dishwasher | Box-bot, Barista |
| Vision / ML | Chess, Greenhouse | Box-bot, Cleaning Cart |
| Data Capture | Greenhouse | All projects |
| Remote Operation | All projects | - |
| Module Development | Chess | All projects |
| Fragments | Greenhouse | Barista |
| Fleet Management | **Greenhouse** | Cleaning Cart, Barista |
| Triggers | **Box-bot**, Greenhouse | Vino, Chess, Barista |
| Scheduled Tasks | **Cleaning Cart** | Greenhouse, Vino, Barista |
| Monitoring & Alerting | **Greenhouse** | Barista |
| Data Pipeline (ML) | **Chess**, Greenhouse | Box-bot, Dishwasher |
| Customer Delivery | **Vino**, **Barista** | - |

**Bold** = Primary responsibility for demonstrating this capability.

## Gap Analysis Methodology

When assessing feature coverage:

1. **List all Viam capabilities** from documentation (see `../docs-dev/understand/what-is-viam.md`)
2. **Map each capability to projects** that naturally exercise it
3. **Identify gaps** - capabilities with no project coverage
4. **Assign gaps to projects** where the capability fits naturally
5. **Consider new projects** if no existing project is a natural fit

### Questions to Ask

- Does this capability have at least one project demonstrating it well?
- Is the demonstration compelling (not just technically present)?
- Would a customer understand how to use this capability from our example?
- Is the project that owns this capability likely to be maintained?

## Configuration Architecture

All Build on Viam projects should follow the two-layer configuration pattern:

### Layer 1: Hardware/Intrinsics (Fragment)

The hardware fragment contains:
- Physical components (arm, gripper, camera, motors, sensors)
- Hardware driver modules
- Frame system and spatial transforms
- Motion service configuration
- Variables for machine-specific values (IP addresses, serial numbers)

**Characteristics:**
- Rarely changes once hardware is set up
- Owned by project lead or hardware team
- Versioned and tagged (stable, dev)
- Shared across machines with same physical setup

### Layer 2: Application (Machine Config + Local Development)

The application layer contains:
- Fragment reference with variables
- Fragment mods for machine-specific overrides
- Application services and modules
- UI components (StreamDeck, tablets)
- Helper components (pose savers, calibration tools)

**Characteristics:**
- Changes frequently during development
- Iterated locally via CLI during development
- Packaged as modules for production deployment
- Each developer can run their own version

### Why This Separation?

1. **Hardware is stable** - Once working, rarely changes
2. **Application iterates rapidly** - Logic changes constantly
3. **Local development is fast** - No deploy cycle during iteration
4. **Production is clean** - Package working code, deploy to machine

See [Team Development Guide](team-development-guide.md) for implementation details.

## Development Workflow Pattern

Projects should follow the CLI development pattern demonstrated by viam-chess:

```
┌─────────────────────────────────────────────────────────────────┐
│  ROBOT (viam-server with hardware fragment)                      │
│  - Arm, gripper, camera running                                  │
│  - Motion service available                                      │
└─────────────────────────────────────────────────────────────────┘
                              ▲
                              │ WebRTC connection
                              │
┌─────────────────────────────┴───────────────────────────────────┐
│  DEVELOPER LAPTOP                                                │
│  - CLI tool connects to remote machine                          │
│  - Gets hardware as dependencies                                 │
│  - Runs application logic locally                                │
│  - Iterates instantly (edit → build → run)                      │
└─────────────────────────────────────────────────────────────────┘
```

**Benefits:**
- No module packaging during development
- Instant iteration
- Multiple developers can share hardware
- Same code works as module in production

See [viam-chess](https://github.com/erh/viam-chess) for reference implementation.

## Proposing New Projects

When proposing a new project, consider:

### 1. Feature Coverage

- Does this project demonstrate capabilities not well-covered elsewhere?
- Which "gap features" could this project address?
- Would this be the PRIMARY demo for any capability?

### 2. Natural Fit

- Do the gap features fit naturally, or are they forced?
- Example: Fleet management fits Greenhouse naturally (multiple sensor stations) but not Chess (single board)
- Example: Customer delivery fits Vino naturally (guest-facing) but not Box-bot (internal utility)

### 3. Demo Appeal

- Is this compelling to watch?
- Would visitors/customers be impressed?
- Does it have a clear "wow" moment?

### 4. Feasibility

- Can this be built with available hardware?
- Is the MVP achievable in hackathon timeframe?
- Are the stretch goals realistic?

### 5. Lifecycle Coverage

- Does this project exercise multiple lifecycle stages?
- Prototype → Deploy → Scale → Fleet → Maintain
- Greenhouse scores highly because it naturally progresses through all stages

### 6. Maintenance

- Can this project be maintained long-term?
- Is the hardware reliable?
- Will someone own it after the hackathon?

## Feature Assignment Guidelines

When assigning gap features to projects:

### Triggers

Best fit for projects with:
- Clear event → action patterns
- Sensor inputs that can trigger automation
- State changes that should initiate behavior

Examples:
- Box-bot: Box detected → start flatten sequence
- Greenhouse: Humidity low → activate mister
- Vino: Glass placed → start pour

### Scheduled Tasks

Best fit for projects with:
- Regular maintenance needs
- Periodic data collection
- Time-based operations

Examples:
- Cleaning Cart: Morning/lunch/evening patrol routes
- Greenhouse: Daily sensor readings, weekly reports
- Barista: Morning warmup, end-of-day cleaning

### Data Pipeline (Capture → Train → Deploy)

Best fit for projects with:
- Vision/ML components that improve over time
- Natural ground truth for labeling
- Enough volume to generate training data

Examples:
- Chess: Game state IS the label (automatic ground truth)
- Greenhouse: Growth stages can be labeled over time
- Box-bot: Box types can be classified and labeled

### Customer Delivery

Best fit for projects with:
- Guest/visitor interaction
- Natural ordering or request flow
- Compelling customer-facing interface

Examples:
- Vino: Wine ordering for guests
- Barista: Coffee ordering for office
- NOT: Box-bot (internal utility, no customer interaction)

### Fleet Management

Best fit for projects with:
- Natural multi-instance deployment
- Identical or similar units
- Centralized management value

Examples:
- Greenhouse: Multiple sensor stations
- Barista: Multiple coffee stations
- Cleaning Cart: Multiple carts for large facility
- NOT: Chess (single board, no fleet benefit)

### Monitoring & Alerting

Best fit for projects with:
- Continuous operation
- Critical parameters to watch
- Remote oversight needs

Examples:
- Greenhouse: Temperature, humidity, soil moisture
- Barista: Bean level, water, temperature
- NOT: Chess (supervised play, no remote monitoring need)

## Project Portfolio Balance

The ideal portfolio has:

1. **At least one project per capability** - No gaps
2. **Diversity of robot types** - Arms, mobile bases, sensors
3. **Range of complexity** - Simple to complex
4. **Mix of use cases** - Office utility, entertainment, industrial
5. **Feasibility spread** - Some quick wins, some ambitious projects

### Current Portfolio Assessment

| Dimension | Assessment |
|-----------|------------|
| Arm manipulation | Well covered (Chess, Vino, Barista, Dishwasher, Box-bot) |
| Mobile navigation | Light (only Cleaning Cart) |
| Vision/ML | Well covered |
| Data/Fleet | Good (Greenhouse primary) |
| Customer-facing | Good (Vino, Barista) |
| Operational (triggers, scheduling) | Good (distributed across projects) |

### Potential Gaps for Future Projects

- **Mobile manipulation** - Combining navigation + arm (partially covered by Cleaning Cart stretch)
- **Outdoor/weather** - All current projects are indoor
- **Multi-robot coordination** - Robots working together (Cleaning Cart + Dishwasher handoff is stretch goal)
- **Voice interaction** - Listed as stretch for several projects, not primary for any

## Updating This Document

When the project portfolio changes:

1. Update the feature coverage table
2. Reassess gap assignments
3. Add new capabilities if Viam adds features
4. Archive completed/deprecated projects
5. Note any persistent gaps that need new projects
