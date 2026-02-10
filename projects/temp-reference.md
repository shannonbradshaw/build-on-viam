Problem
For lab managers it takes a lot of effort to maintain the lab in order: fasteners, electronic components, tools, consumables all need to be neatly organized every day. Besides ensuring that everything is in its proper place, they have to manually maintain an up-to-date inventory and reorder items when they’re running low.
For lab users it’s hard to know if the lab even has an item they need, where it’s located, or if someone is using it at the moment.

Case in point:

Proposal
A modular automated storage system for the lab. It’s like a vending machine that has both an output and an input. Users can select an item they need on the screen (e.g. M4 nuts) and the machine gives them a bin where those items are stored. When they’re done, they place the bin back in the “Return” slot, and the machine puts it back in its place.

Isometric view of the 29-bin system (1m x 1m x 0.5m)
I
Gripper close-up

How it works
Every bin has an RFID tag in the bottom that the machine can read to identify it, they should also have human readable labels on the sides
All bins are registered in the database (Airtable for starters) where their contents are assigned (e.g. bin with ID 123 is used for M4 nuts) and where they can be updated (e.g. renamed)
The machine keeps the state of the position of the bins inside of it, so they should not be generally manually accessible, with the exception of troubleshooting. Still each bin is uniquely identifiable through RFID, so even in the event of reshuffling the state can be updated by the machine with a reindexing routine.
The machine only uses 3-axis gantry to pick and place bins from and into their slots, no additional actuators needed

Retrieval process

Features
Automatic inventory digital twin maintained by the machine
Public (for employees) searchable database with bins and their up-to-date status:
Is the bin stored or currently used
Latest snapshot of bin contents (bin contents are snapshotted every time it’s returned)
Photo or badge ID of the person retrieving the bin, to know who is the actively using the bin
Possible future features
Bulk return mechanism: a system that allows placing multiple bins in the return slot, instead of returning them one-by-one
Computer Vision-based inventory estimation: quantity of items in the bin estimated from the return photo and is recorded in the database
Computer Vision-based bin content validation: e.g. alert message is sent if somebody put a screw in a washer bin
Additional bin sizes, e.g. 8’ x 12’

Item
Type
Product URL
Unit price

# of units

Total cost
Bin 6' x 8'
Other
https://www.mcmaster.com/4315T71-4315T712/
$9.42
29
$273.18
20mm x 20mm x 1000mm V-slot rail
Framing
https://makerstore.cc/product/v-slot-20-x-20mm/
$13.25
18
$238.50
20mm x 60mm x 1000mm V-slot rail
Framing
https://makerstore.cc/product/v-slot-20-x-60mm/
$24.25
2
$48.50
20mm x 60mm x 500mm V-slot rail
Framing
https://makerstore.cc/product/v-slot-20-x-60mm/
$12.40
1
$12.40
20mm x 60mm x 1000mm V-slot rail
Framing
https://makerstore.cc/product/v-slot-20-x-80mm-4/
$31.15
1
$31.15
V-slot 3-way cube
Framing
https://makerstore.cc/product/us-brac-cube/
$4.00
8
$32.00
V-slot 90 degree corner connector
Framing
https://makerstore.cc/product/90-degree-angle-corner-connector-v-slot/
$3.40
8
$27.20
V-slot sliding T-nut
Framing
https://makerstore.cc/product/sliding-t-nut/
$0.65
180
$117.00
V-slot low-profile screws (various lengths)
Framing
https://makerstore.cc/product/m5-low-profile-screws/
$0.30
180
$54.00
Dual V Wheel Kit – Metal
Motion
https://makerstore.cc/product/dual-v-wheel-kit-metal/
$8.40
16
$134.40
Smooth Idler Pulley Kit
Motion
https://makerstore.cc/product/us-wheel-pulley-kit/
$6.00
6
$36.00
Motor Mount Plate – NEMA23
Motion
https://makerstore.cc/product/motor-mount-plate-nema23/
$14.80
3
$44.40
GT2 (2mm) Timing Belt
Motion
https://makerstore.cc/product/gt2-2mm-timing-belt-per-meter/
$4.95
4
$19.80
GT2 (2mm) Aluminum Timing Pulley 30
Motion
https://makerstore.cc/product/gt2-2mm-aluminum-timing-pulley-30/
$8.65
3
$25.95
NEMA 23 Bipolar Stepper Motor
Electronics
https://www.omc-stepperonline.com/nema-23-bipolar-1-8deg-1-16nm-164-3oz-in-1-5a-5-4v-57x57x56mm-4-wires-23hs22-1504s
$13.37
3
$40.11
Stepper Motor Driver
Electronics
https://www.adafruit.com/product/6121?gad_campaignid=21079227318
$8.95
3
$26.85
RFID reader board
Electronics
https://www.adafruit.com/product/364
$39.95
1
$39.95
IR distance sensor
Electronics
https://www.sparkfun.com/infrared-proximity-sensor-sharp-gp2y0a21yk.html
$15.50
2
$31.00
Raspberry Pi touch display
Electronics
https://www.pishop.us/product/official-raspberry-pi-7-touch-screen-display-with-10-finger-capacitive-touch/?src=raspberrypi
$66.00
1
$66.00
