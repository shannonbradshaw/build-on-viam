# Project: Barista

## Overview

**One-line description:** Robotic coffee station that prepares espresso drinks on demand

**Project Lead:** TBD
**Team Members:** TBD
**Status:** Proposed

## Description

Barista is a robotic coffee preparation system that makes espresso-based drinks on demand. Using a robot arm, the system operates an espresso machine - grinding beans, tamping, pulling shots, steaming milk, and assembling drinks. Customers order via a tablet interface or mobile app and watch their drink being prepared.

This project combines manipulation complexity (multi-step beverage preparation), customer-facing interaction (ordering interface), and operational features (inventory tracking, scheduling, quality monitoring). It's a natural complement to Vino, demonstrating similar customer delivery features with significantly more complex automation.

Coffee is a high-frequency use case - unlike wine (occasional), coffee is daily. This creates natural opportunities for data collection, model training, and demonstrating fleet management across multiple office locations.

## Viam Capabilities Demonstrated

- [x] Motion / Arm Control ← **Complex multi-step manipulation**
- [x] Gripper Manipulation (portafilter, cups, tamper)
- [x] Vision / ML (cup detection, foam quality, fill level)
- [x] Data Management (order history, drink analytics)
- [x] Fleet Management ← **Multiple coffee stations**
- [x] Remote Operation
- [x] Modular Resources (barista service)
- [ ] Multi-machine Coordination
- [x] Cloud Integration
- [x] Customer Delivery ← **Ordering app, preferences, billing**
- [x] Triggers ← **Order received, cup placed, brew complete**
- [x] Scheduled Tasks ← **Cleaning cycles, bean refill checks**
- [x] Monitoring/Alerting ← **Bean level, water, temperature**
- [x] Data Pipeline ← **Quality images for training**

## Hardware Requirements

| Component | Description | Options |
|-----------|-------------|---------|
| Arm | 6-DOF robot arm | xArm 6, xArm 5 Lite, UFactory Lite 6 |
| Gripper | Multi-tool handling | Parallel jaw + custom portafilter holder |
| Espresso Machine | Semi-auto espresso | Breville Barista Express, Gaggia Classic, Rancilio Silvia |
| Grinder | Coffee grinding | Built-in or separate burr grinder |
| Camera | Drink monitoring | USB camera for cup/fill detection |
| Tablet | Order interface | iPad or Android tablet |
| Cup Dispenser | Cup staging | Simple gravity dispenser |
| Milk System | Steaming/frothing | Machine steam wand or separate frother |
| Sensors | Level monitoring | Weight sensors for beans/water |
| Compute | Main controller | Raspberry Pi 4, Intel NUC |

**Estimated Hardware Cost:** $3,000-6,000 (arm + espresso machine + accessories)

**Remote-Friendly:** Partially - control logic can be developed remotely, physical testing requires hardware

---

## MVP Options

Select one for hackathon scope:

### Option A: Single Drink Type (Recommended)
Make espresso shots only - no milk, no variations.
- **Complexity:** Medium
- **Demo Appeal:** High
- **Scope:** Portafilter handling, tamping, shot pulling, cup delivery

### Option B: Espresso + Americano
Espresso plus hot water addition for Americano.
- **Complexity:** Medium
- **Demo Appeal:** High
- **Scope:** Adds water dispensing step

### Option C: Full Drink Menu
Espresso, Americano, Latte (requires milk steaming).
- **Complexity:** High
- **Demo Appeal:** Very High
- **Scope:** Adds milk steaming, foam quality monitoring

### Option D: Order Interface Focus
Simple drink preparation + polished ordering interface.
- **Complexity:** Medium
- **Demo Appeal:** High
- **Scope:** Focus on customer experience, simpler manipulation

**Selected MVP:** _______________

---

## Backlog

Select 3-5 items for post-hackathon development:

### Drink Preparation
- [ ] **Multiple drink types** - Espresso, Americano, Latte, Cappuccino
- [ ] **Size variations** - Small, Medium, Large cups
- [ ] **Strength options** - Single, double, triple shots
- [ ] **Milk alternatives** - Oat, almond, soy milk handling
- [ ] **Temperature control** - Monitor and adjust brew temperature

### Manipulation & Quality
- [ ] **Tamping pressure** - Consistent tamp pressure via force feedback
- [ ] **Grind adjustment** - Automatic grind size tuning based on shot time
- [ ] **Foam quality detection** - ML model assesses microfoam quality
- [ ] **Fill level monitoring** - Camera detects fill level, stops at correct amount
- [ ] **Latte art** - Stretch goal: pour patterns for latte art

### Customer Delivery (Gap Feature)
- [ ] **Web ordering interface** - TypeScript SDK tablet app for ordering
- [ ] **Mobile app** - Flutter SDK app for remote ordering
- [ ] **Guest profiles** - Remember regular orders, preferences
- [ ] **Order queue display** - Show pending orders on screen
- [ ] **Billing integration** - Per-drink billing demonstration
- [ ] **Loyalty tracking** - Drink count, rewards (demo)

