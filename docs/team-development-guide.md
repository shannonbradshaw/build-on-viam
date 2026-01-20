# Team Development Guide: Building Applications on Shared Robots

This guide explains the recommended architecture and workflow for Build on Viam projects. It's based on the patterns used in [viam-chess](https://github.com/erh/viam-chess), which enables rapid iteration on application code while sharing hardware across team members.

## The Core Architecture: Two Layers

Separate your robot configuration into two distinct layers:

```
┌─────────────────────────────────────────────────────────────────┐
│  Layer 2: APPLICATION (machine config + local development)      │
│  - Application services and modules                             │
│  - Game logic, behavior, business rules                         │
│  - Iterated locally via CLI during development                  │
│  - Packaged as modules for production                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ depends on
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Layer 1: HARDWARE/INTRINSICS (fragment)                        │
│  - Physical components (arm, gripper, camera, motors, sensors)  │
│  - Hardware driver modules                                      │
│  - Frame system and spatial transforms                          │
│  - Rarely changes once hardware is set up                       │
└─────────────────────────────────────────────────────────────────┘
```

### Why This Separation?

1. **Hardware is stable** - Once your arm, camera, and sensors are working, that configuration rarely changes
2. **Application code iterates rapidly** - Game logic, behaviors, and algorithms change constantly during development
3. **Local development is fast** - Run application code on your laptop against remote hardware, no deploy cycle
4. **Production is clean** - Package working code as a module, deploy to machine config

## Layer 1: Hardware/Intrinsics Fragment

Create a fragment containing all physical hardware configuration.

### What Goes in the Hardware Fragment

| Include | Examples |
|---------|----------|
| Physical components | arm, gripper, camera, motors, sensors, boards |
| Hardware driver modules | ufactory, intel-realsense, gpio drivers |
| Frame system | Component positions, transforms, spatial relationships |
| Motion service config | Joint limits, planning parameters |
| Variables | IP addresses, serial numbers, USB paths |

### Example Hardware Fragment

```json
{
  "components": [
    {
      "name": "arm",
      "api": "rdk:component:arm",
      "model": "ufactory:xarm:xarm6",
      "attributes": {
        "host": { "$variable": { "name": "arm-ip-address" } },
        "speed": 100
      },
      "frame": {
        "parent": "world",
        "translation": { "x": 0, "y": 0, "z": 0 }
      }
    },
    {
      "name": "gripper",
      "api": "rdk:component:gripper",
      "model": "ufactory:xarm:gripper",
      "attributes": {
        "arm": "arm"
      }
    },
    {
      "name": "cam",
      "api": "rdk:component:camera",
      "model": "intel:realsense:realsense",
      "attributes": {
        "serial_number": { "$variable": { "name": "cam-serial-number" } }
      },
      "frame": {
        "parent": "arm",
        "translation": { "x": 0, "y": 0, "z": 100 }
      }
    }
  ],
  "modules": [
    {
      "type": "registry",
      "name": "viam_ufactory",
      "module_id": "viam:ufactory",
      "version": "latest"
    },
    {
      "type": "registry",
      "name": "viam_realsense",
      "module_id": "viam:realsense",
      "version": "latest"
    }
  ],
  "services": [
    {
      "name": "builtin",
      "api": "rdk:service:motion",
      "model": "rdk:builtin:builtin"
    }
  ]
}
```

### Fragment Variables

Use variables for anything that differs between physical machines:

```json
{
  "host": { "$variable": { "name": "arm-ip-address" } }
}
```

Common variables:
- `arm-ip-address` - Network address of robot arm
- `cam-serial-number` - Camera serial number
- `board-name` - GPIO board identifier
- `usb-path` - USB device path

## Layer 2: Application Layer

The application layer lives in the machine config and includes your custom services and modules.

### What Goes in the Machine Config

| Include | Examples |
|---------|----------|
| Hardware fragment reference | With variables for this specific machine |
| Fragment mods | Machine-specific overrides |
| Application services | Your custom vision services, game logic, etc. |
| Application modules | Your packaged code |
| UI components | StreamDeck buttons, web interfaces |
| Helper components | Pose savers, calibration tools |

### Example Machine Config

