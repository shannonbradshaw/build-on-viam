#!/usr/bin/env python3
"""
Roomba Serial Debug Script
More detailed diagnostics for troubleshooting serial communication issues.
"""

import serial
import time
import sys

def debug_serial(port):
    """Detailed serial debugging with byte-level output."""
    print(f"\n{'='*70}")
    print("Roomba Serial Communication Debug")
    print(f"{'='*70}\n")

    print(f"Port: {port}")
    print(f"Baud: 115200")
    print(f"Data bits: 8, Parity: None, Stop bits: 1\n")

    try:
        ser = serial.Serial(
            port=port,
            baudrate=115200,
            timeout=2,  # Longer timeout for debugging
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE
        )

        print("✅ Serial port opened\n")

        # Clear any existing data
        ser.reset_input_buffer()
        ser.reset_output_buffer()

        print("Test 1: Waking up Roomba")
        print("-" * 70)
        print("Sending START command (byte 128)...")
        ser.write(bytes([128]))
        time.sleep(0.5)
        print("✓ Sent\n")

        print("Test 2: Entering Safe Mode")
        print("-" * 70)
        print("Sending SAFE MODE command (byte 131)...")
        ser.write(bytes([131]))
        time.sleep(0.5)
        print("✓ Sent\n")
        

        print("Test 3: Simple Sensor Request (Charging State)")
        print("-" * 70)
        print("Sending: Sensors(142) ChargingState(21)")
        print("Bytes: [142, 21]")
        ser.write(bytes([142, 21]))
        time.sleep(0.2)

        waiting = ser.in_waiting
        print(f"Bytes waiting to read: {waiting}")

        if waiting > 0:
            data = ser.read(waiting)
            print(f"✅ RECEIVED DATA: {list(data)}")
            print(f"   Raw bytes: {data.hex()}")
            if len(data) >= 1:
                charging_state = data[0]
                states = {
                    0: "Not charging",
                    1: "Reconditioning Charging",
                    2: "Full Charging",
                    3: "Trickle Charging",
                    4: "Waiting",
                    5: "Charging Fault"
                }
                print(f"   Charging state: {states.get(charging_state, 'Unknown')}")
        else:
            print("❌ NO DATA RECEIVED")
            print("\n⚠️  This means:")
            print("   • Commands are being sent (TX working)")
            print("   • But no response is coming back (RX NOT working)")
            print("\n🔍 Check:")
            print("   1. Roomba Pin 4 (TXD) → USB-to-TTL RX pin")
            print("   2. Wire connection is secure")
            print("   3. Roomba is awake (press Clean button)")

        print("\n")
        print("Test 4: Button Press Detection")
        print("-" * 70)
        print("Press the CLEAN button on the Roomba whenever you're ready...")
        print("Monitoring for button press signal for 30 seconds...\n")

        # Request button packet repeatedly for 30 seconds
        for i in range(60):
            ser.write(bytes([142, 18]))  # Buttons packet
            time.sleep(0.5)

            if ser.in_waiting > 0:
                data = ser.read(ser.in_waiting)
                if data[0] != 0:
                    print(f"✅ BUTTON PRESS DETECTED! Data: {list(data)}")
                    print("   This means RX is working!")
                    break

            if i % 2 == 0:
                print(f"   Waiting... ({i//2 + 1}/30 seconds)")
        else:
            print("❌ No button press detected in 30 seconds")
            print("   Either you didn't press it, or RX isn't working")

        print("\n")
        print("Test 5: Beep Test (TX verification)")
        print("-" * 70)
        print("Sending beep command...")
        print("Commands:")
        print("  Song(140) number=0 length=1 note=72 duration=10")
        print("  Play(141) number=0")
        ser.write(bytes([140, 0, 1, 72, 10]))
        time.sleep(0.1)
        ser.write(bytes([141, 0]))
        time.sleep(0.5)

        input("\n❓ Did you hear a beep? (Press Enter to continue)")

        print("\n" + "="*70)
        print("DIAGNOSIS")
        print("="*70)
        print("\n📊 Results Summary:")
        print("   • Serial port: ✅ Opens successfully")
        print("   • TX (sending): Check if you heard beep")
        print("   • RX (receiving): Check if you got sensor data")

        print("\n🔍 Common Issues:")
        print("\n1. NO BEEP + NO DATA = Both TX and RX not working")
        print("   → Check all wiring, Mini-DIN connection")
        print("   → Verify Roomba is powered on")

        print("\n2. BEEP + NO DATA = Only TX working (RX problem)")
        print("   → Check Roomba Pin 4 (TXD) → Adapter RX")
        print("   → This is your current situation if you heard beep")

        print("\n3. NO BEEP + DATA = Only RX working (TX problem)")
        print("   → Check Roomba Pin 3 (RXD) → Adapter TX")

        print("\n4. BEEP + DATA = Everything working! 🎉")

        print("\n" + "="*70 + "\n")

        ser.close()

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    port = sys.argv[1] if len(sys.argv) > 1 else "/dev/ttyUSB0"

    print("\n⚠️  Make sure Roomba is awake!")
    print("   Press Clean button, then press Enter here\n")
    input("Press Enter to start debug...")

    debug_serial(port)