### Triggers (Gap Feature)
- [ ] **Order received trigger** - New order starts preparation sequence
- [ ] **Cup placed trigger** - Sensor detects cup in position, proceeds
- [ ] **Shot complete trigger** - Detect shot volume reached, stop extraction
- [ ] **Low beans alert** - Weight sensor triggers refill alert
- [ ] **Water level alert** - Trigger alert when reservoir low
- [ ] **Temperature alert** - Alert if brew temp out of range

### Scheduled Tasks (Gap Feature)
- [ ] **Morning warmup** - Pre-heat machine before office opens
- [ ] **Cleaning cycle** - Daily backflush and cleaning routine
- [ ] **Inventory check** - Daily bean/water level report
- [ ] **Descaling reminder** - Schedule-based maintenance alert

### Data Pipeline / ML Training (Gap Feature)
- [ ] **Drink image capture** - Capture image of every finished drink
- [ ] **Quality labeling** - Rate drinks for quality (foam, color, fill)
- [ ] **Train quality model** - Detect good vs bad drinks before serving
- [ ] **Shot time tracking** - Capture extraction times for grind tuning
- [ ] **Failure mode capture** - Image failed drinks for troubleshooting

### Monitoring & Alerting (Gap Feature)
- [ ] **Real-time dashboard** - Station status, queue length, drink stats
- [ ] **Inventory alerts** - Beans, milk, cups, water levels
- [ ] **Error notifications** - Alert on jams, spills, machine issues
- [ ] **Usage analytics** - Popular drinks, peak times, wait times

### Fleet (Gap Feature)
- [ ] **Multi-station deployment** - Same config across office locations
- [ ] **Centralized ordering** - Order from any station, view all queues
- [ ] **Cross-station analytics** - Compare usage, quality across locations
- [ ] **Unified inventory** - Track supplies across all stations

---

## Stretch Goals

- [ ] Voice ordering ("Hey Barista, make me a latte")
- [ ] Latte art patterns (hearts, leaves, etc.)
- [ ] Cold brew / iced drink support
- [ ] Bean variety selection from multiple hoppers
- [ ] Integration with calendar (make coffee before meeting ends)
- [ ] Roast date tracking and freshness alerts
- [ ] Per-user caffeine tracking (optional health feature)

---

## Success Criteria

**MVP Complete When:**
- [ ] Robot can prepare an espresso shot end-to-end
- [ ] Cup is correctly positioned and filled
- [ ] Order can be placed via tablet interface
- [ ] Works reliably for 5+ drinks in sequence
- [ ] No spills or safety issues

**Project Complete When:**
- [ ] Multiple drink types available
- [ ] Customer ordering interface polished
- [ ] Monitoring dashboard operational
- [ ] All selected backlog items implemented
- [ ] Documentation complete
- [ ] Can run unsupervised for a morning

---

## Documentation Deliverables

- [ ] README with setup instructions
- [ ] Hardware assembly guide
- [ ] Espresso machine integration guide
- [ ] Drink recipe configuration
- [ ] Customer app setup guide
- [ ] Operations and maintenance guide
- [ ] Troubleshooting guide (jams, spills, quality issues)

---

## Links

- **Jira Epic:** [TBD]
- **GitHub Repo:** [TBD]
- **Viam Organization:** [TBD]
- **Hardware BOM:** [TBD]

---

## Notes

**Why this project is compelling:**

1. **High engagement** - Everyone loves coffee, high interaction frequency
2. **Demo appeal** - Watching a robot make your coffee is captivating
3. **Real utility** - Actually useful in an office setting
4. **Feature coverage** - Naturally exercises many Viam capabilities
5. **Complexity showcase** - Multi-step manipulation is impressive
6. **Scale story** - Easy to imagine multiple stations (fleet)

**Gap Features This Project Addresses:**
- **Customer Delivery** - Full ordering interface with TypeScript/Flutter SDKs
- **Triggers** - Order received, cup placed, shot complete, inventory alerts
- **Scheduled Tasks** - Morning warmup, cleaning cycles, inventory checks
- **Monitoring/Alerting** - Bean level, water level, temperature, usage dashboard
- **Data Pipeline** - Drink quality images, shot timing data, model training
- **Fleet Management** - Multiple coffee stations with centralized management

**Comparison to Vino:**

| Aspect | Vino | Barista |
|--------|------|---------|
| Drink complexity | Single action (pour) | Multi-step (grind, tamp, brew, steam) |
| Frequency | Occasional | Daily/multiple per day |
| Temperature sensitivity | Room temp | Critical (brew temp, steam temp) |
| Quality variation | Low | High (many variables affect quality) |
| Data opportunity | Low volume | High volume, quality metrics |
| Fleet potential | Medium | High (every office needs coffee) |

**Risk Factors:**
- Espresso machine integration varies by model
- Milk steaming is complex manipulation
- Quality consistency requires tuning
- Cleanup and maintenance are significant
- Hot liquids require safety considerations

**Recommended Approach:**
1. Start with espresso-only MVP (no milk)
2. Use semi-automatic machine with exposed portafilter
3. Focus on reliability before adding drink types
4. Add customer interface early for engagement
5. Milk steaming as post-hackathon enhancement