```json
{
  "fragments": [
    {
      "id": "your-hardware-fragment-uuid",
      "variables": {
        "arm-ip-address": "10.1.1.50",
        "cam-serial-number": "327122073698"
      }
    }
  ],
  "fragment_mods": [
    {
      "fragment_id": "your-hardware-fragment-uuid",
      "mods": [
        {
          "$set": {
            "components.arm.frame.translation.z": -10
          }
        }
      ]
    }
  ],
  "components": [
    {
      "name": "pose-home",
      "api": "rdk:component:switch",
      "model": "erh:vmodutils:arm-position-saver",
      "attributes": {
        "arm": "arm",
        "joints": [-0.07, -0.20, -1.57, 0, 1.74, 3.07]
      }
    }
  ],
  "services": [
    {
      "name": "piece-finder",
      "api": "rdk:service:vision",
      "model": "erh:viam-chess:piece-finder",
      "attributes": {
        "input": "cam"
      }
    },
    {
      "name": "chess",
      "api": "rdk:service:generic",
      "model": "erh:viam-chess:chess",
      "attributes": {
        "piece-finder": "piece-finder",
        "arm": "arm",
        "gripper": "gripper",
        "pose-start": "pose-home"
      }
    }
  ],
  "modules": [
    {
      "type": "registry",
      "name": "erh_viam-chess",
      "module_id": "erh:viam-chess",
      "version": "latest"
    }
  ]
}
```

## The CLI Development Pattern

The key to rapid iteration is developing application code locally while using remote hardware. This is done with a CLI tool that connects to the robot.

### How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│  ROBOT (running viam-server)                                     │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │  Hardware fragment applied                                   ││
│  │  - arm, gripper, camera components running                  ││
│  │  - Motion service available                                  ││
│  │  - Frame system configured                                   ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
                              ▲
                              │ WebRTC connection (through NAT/firewalls)
                              │
┌─────────────────────────────┴───────────────────────────────────┐
│  DEVELOPER LAPTOP                                                │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │  CLI Tool                                                    ││
│  │  1. Connect to remote machine                                ││
│  │  2. Get hardware components as dependencies                  ││
│  │  3. Instantiate application service locally                  ││
│  │  4. Run commands, see results instantly                      ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

### Example CLI Tool (Go)

```go
package main

import (
    "context"
    "flag"

    "github.com/erh/vmodutils"
    "go.viam.com/rdk/logging"
    generic "go.viam.com/rdk/services/generic"

    "yourproject"
)

func main() {
    host := flag.String("host", "", "robot hostname or IP")
    cmd := flag.String("cmd", "", "command to run")
    flag.Parse()

    ctx := context.Background()
    logger := logging.NewLogger("cli")

    // 1. Connect to remote machine
    machine, err := vmodutils.ConnectToHostFromCLIToken(ctx, *host, logger)
    if err != nil {
        panic(err)
    }
    defer machine.Close(ctx)

    // 2. Get hardware as local dependencies
    deps, err := vmodutils.MachineToDependencies(machine)
    if err != nil {
        panic(err)
    }

    // 3. Configure your service (references hardware by name)
    cfg := yourproject.Config{
        Arm:     "arm",
        Gripper: "gripper",
        Camera:  "cam",
    }

    // 4. Instantiate your service locally with remote hardware
    svc, err := yourproject.New(ctx, deps, generic.Named("cli"), &cfg, logger)
    if err != nil {
        panic(err)
    }
    defer svc.Close(ctx)

    // 5. Run commands
    switch *cmd {
    case "pick":
        svc.DoCommand(ctx, map[string]interface{}{"pick": true})
    case "place":
        svc.DoCommand(ctx, map[string]interface{}{"place": true})
    }
}
```

### Development Iteration Loop

```
1. Edit application code on your laptop
2. Build CLI: `go build -o mycli cmd/cli/main.go`
3. Run against robot: `./mycli -host robot.local -cmd pick`
4. See results immediately
5. Repeat
```

No module packaging, no deployment, no waiting. Just edit → build → run.

### The vmodutils Helper

The `vmodutils` package (github.com/erh/vmodutils) provides:

- `ConnectToHostFromCLIToken()` - Connect to a Viam machine using CLI credentials
- `MachineToDependencies()` - Convert machine resources to local dependencies

This bridges the gap between cloud-managed hardware and local development.

## Project Structure

Organize your project like viam-chess:

```
your-project/
├── cmd/
│   ├── cli/
│   │   └── main.go           # CLI for local development
│   └── module/
│       └── main.go           # Module entry point for production
├── your_service.go           # Main application logic
├── helper.go                 # Additional application code
├── your_service_test.go      # Tests
├── meta.json                 # Module metadata
├── Makefile                  # Build automation
├── go.mod
└── README.md
```

### meta.json

```json
{
  "module_id": "your-org:your-project",
  "visibility": "public",
  "models": [
    {
      "api": "rdk:service:generic",
      "model": "your-org:your-project:main-service"
    }
  ],
  "entrypoint": "bin/your-project",
  "build": {
    "build": "make module.tar.gz",
    "path": "module.tar.gz",
    "arch": ["linux/amd64", "linux/arm64", "darwin/arm64"]
  }
}
```

### Makefile

