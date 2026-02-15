# Roomba 650/655 Hardware Setup Tutorial (Battery-Powered)

Complete guide for connecting a Raspberry Pi to a Roomba 650/655 using direct battery connection for power. This setup allows the Pi to run entirely from the Roomba's battery.

**Power Method:** Direct battery connection (bypasses Mini-DIN fuse limitation)

---

## Components Required

| Component | Specification | Example |
|-----------|---------------|---------|
| Roomba 650/655 (Pre-wired) | 600 series with Open Interface, battery connection installed | iRobot Roomba 650 or 655 |
| Raspberry Pi | Pi 4 or Pi 5 | Raspberry Pi 5 recommended |
| Mini-DIN Cable | 7-pin for Roomba (serial communication only) | [Adafruit #2438](https://www.adafruit.com/product/2438) |
| USB-to-TTL Adapter | 5V tolerant serial adapter | FTDI, CP2102, or CH340-based |
| Jumper Wires | For UBEC output and serial connections | Male-to-female recommended |

**Note:** The Roomba comes pre-wired with direct battery connection and UBEC already installed.

---

## Mini-DIN Connector Pinout

The Roomba's 7-pin Mini-DIN connector provides serial communication and power:

![Mini-DIN Connector Pinout](images/mini-din-pinout.png)

**Important:** Pins 1 and 2 are connected to the Roomba's battery through a 200mA PTC resettable fuse.

---

## Wiring Instructions

### Step 1: Power Connection (UBEC → Pi)

**⚠️ CRITICAL SAFETY WARNING:**
The Roomba battery provides 12-17V unregulated. The pre-wired UBEC steps this down to 5V. **Never bypass the UBEC** - battery voltage will destroy the Pi instantly!

**Pre-Wired Setup (Already Complete):**
- Battery wires soldered to pads below Roomba's Dock button
- Battery wires connected to UBEC input
- UBEC outputs regulated 5V via servo connector

**UBEC Output Connector Pinout:**
The 3-pin female servo connector has:
- **Pin 1 (Black/Brown wire):** Ground (GND)
- **Pin 2 (Red wire):** 5V Power (regulated)
- **Pin 3:** Not connected (NC) - ignore this pin

**Your Task - Connect UBEC Output to Raspberry Pi:**

1. **Verify UBEC output voltage (STRONGLY RECOMMENDED):**
   - Use a multimeter before connecting to Pi
   - Measure between UBEC Pin 2 (red) and Pin 1 (black)
   - Should read 5.0-5.2V
   - If voltage is wrong, STOP and ask for help

2. **Prepare jumper wires:**
   - Take 2x male-to-female jumper wires (red and black recommended)
   - You only need 2 pins - ignore Pin 3

3. **Connect UBEC to Raspberry Pi GPIO:**
   ```
   UBEC Pin 2 (Red/5V)    →  Pi GPIO Pin 4 (5V)
   UBEC Pin 1 (Black/GND) →  Pi GPIO Pin 6 (GND)
   ```
   - Insert male ends into UBEC servo connector (Pins 1 and 2 are adjacent)
   - Connect female ends to Pi GPIO header (Pins 4 and 6 are adjacent)
   - Ensure connections are secure

4. **Power on test:**
   - Pi should boot when Roomba is powered on
   - Green LED on Pi should light up steadily
   - If Pi doesn't power on, check connections and voltage

---

### Step 2: Serial Communication (Roomba ↔ USB-to-TTL ↔ Pi)

**⚠️ CRITICAL:** The Roomba uses 5V logic on TXD/RXD. Direct connection to Pi GPIO (3.3V) may damage the Pi. Use a USB-to-TTL adapter instead, which handles voltage differences safely.

1. **Configure USB-to-TTL adapter**:
   - Set the voltage jumper to 5V mode
   - This ensures the adapter can properly read the Roomba's 5V signals

2. **Wire connections** (cross TX/RX):
   ```
   Roomba Pin 3 (RXD) → USB-to-TTL TX pin
   Roomba Pin 4 (TXD) → USB-to-TTL RX pin
   ```
   **Remember:** TX goes to RX, RX goes to TX (crossed connections)

3. **Connect USB-to-TTL to Pi**:
   - Plug USB-to-TTL adapter into any Pi USB port
   - No GPIO pins needed for serial communication

---

### Step 3: Optional - BRC (Baud Rate Change) Pin

The BRC pin (Pin 5) can be used to prevent the Roomba from sleeping, but is **not required** for basic operation. Skip this for initial setup.

---

## Connection Diagram

![Connection Diagram](images/connection-diagram.jpg)

**Note:** If you need clarification on any part of this diagram, ask Jalen.

---

## Safety Checklist

Before powering on, verify:

- [ ] UBEC output voltage is 5.0-5.2V (measure with multimeter - CRITICAL!)
- [ ] UBEC 5V wire (red) connects to Pi GPIO Pin 4 (5V)
- [ ] UBEC GND wire (black) connects to Pi GPIO Pin 6 (GND)
- [ ] No exposed wires touching metal or other wires (short circuit risk)
- [ ] Battery connection wires are insulated and secure
- [ ] USB-to-TTL adapter is properly inserted in Pi USB port
- [ ] TX/RX connections are crossed (TX → RX, RX → TX)
- [ ] Roomba battery is charged (press Clean button to check)
- [ ] All connections are firm and won't come loose during movement

---

## Troubleshooting

### Power Issues

**Problem:** Pi doesn't power on
- **Check UBEC output voltage** with multimeter (should be 5.0-5.2V)
- Verify Roomba battery is charged (press Clean button - Roomba should respond)
- Check UBEC connections: Red to Pin 4 (5V), Black to Pin 6 (GND)
- Verify connections are secure and not loose
- Check battery connection wires at UBEC input

**Problem:** Pi powers on then shuts off immediately
- Likely short circuit or loose connection
- Disconnect Pi and check for exposed wires
- Verify GPIO connections are correct (Pin 4 and 6)
- Check UBEC isn't overheating

**Problem:** UBEC voltage is wrong
- If 0V: Battery connection issue or UBEC failure - ask for help
- If >5.5V: STOP! Do not connect to Pi - ask for help
- Verify battery is charged and Roomba powers on

**Problem:** Battery drains faster than normal
- Expected - Pi draws ~1-2A continuously
- ~35% reduction in runtime is normal
- Recharge battery more frequently

### Serial Communication Issues

**Problem:** Serial port not detected
- Run `lsusb` to verify USB-to-TTL is recognized
- Try different USB port on Pi
- Verify USB-to-TTL voltage jumper set to 5V
- Check for driver installation requirements

**Problem:** No response from Roomba
- Press Clean button to wake Roomba
- Verify TX/RX crossed: Roomba Pin 3 → TTL TX, Roomba Pin 4 → TTL RX
- Check baud rate is 115200
- Ensure Mini-DIN cable fully inserted
- Try sending Start command (byte 128) multiple times

**Problem:** Roomba sleeps after 5 minutes
- Normal OI behavior - not a bug
- Send periodic OI commands to stay awake
- Consider BRC pin implementation (advanced)

---

## Notes on the Hardware

### Power System
- **Battery runtime:** Reduced by ~35% when powering Pi from Roomba battery
- **Current draw:** Pi 5 draws ~800mA-1.2A idle, up to 5A under load; Pi 4 draws ~600-800mA idle, up to 3A under load
- **Battery voltage:** 12-17V from Roomba's 14.4V NiMH pack (varies with charge)
- **UBEC capacity:** 3A continuous, 5A peak - sufficient for both Pi 4 and Pi 5
- **Why direct battery:** Mini-DIN Vpwr pins have 200mA fuse - Pi 4/5 draw 3-5A (15-25x over limit)

### Serial Communication
- **Baud rate:** 115200 (default for Roomba 650/655)
- **Voltage levels:** Roomba uses 5V logic on TX/RX
- **USB-to-TTL safety:** Isolates Pi's 3.3V GPIO from Roomba's 5V signals
- **Ground reference:** Already common through battery connection

---

## References

### Official Documentation
- [Create 2 Open Interface Specification](https://cdn-shop.adafruit.com/datasheets/create_2_Open_Interface_Spec.pdf)
- [iRobot Roomba Open Interface Pinout](https://pinoutguide.com/Electronics/irobot_roomba_serial_pinout.shtml)

### Hardware Components
- [Adafruit Mini-DIN Cable (#2438)](https://www.adafruit.com/product/2438)
- [Adafruit UBEC 5V 3A (#1385)](https://www.adafruit.com/product/1385)

### Community Projects
- [Hacking a Broken Roomba](https://www.royvanrijn.com/blog/2015/12/hacking-a-broken-roomba/) - Direct battery connection method
- [Pi Streaming Roomba](https://yakinikuman.github.io/pistreaming_roomba/) - Alternative approach
