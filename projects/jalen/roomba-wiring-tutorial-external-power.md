# Roomba 650/655 Hardware Setup Tutorial (External Power)

Complete guide for connecting a Raspberry Pi to a Roomba 650/655 using external power. This setup keeps the Pi powered independently via USB power bank, using the Roomba only for serial communication.

**Power Method:** External USB power bank (simplest and safest option)

---

## Components Required

| Component | Specification | Example |
|-----------|---------------|---------|
| Roomba 650/655 | 600 series with Open Interface | iRobot Roomba 650 or 655 |
| Raspberry Pi | Pi 4 or Pi 5 | Raspberry Pi 5 recommended |
| Mini-DIN Cable | 7-pin for Roomba (serial communication only) | [Adafruit #2438](https://www.adafruit.com/product/2438) |
| USB-to-TTL Adapter | 5V tolerant serial adapter | FTDI, CP2102, or CH340-based |
| USB Power Bank | Powers Raspberry Pi independently | 5V output, 3A minimum (5A recommended for Pi 5) |
| Jumper Wires | For serial connections | Male-to-female recommended |

**Note:** With external power, the Mini-DIN cable is used ONLY for serial communication (TX/RX), not power.

---

## Mini-DIN Connector Pinout

The Roomba's 7-pin Mini-DIN connector provides serial communication and power:

![Mini-DIN Connector Pinout](images/mini-din-pinout.png)

**Why External Power?**
Mini-DIN Pins 1 & 2 (Vpwr) have a 200mA PTC fuse (500mA peak). This is insufficient for any Raspberry Pi model. Using external power avoids this limitation entirely.

---

## Wiring Instructions

### Step 1: Power Connection (USB Power Bank → Pi)

This is the simplest power option - no voltage regulation or GPIO wiring needed!

**Your Task:**

1. **Connect USB power bank to Raspberry Pi:**
   - Connect USB-C cable from power bank to Pi's USB-C power port
   - Ensure power bank is fully charged and supports 5V/3A output minimum

2. **Verify Pi powers on:**
   - Green LED on Pi should light up steadily
   - Pi should begin boot sequence
   - If Pi doesn't power on, try a different power bank or cable

3. **Power bank requirements:**
   - Minimum 3A output (5V/3A = 15W)
   - Recommended 5A for Pi 5 (5V/5A = 25W for optimal performance)
   - USB-C PD (Power Delivery) capable recommended
   - Capacity: 20,000mAh+ recommended for extended use

**Advantages of External Power:**
- ✅ No risk of incorrect voltage damaging Pi
- ✅ No impact on Roomba battery runtime
- ✅ Easy to swap/recharge power bank independently
- ✅ No soldering or GPIO connections required
- ✅ Simplest and safest setup method

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

## Safety Checklist

Before powering on, verify:

- [ ] USB power bank is charged
- [ ] Pi powers on from power bank (green LED lit)
- [ ] USB-to-TTL adapter voltage jumper set to 5V
- [ ] USB-to-TTL adapter is properly inserted in Pi USB port
- [ ] TX/RX connections are crossed (TX → RX, RX → TX)
- [ ] Mini-DIN cable fully inserted into Roomba
- [ ] Roomba battery is charged (press Clean button to check)
- [ ] No exposed wires that could short

---

## Troubleshooting

### Power Issues

**Problem:** Pi doesn't power on
- Check power bank is charged (press button to see charge level)
- Try different USB cable (some cables are charge-only, not data+power)
- Verify cable is plugged into Pi's power port (not data port)
- Test power bank with another device to confirm it works
- Ensure power bank output is 5V/3A minimum (5A for Pi 5)

**Problem:** Pi powers on but shuts off randomly
- Power bank may not supply enough current (Pi 4/5 need 3-5A)
- Verify power bank supports USB-C PD (Power Delivery)
- Check for loose USB-C connection
- Power bank may be in low-battery mode (recharge it)
- Some power banks don't provide enough current - try a higher-rated one

**Problem:** Power bank drains quickly
- Pi 5 draws ~10-25W continuously (Pi 4: ~6-15W)
- 20,000mAh power bank (~100Wh) = ~4-10 hours runtime depending on load
- Consider larger capacity bank for longer sessions
- Bring spare charged power bank for all-day use

### Serial Communication Issues

**Problem:** Serial port not detected
- Run `lsusb` to verify USB-to-TTL is recognized
- Try different USB port on Pi (not power port!)
- Verify USB-to-TTL voltage jumper set to 5V
- Check for driver installation requirements (some adapters need manual drivers)

**Problem:** No response from Roomba
- Press Clean button to wake Roomba
- Verify TX/RX crossed: Roomba Pin 3 → TTL TX, Roomba Pin 4 → TTL RX
- Check baud rate is 115200
- Ensure Mini-DIN cable fully inserted into Roomba
- Try sending Start command (byte 128) multiple times

**Problem:** Roomba sleeps after 5 minutes
- Normal OI behavior - not a bug
- Send periodic OI commands to stay awake
- Consider BRC pin implementation (advanced)

---

## Notes on the Hardware

### Power System
- **Battery independence:** Pi and Roomba run on separate power sources
- **No runtime impact:** Roomba battery runtime is unaffected
- **Power bank selection:** 20,000mAh+ recommended, must support 3-5A output
- **USB-C PD support:** Strongly recommended for Pi 4/5 reliable power delivery
- **Charging:** Can charge/swap power bank without affecting Roomba
- **Why not Mini-DIN power:** Vpwr pins have 200mA fuse - Pi 4/5 draw 3-5A (15-40x over limit)

### Serial Communication
- **Baud rate:** 115200 (default for Roomba 650/655)
- **Voltage levels:** Roomba uses 5V logic on TX/RX
- **USB-to-TTL safety:** Isolates Pi's 3.3V GPIO from Roomba's 5V signals
- **No shared ground needed:** Each device has independent power source

### Comparison with Battery-Powered Setup
**External Power Advantages:**
- Simpler setup (no soldering, no voltage regulation)
- Safer (no risk of incorrect voltage)
- No impact on Roomba battery life
- Easy to troubleshoot (isolate power and serial issues)

**External Power Disadvantages:**
- Need to manage two batteries (Roomba + power bank)
- Extra device to mount on Roomba
- Power bank adds weight

---

## References

### Official Documentation
- [Create 2 Open Interface Specification](https://cdn-shop.adafruit.com/datasheets/create_2_Open_Interface_Spec.pdf)
- [iRobot Roomba Open Interface Pinout](https://pinoutguide.com/Electronics/irobot_roomba_serial_pinout.shtml)

### Hardware Components
- [Adafruit Mini-DIN Cable (#2438)](https://www.adafruit.com/product/2438)

### Community Projects
- [Pi Streaming Roomba](https://yakinikuman.github.io/pistreaming_roomba/) - Community tutorial with power options