```makefile
MODULE_BINARY := bin/your-project

all: $(MODULE_BINARY) cli

cli: *.go cmd/cli/*.go
	go build -o ./mycli cmd/cli/*.go

$(MODULE_BINARY): *.go cmd/module/*.go
	go build -o $(MODULE_BINARY) cmd/module/main.go

test:
	go test ./...

module.tar.gz: meta.json $(MODULE_BINARY)
	strip $(MODULE_BINARY)
	tar czf $@ meta.json $(MODULE_BINARY)

module: test module.tar.gz
```

## Multi-Developer Workflow

### How Multiple Developers Share One Robot

With this architecture, conflicts are minimized:

1. **Hardware fragment is stable** - Rarely edited, owned by project lead
2. **Application code is local** - Each developer runs their own version
3. **No config conflicts** - Developers don't edit the same files simultaneously

### Workflow for a Team

```
┌─────────────────────────────────────────────────────────────────┐
│  Developer A                    Developer B                      │
│  ┌───────────────────┐         ┌───────────────────┐            │
│  │ Working on vision │         │ Working on motion │            │
│  │ piece_finder.go   │         │ movement.go       │            │
│  └─────────┬─────────┘         └─────────┬─────────┘            │
│            │                             │                       │
│            │    ┌───────────────────┐    │                       │
│            └───►│  Shared Robot     │◄───┘                       │
│                 │  (hardware only)  │                            │
│                 └───────────────────┘                            │
│                                                                  │
│  Each developer:                                                 │
│  - Edits code locally                                           │
│  - Runs CLI against shared hardware                             │
│  - Commits to shared repo when ready                            │
└─────────────────────────────────────────────────────────────────┘
```

### Coordination Points

| Situation | Solution |
|-----------|----------|
| Two developers need robot simultaneously | Time-share or use separate test rigs |
| Hardware fragment needs update | Project lead coordinates change |
| Application module ready for production | PR review → merge → publish module |
| Testing a colleague's changes | Pull their branch, build CLI, test |

## From Development to Production

### Development Phase

1. Hardware fragment deployed to robot (one-time setup)
2. Developers iterate using CLI against remote hardware
3. Code lives in git repository
4. Changes reviewed via pull requests

### Production Deployment

1. Build module: `make module`
2. Publish to registry: `viam module upload`
3. Update machine config to reference published module
4. Robot pulls module automatically

### Stable vs Development

With this pattern, "stable" simply means:
- The module version currently deployed to the machine config
- Developers test locally before publishing new versions
- Rollback = change module version in config

No complex fragment tagging needed for application code.

## Fragment Management

### When to Update the Hardware Fragment

- Adding new hardware (camera, sensor, etc.)
- Changing frame relationships
- Updating hardware driver versions
- Fixing calibration values

### Fragment Version Tags

For hardware fragments, use tags to control rollout:

```json
{
  "fragments": [
    {
      "id": "hardware-fragment-uuid",
      "_tag": "stable"
    }
  ]
}
```

- `stable` - Known-working hardware config
- `dev` - Testing hardware changes

### Fragment Variables vs Mods

| Use Variables For | Use Mods For |
|-------------------|--------------|
| IP addresses | Calibration adjustments |
| Serial numbers | Frame translation tweaks |
| USB paths | Joint limit overrides |
| Predictable per-machine differences | One-off fixes for specific machines |

## Quick Reference

### Setting Up a New Project

1. Create hardware fragment with physical components
2. Create machine in Viam app, apply fragment with variables
3. Set up project structure (see above)
4. Build CLI tool using vmodutils pattern
5. Iterate on application code locally

### Daily Development

1. `git pull` latest code
2. `make cli` build CLI tool
3. `./mycli -host robot.local -cmd test` run against hardware
4. Edit code, repeat
5. `git commit` when feature complete

### Deploying to Production

1. `make test` run tests
2. `make module` build module tarball
3. `viam module upload` publish to registry
4. Update machine config with new module version

### Troubleshooting

**"Can't connect to robot"**
- Verify robot is online in Viam app
- Check you're authenticated (`viam login`)
- Verify hostname/IP is correct

**"Component not found"**
- Hardware fragment might not be applied
- Check component names match your config
- Verify fragment variables are set

**"Module not loading"**
- Check module is published to registry
- Verify version in machine config
- Check robot logs for errors

## Example: Chess Project

See [viam-chess](https://github.com/erh/viam-chess) for a complete reference implementation:

- `cmd/cli/main.go` - CLI development tool
- `cmd/module/main.go` - Module entry point
- `chess.go` - Main application service
- `piece_finder.go` - Vision service
- `examples/config1.json` - Machine config example
- `Makefile` - Build automation

This project demonstrates all the patterns described in this guide.
