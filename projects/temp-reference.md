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
