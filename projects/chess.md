# Project: Chess

## Overview

**One-line description:** Robot that plays chess against humans, physically moving pieces on a real board

**Project Lead:** TBD
**Team Members:** TBD
**Status:** Existing (has backlog)

## Description

Chess is a robotic chess opponent that uses computer vision to detect piece positions, a chess engine for move calculation, and a robot arm to physically move pieces on a real chessboard. Players sit across from the robot and play a normal game of chess.

This project demonstrates vision-based detection, ML for piece classification, precise manipulation, and creates an extremely engaging interactive demo.

## Viam Capabilities Demonstrated

- [x] Motion / Arm Control
- [x] Gripper Manipulation
- [x] Vision / ML
- [x] Data Management (game recording)
- [ ] Fleet Management
- [x] Remote Operation
- [x] Modular Resources (chess service)
- [ ] Multi-machine Coordination
- [x] Cloud Integration
- [x] Data Pipeline ← **Capture → Train → Deploy for piece detection**
- [x] Triggers ← **Game end detection, board state changes**

## Hardware Requirements

| Component | Description | Options |
|-----------|-------------|---------|
| Arm | 6-DOF robot arm for piece movement | xArm 6, xArm 5 Lite |
| Gripper | Chess piece handling | Small parallel jaw, magnetic, vacuum |
| Camera | Board state detection | Overhead mounted, Intel RealSense |
| Board | Standard chess board | Standard board, custom with markers |
| Pieces | Detectable chess pieces | Standard pieces, custom for easier detection |
| Compute | Main controller | Raspberry Pi 4, Intel NUC |

**Estimated Hardware Cost:** $TBD (arm is primary cost)

**Remote-Friendly:** Yes - can play against robot remotely via video feed

---

## MVP Options

Select one for hackathon scope:

### Option A: Full Game Play (Recommended if building on existing)
Robot plays complete game, detects all pieces, makes legal moves against human opponent.
- **Complexity:** High
- **Demo Appeal:** Very High
- **Scope:** Piece detection, chess engine integration, full game flow

### Option B: Move Execution Only
Human inputs moves via app, robot executes them physically.
- **Complexity:** Medium
- **Demo Appeal:** High
- **Scope:** Motion planning, piece manipulation, no vision required

### Option C: Piece Reset
Robot resets board to starting position after game ends.
- **Complexity:** Medium
- **Demo Appeal:** Medium
- **Scope:** All piece detection, organized placement

### Option D: Teaching Mode
Robot demonstrates famous games move-by-move with commentary.
- **Complexity:** Medium
- **Demo Appeal:** High
- **Scope:** Scripted moves, display integration

**Selected MVP:** _______________

---

## Backlog

Select 3-5 items for post-hackathon development:

### Gameplay
- [ ] **Difficulty levels** - Adjustable AI difficulty (beginner to expert)
- [ ] **Opening book** - Pre-programmed opening strategies
- [ ] **Captured piece handling** - Sort captured pieces into trays
- [ ] **Game clock** - Timed games with physical/virtual clock

### Data & Analytics
- [ ] **Game recording** - Capture and replay games with data service
- [ ] **Tournament mode** - Track multiple games, maintain leaderboard
- [ ] **Opening book training** - Learn from games played, improve strategy
- [ ] **Player statistics** - Track wins/losses/draws per player

### User Experience
- [ ] **Remote play** - Play against robot from anywhere via app
- [ ] **Voice commentary** - Robot announces moves and commentary
- [ ] **Spectator mode** - Live streaming with move overlay
- [ ] **Move hints** - Optional hints for learning players

### Scale & Fleet
- [ ] **Multi-board fleet** - Multiple chess stations, centralized tournaments
- [ ] **Online integration** - Integration with chess.com or Lichess for ratings
- [ ] **Robot vs robot** - Two robots play each other

### Data Pipeline / ML Training (Gap Feature)
- [ ] **Automated board capture** - Capture board images during every game
- [ ] **Piece position labeling** - Auto-label images with known game state
- [ ] **Training data export** - Export labeled dataset for model training
- [ ] **Train improved detector** - Use captured data to train better piece-finder
- [ ] **Deploy updated model** - Push improved model via Registry
- [ ] **A/B model comparison** - Compare detection accuracy between model versions

### Triggers (Gap Feature)
- [ ] **Game end trigger** - Detect checkmate/stalemate, auto-save game and offer reset
- [ ] **Human move trigger** - Detect when human has moved, robot responds
- [ ] **Illegal move alert** - Trigger alert if detected position is impossible
- [ ] **Timeout trigger** - If no move detected for X minutes, prompt player

---

## Stretch Goals

- [ ] Play other games (checkers, Go with different board)
- [ ] Personality modes (aggressive, defensive, teaching)
- [ ] Celebrity voice packs for commentary
- [ ] AR overlay showing possible moves
- [ ] Integration with chess puzzles/training

---

## Success Criteria

**MVP Complete When:**
- [ ] Robot accurately detects all piece positions
- [ ] Robot makes legal chess moves
- [ ] Robot can play a complete game without errors
- [ ] Human player has a good experience

**Project Complete When:**
- [ ] All selected backlog items implemented
- [ ] Win rate against average players is reasonable
- [ ] Can run unsupervised at an event

---

## Documentation Deliverables

- [ ] README with setup instructions
- [ ] Hardware assembly guide (linked from existing doc)
- [ ] Camera calibration guide
- [ ] Chess engine configuration
- [ ] Demo operation guide

---

## Links

- **Existing Code:** ~/viam/viam-chess
- **Hardware Doc:** https://docs.google.com/document/d/1T_ZlkjAxhhUZB5_EhZ64C6UP2SrXKVqBU8UHFkGirrw/
- **Setup Photos:** https://photos.app.goo.gl/GDuryUgFtMPufmRD7
- **Jira Epic:** [TBD]
- **Viam Organization:** [TBD]

---

## Notes

**Gap Features This Project Addresses:**
- **Data Pipeline** - Excellent example of capture → label → train → deploy cycle (board images auto-labeled with game state)
- **Triggers** - Game end detection, human move detection, timeout handling

**Why data pipeline fits here:**
- Chess has automatic ground truth - the game state IS the label
- Every game generates labeled training data for free
- Clear metric for model improvement (detection accuracy)
- Natural A/B testing opportunity (old model vs new model)
