# Project: Greenhouse

## Overview

**One-line description:** Automated growing environment with sensing, environmental control, and growth tracking

**Project Lead:** TBD
**Team Members:** TBD
**Status:** New

## Description

Greenhouse is an automated plant growing system that monitors environmental conditions (temperature, humidity, soil moisture, light), controls actuators (pumps, lights, fans), and tracks plant growth over time. The system demonstrates Viam's data capture, cloud sync, remote monitoring, and ML capabilities.

This project naturally exercises the full robotics lifecycle - from prototype through fleet deployment - as it can scale from a single plant pod to multiple grow stations with centralized monitoring.

## Viam Capabilities Demonstrated

- [ ] Motion / Arm Control (stretch: harvesting)
- [ ] Vision / ML (ripeness detection)
- [x] Data Management
- [x] Fleet Management (multi-station) ← **Primary fleet demo**
- [x] Remote Operation
- [ ] Modular Resources
- [x] Multi-machine Coordination ← **Multiple sensor stations**
- [x] Cloud Integration
- [x] Triggers ← **Threshold-based automation**
- [x] Fragments (environment recipes)
- [x] Monitoring/Alerting ← **Environmental alerts**
- [x] Data Pipeline ← **Capture → Train → Deploy cycle**
- [x] Scheduled Tasks ← **Periodic readings, daily reports**

## Hardware Requirements

| Component | Description | Options |
|-----------|-------------|---------|
| Sensors | Environmental monitoring | DHT22 (temp/humidity), soil moisture, light sensor, pH |
| Actuators | Environment control | Relay-controlled pump, solenoid, grow lights, fans |
| Camera | Time-lapse & monitoring | USB camera, RPi camera |
| Compute | Main controller | Raspberry Pi 4, Jetson Nano (if ML) |
| Enclosure | Growing environment | IKEA cabinet, grow tent, custom build |
| Growing medium | Plant support | Soil pots, hydroponics, AeroGarden-style |

**Estimated Hardware Cost:** $200-500 (excluding enclosure)

**Remote-Friendly:** Yes - sensors can be monitored from anywhere, development can be fully remote

---

## MVP Options

Select one for hackathon scope:

### Option A: Monitor + Dashboard
Sensors track temp/humidity/soil moisture, display on web dashboard.
- **Complexity:** Low
- **Demo Appeal:** Medium
- **Scope:** Sensor integration, data capture, basic visualization

### Option B: Monitor + Auto-Water (Recommended)
Above plus automated watering based on soil moisture thresholds.
- **Complexity:** Low-Medium
- **Demo Appeal:** Medium-High
- **Scope:** Adds actuation, threshold logic, closed-loop control

### Option C: Monitor + Water + Lights
Full environment control including grow lights on schedule.
- **Complexity:** Medium
- **Demo Appeal:** High
- **Scope:** Multiple actuators, scheduling, light cycles

### Option D: Single Plant Pod
Small self-contained unit (like AeroGarden) with full monitoring.
- **Complexity:** Low-Medium
- **Demo Appeal:** High
- **Scope:** Compact, portable, good for demos

**Selected MVP:** _______________

---

## Backlog

Select 3-5 items for post-hackathon development:

### Environmental Control
- [ ] **Multi-zone control** - Different settings for different plant types
- [ ] **Recipe management** - Saved profiles for different crops (via fragments)
- [ ] **Climate scheduling** - Day/night cycles, seasonal adjustments
- [ ] **Fan/ventilation control** - Humidity and temperature regulation

### Vision & ML
- [ ] **Ripeness detection** - ML model detects when produce is ready to harvest
- [ ] **Growth tracking** - Measure plant size/health over time
- [ ] **Pest detection** - Identify pests or disease via vision
- [ ] **Growth time-lapse** - Capture images on schedule, compile into video

### Data & Monitoring
- [ ] **Alerting** - Notify when conditions out of range or harvest ready
- [ ] **Historical analysis** - Track growth rates, correlate with conditions
- [ ] **Yield tracking** - Track harvests over time, optimize for yield
- [ ] **Environmental dashboard** - Rich visualization of all metrics

### Scale & Fleet
- [ ] **Multi-station fleet** - Multiple grow stations with centralized monitoring
- [ ] **Cross-station comparison** - Compare growth across different setups
- [ ] **Centralized recipes** - Push environment profiles to all stations

### Triggers (Gap Feature)
- [ ] **Humidity trigger** - When humidity < 40%, activate mister automatically
- [ ] **Temperature trigger** - When temp > 85°F, activate fans and send alert
- [ ] **Soil moisture trigger** - When soil dry, trigger watering cycle
- [ ] **Light trigger** - Adjust grow lights based on ambient light sensor

### Data Pipeline / ML Training (Gap Feature)
- [ ] **Automated data capture** - Capture images on schedule for training data
- [ ] **Growth stage labeling** - Label images with growth stage for ML training
- [ ] **Train ripeness model** - Use captured data to train harvest-ready detector
- [ ] **Deploy trained model** - Push updated model to all stations via Registry
- [ ] **Model performance tracking** - Compare model accuracy across versions

### Monitoring & Alerting (Gap Feature)
- [ ] **Threshold alerts** - Configure alerts for out-of-range conditions
- [ ] **Fleet health dashboard** - Single view of all station statuses
- [ ] **Daily digest** - Scheduled summary of all station metrics
- [ ] **Anomaly detection** - Alert on unusual patterns (sensor drift, failures)

---

## Stretch Goals

- [ ] Harvesting arm on gantry (complex mechanical addition)
- [ ] Seed planting automation
- [ ] Integration with weather API for outdoor greenhouses
- [ ] Produce delivery handoff to mobile robot
- [ ] Nutrient dosing for hydroponics
- [ ] CO2 monitoring and injection

---

## Success Criteria

**MVP Complete When:**
- [ ] Sensors reading and logging to Viam cloud
- [ ] Dashboard shows current and historical data
- [ ] Automated watering triggers correctly (if Option B+)
- [ ] System runs unattended for 24+ hours

**Project Complete When:**
- [ ] Plants successfully grown from seed to harvest
- [ ] All selected backlog items implemented
- [ ] Time-lapse video created
- [ ] Documentation complete

---

## Documentation Deliverables

- [ ] README with setup instructions
- [ ] Hardware wiring guide
- [ ] Sensor calibration guide
- [ ] Fragment templates for different crops
- [ ] Dashboard configuration
- [ ] Time-lapse setup guide

---

## Links

- **Jira Epic:** [TBD]
- **GitHub Repo:** [TBD]
- **Viam Organization:** [TBD]
- **Hardware BOM:** [TBD]

---

## Notes

**Why this project scores highly:**
- Naturally exercises all 5 lifecycle stages (prototype → deploy → scale → fleet → maintain)
- Data capture, cloud sync, remote monitoring are Viam strengths
- Remote-friendly for distributed team members
- Tangible output (actual vegetables/herbs)
- Great content potential (time-lapses, growth data)
- Easy to scale from 1 station to many (fleet demo)

**Gap Features This Project Addresses:**
- **Fleet Management** - Primary demo of multi-machine coordination with 2-3 sensor stations
- **Triggers** - Threshold-based automation (humidity, temperature, soil moisture)
- **Data Pipeline** - End-to-end capture → label → train → deploy workflow
- **Monitoring/Alerting** - Environmental alerts and fleet health dashboard
- **Scheduled Tasks** - Periodic sensor readings, daily reports, time-lapse capture
