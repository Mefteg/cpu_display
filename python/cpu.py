import serial
import time
import psutil
import struct
import json
import atexit

KEY_PORT = 'port'
KEY_BAUDRATE = 'baudrate'

#############
# FUNCTIONS #
#############

# Get preferences stored in a JSON file
def get_preferences(filename):
    # get preferences (port, baudrate, etc...)
    filePreferences = open(filename, 'r')
    data = filePreferences.read()
    filePreferences.close()

    # JSON decode
    return json.loads(data)
#end get_preferences

# LOCKING OPERATION
# Try to connect to the device. If it fails, it waits 1 second and try again.
def connection(preferences):
    ser = serial.Serial()
    ser.port = preferences[KEY_PORT]
    ser.baudrate = preferences[KEY_BAUDRATE]

    # wait for connection
    while not ser.is_open:
        try:
            ser.open()
        except (ValueError, serial.SerialException) as error:
            time.sleep(1)

    # wait a bit because connection reboots the arduino
    time.sleep(5)

    return ser
# end connection

# Callback executed when the program is killed
def exit_handler(ser):
    if ser:
        ser.close()
#end exit_handler

########
# MAIN #
########

# get preferences (in a JSON format)
preferences = get_preferences('preferences.json')

# wait for connection
ser = connection(preferences)

# set exit callback
atexit.register(exit_handler, ser)

# loop
while True:
    try:
    	cpu = psutil.cpu_percent(interval=None) * 2.55 # (255 / 100)
    	cpu_int = int(cpu)

    	ser.write(bytes(cpu_int))
    	
    	data = ser.readline()
    except (ValueError, serial.SerialException, serial.SerialTimeoutException, AttributeError) as error:
        ser.close()
        # wait for a reconnection
        ser = connection(preferences)

	time.sleep(0.05)
