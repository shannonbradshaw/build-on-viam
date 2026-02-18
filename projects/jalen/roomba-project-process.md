# Roomba Integration Project - Process Guide

Complete workflow for integrating a Roomba 650/655 with Viam platform.

---

## Phase 1: Hardware Preparation

### 1.1 Gather Components
- [ ] Roomba 650 or 655
- [ ] Raspberry Pi 5 (or Pi 4)
- [ ] Adafruit Mini-DIN cable (#2438)
- [ ] USB-to-TTL adapter (CH340 or FTDI)
- [ ] UBEC voltage regulator (Adafruit #1385) - for battery-powered option
- [ ] Jumper wires (male-to-female)
- [ ] Tools: Soldering iron, multimeter, crimping tool, drill

### 1.2 Battery Connection (Battery-Powered Option)
- [ ] Disassemble Roomba (remove top cover)
- [ ] Locate battery pads below Dock button
- [ ] Solder wires to battery pads (positive and ground)
- [ ] Connect battery wires to UBEC input
- [ ] Solder UBEC output wires to battery jumper wires (for Pi GPIO connection)
- [ ] Add heat shrink tubing around soldered connections for insulation
- [ ] Crimp DuPont connectors on the combined wires
- [ ] Test UBEC output voltage (should be 5.0-5.2V)

### 1.3 Serial Communication Wiring
- [ ] Mini-DIN cable wires (Pin 3 and Pin 4) come pre-stripped and exposed
- [ ] Crimp DuPont connectors to Pin 3 and Pin 4 wires
- [ ] Set USB-to-TTL voltage jumper to 5V mode
- [ ] Connect wires (crossed): Roomba Pin 3 → TTL TX, Roomba Pin 4 → TTL RX
- [ ] Test continuity with multimeter

### 1.4 Physical Integration
- [ ] Drill small hole in Roomba body for battery wires (from internal pads to external UBEC)
- [ ] Drill hole in Roomba cover for Mini-DIN cable routing
- [ ] Route battery wires through body hole
- [ ] Route Mini-DIN cable through cover hole
- [ ] Add strain relief and cable management

---

## Phase 2: Initial Testing

### 2.1 Power Test
- [ ] Connect soldered UBEC output wires to Pi GPIO (Pin 4 = 5V, Pin 6 = GND)
- [ ] Power on Roomba
- [ ] Verify Pi boots successfully (green LED on)
- [ ] Check for stable power (no shutdowns or reboots)

### 2.2 Serial Connection Test
- [ ] Set up Python virtual environment on Pi
- [ ] Install pyserial package
- [ ] Run debug_roomba_serial.py script
- [ ] Verify serial port detected (/dev/ttyUSB0)
- [ ] Test button press detection (confirms RX working)
- [ ] Test beep command (confirms TX working)
- [ ] Verify sensor data reading (battery, charging state)

### 2.3 Troubleshooting
- [ ] Fix any crimp/connection issues found
- [ ] Verify TX/RX paths with multimeter if needed
- [ ] Test with FULL mode if Safe mode causes shutdown
- [ ] Document any issues and solutions

---

## Appendix: Key Resources

**Documentation:**
- Battery-powered wiring tutorial: `roomba-wiring-tutorial-battery-powered.md`
- External power wiring tutorial: `roomba-wiring-tutorial-external-power.md`
- Connection test script: `debug_roomba_serial.py`
- Main README: `README.md`

**Hardware References:**
- [Adafruit Mini-DIN Cable](https://www.adafruit.com/product/2438)
- [Adafruit UBEC](https://www.adafruit.com/product/1385)
- [Roomba Open Interface Spec](https://cdn-shop.adafruit.com/datasheets/create_2_Open_Interface_Spec.pdf)

**Viam Resources:**
- [Viam Documentation](https://docs.viam.com)
- [Viam Module Registry](https://app.viam.com/registry)
- [Viam Python SDK](https://python.viam.dev)
