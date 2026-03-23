import collections
import collections.abc

# These lines fix the DroneKit crash on Python 3.10+
# The "# type: ignore" tells VS Code to stop complaining about it
collections.MutableMapping = collections.abc.MutableMapping  # type: ignore
collections.Mapping = collections.abc.Mapping                # type: ignore

from dronekit import connect, VehicleMode
import time

# --- Rest of your connection code ---

# Connect to the SITL simulation
print("Connecting to vehicle...")
# Added a timeout and explicit heartbeat check
vehicle = connect('127.0.0.1:14550', wait_ready=True, timeout=60)

# STEP 2: Wait a second for parameters to sync
time.sleep(2)

# Read some state with "None" checks
print("--- Vehicle Status ---")
if vehicle.location.global_frame:
    print(f" GPS: {vehicle.location.global_frame}")

if vehicle.battery:
    print(f" Battery: {vehicle.battery}")

# This is likely where your error was:
if vehicle.mode:
    print(f" Mode: {vehicle.mode.name}")
else:
    print(" Mode: Waiting for heartbeat...")

print(f" Altitude: {vehicle.location.global_relative_frame.alt}")

# Close vehicle object
vehicle.close()
print("Done!")