# Roomba 650/655 Setup Documentation

This directory contains wiring tutorials and test scripts for connecting a Raspberry Pi to a Roomba 650/655.

## Wiring Tutorials

Choose the tutorial based on your power setup:

### Option 1: Battery-Powered (Recommended for Integration)
**File:** `roomba-wiring-tutorial-battery-powered.md`

- Pi powered directly from Roomba battery via UBEC voltage regulator
- Single power source for entire system
- Pre-wired direct battery connection (bypasses 200mA Mini-DIN fuse)
- ~35% reduction in Roomba battery runtime
- Best for fully integrated robotic applications

### Option 2: External Power (Simpler Setup)
**File:** `roomba-wiring-tutorial-external-power.md`

- Pi powered by separate USB-C power bank
- No impact on Roomba battery runtime
- Simpler wiring (no GPIO connections for power)
- Requires managing two batteries
- Best for testing and development

Both tutorials include:
- Step-by-step wiring instructions
- Safety checklists
- Troubleshooting guides
- Component requirements for Pi 4 and Pi 5

## Connection Test Scripts

Python scripts to verify Roomba serial communication is working before using Viam.

### Setup

**1. Create a virtual environment (recommended):**

```bash
# Create virtual environment
python3 -m venv ~/roomba-env

# Activate virtual environment
source ~/roomba-env/bin/activate

# Your prompt should now show (roomba-env)
```

**2. Install dependencies:**

```bash
# Install pyserial in the virtual environment
pip3 install pyserial
```

**Note:** Remember to activate the virtual environment each time:
```bash
source ~/roomba-env/bin/activate
```

---

### Script 1: `debug_roomba_serial.py` (Recommended)

**Purpose:** Detailed diagnostic script for troubleshooting serial communication issues.

**Usage:**
```bash
source ~/roomba-env/bin/activate
python3 debug_roomba_serial.py /dev/ttyUSB0
```

**What It Tests:**
1. Serial port connection
2. START command (wake Roomba)
3. Sensor reading (charging state)
4. Button press detection (tests RX path)
5. Beep test (tests TX path)
6. Cliff sensor readings

**Features:**
- Shows raw bytes sent/received
- Tests TX and RX paths separately
- 30-second button press detection window
- Diagnoses specific wiring issues
- Explains what each result means

---

### Common Issues & Solutions

**No serial ports found:**
- Check USB-to-TTL adapter is plugged into Pi USB port
- Run `ls /dev/ttyUSB* /dev/ttyACM*` to see available ports
- Try `lsusb` to verify USB device is detected
- Check CH340 driver: `lsmod | grep ch34`

**Serial connection error:**
- Verify TX/RX wires are crossed (Roomba Pin 3 → TTL TX, Roomba Pin 4 → TTL RX)
- Check Mini-DIN cable is fully inserted
- Ensure USB-to-TTL voltage jumper is set to 5V mode
- Test continuity with multimeter on crimped connections

**No sensor data received:**
- Commands being sent but no data back = RX path issue
- Check Roomba Pin 4 (TXD) → USB-to-TTL RX connection
- Verify crimps have electrical continuity (not just mechanical hold)
- Try bypass test: twist wires together directly

## Images

- `images/mini-din-pinout.png` - Official Mini-DIN connector pinout diagram
- `images/connection-diagram.jpg` - Complete wiring diagram for battery-powered setup

## References

- [Roomba Open Interface Specification](https://cdn-shop.adafruit.com/datasheets/create_2_Open_Interface_Spec.pdf)
- [Adafruit Mini-DIN Cable (#2438)](https://www.adafruit.com/product/2438)
- [Adafruit UBEC 5V 3A (#1385)](https://www.adafruit.com/product/1385)
