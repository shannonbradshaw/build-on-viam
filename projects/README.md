# Build on Viam Projects

This directory contains all projects for the Build on Viam program.

## Active Projects

| Project | Status | Primary Capabilities | MVP Options |
|---------|--------|---------------------|-------------|
| [Vino](vino.md) | Existing | Arm, gripper, **customer delivery** | Pour on demand, glass detection |
| [Chess](chess.md) | Existing | Arm, vision, ML, **data pipeline** | Full game play, move execution |
| [Greenhouse](greenhouse.md) | New | Data, ML, **fleet**, **triggers** | Monitor + auto-water |
| [Box Bot](box-bot.md) | New | Vision, arm, **triggers** | Flatten only |
| [Dishwasher](dishwasher.md) | New | Arm, vision, **data pipeline** | Single dish type |
| [Cleaning Cart](cleaning-cart.md) | New | Navigation, SLAM, **scheduled tasks** | Patrol + detect |
| [Barista](barista.md) | Proposed | Arm, **customer delivery**, **fleet**, **triggers** | Espresso only |

## Project Comparison

| Project | Platform Coverage | Feasibility | Cool Factor | Assessment Score |
|---------|------------------|-------------|-------------|------------------|
| Greenhouse | 5 | 3 | 5 | **4.6** |
| Barista | 5 | 3 | 5 | **4.5** |
| Box Bot | 4 | 4 | 5 | **4.0** |
| Cleaning Cart | 5 | 2 | 5 | **4.0** |
| Dishwasher | 4 | 3 | 5 | **3.8** |
| Vino | 4 | 4 | 5 | **4.0** |
| Chess | 4 | 4 | 5 | **4.0** |

## Viam Capabilities by Project

| Capability | Vino | Chess | Greenhouse | Box Bot | Dishwasher | Cleaning Cart | Barista |
|------------|------|-------|------------|---------|------------|---------------|---------|
| Arm Control | x | x | | x | x | | x |
| Gripper | x | x | | x | x | | x |
| Vision/ML | x | x | x | x | x | x | x |
| Navigation/SLAM | | | | | | x | |
| Data Capture | x | x | x | x | x | x | x |
| Remote Operation | x | x | x | x | x | x | x |
| Multi-robot Coordination | | | x | | x | x | |
| Fragments | | | x | | | | x |
| **Triggers** | x | x | x | x | x | x | x |
| **Data Pipeline** | | x | x | x | x | | x |
| **Scheduled Tasks** | x | | x | | | x | x |
| **Customer Delivery** | x | | | | | | x |
| **Fleet Management** | | | x | | | x | x |
| **Monitoring/Alerting** | | | x | | | | x |

## Reference Documents

- [Project Assessment Criteria](../docs/project-assessment-criteria.md) - How projects are evaluated
- [Project Template](../templates/project-template.md) - Template for new projects
- [Submission Guidelines](../docs/submission-guidelines.md) - How to propose new projects
- [Project Details Options](project-details-options.md) - Full options breakdown for all projects

## Selecting a Project

During the hackathon kickoff, engineers will select which project to join. Consider:

- Which capabilities do you want to learn?
- What hardware is available to you?
- Which team members do you want to collaborate with?

**Requirement:** Every engineer must join a project team.

## Next Steps

For each project:
1. [ ] Select MVP option
2. [ ] Select 3-5 backlog items
3. [ ] Confirm hardware availability
4. [ ] Assign project lead
5. [ ] Create Jira epic
