DroneKit SITL Connection Test
A simple Python script to establish a MAVLink connection with an ArduPilot SITL instance and retrieve basic telemetry data (GPS, Battery, Flight Mode, and Altitude).

Prerequisites
Python 3.10+ (Script includes collections.abc compatibility patches)

ArduPilot SITL installed on Linux (Mint/Ubuntu)

MAVProxy (Required for the sim_vehicle.py bridge)

Setup Instructions
1. Start the Virtual Drone (SITL)
In your first terminal, launch the ArduCopter simulation. This acts as the "server" for your script.

Bash
sim_vehicle.py -v ArduCopter --console
Wait until the terminal displays the MAV> prompt before proceeding.

2. Prepare the Python Environment
In a new terminal window, navigate to your project folder and set up your dependencies:

Bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required libraries
pip install dronekit pymavlink
3. Run the Telemetry Script
Ensure the simulator from Step 1 is still running. In your second terminal (with the venv active), execute:

Bash
python3 script.py
Expected Output
Upon successful connection, the script will print the following:

GPS Coordinates: Global latitude and longitude.

Battery Status: Voltage and percentage level.

Flight Mode: Current state (e.g., STABILIZE).

Relative Altitude: Meters above the takeoff point.
⚠️ Challenges Faced

While building this, I ran into several real-world issues:

DroneKit crashing due to collections import changes in Python 3.10+
Virtual environment inconsistencies
SITL connection timing and heartbeat delays
Running multiple terminal sessions (one for SITL, one for script)

🚀 Future Improvements
Auto takeoff and landing
Waypoint navigation
Battery failsafe system
Telemetry dashboard
💡 Why this project?

This project helped me understand how to:

Work with drone simulation environments
Debug real-world system issues
Handle communication between software and simulated hardware

Built using:

Python
DroneKit
ArduPilot SITLe resolved through debugging and environment fixes


Flight Mode: Current state (e.g., STABILIZE).

Relative Altitude: Meters above the takeoff point.
