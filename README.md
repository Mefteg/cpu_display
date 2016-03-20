# cpu_display
Display cpu usage using a 1mA AmpMeter.

## Install
### Arduino
Install Arduino IDE: https://www.arduino.cc/en/Main/Software
### Python
Install Python 2.7: https://www.python.org/downloads/

Install 'pyserial' and 'psutil':
```
pip install pyserial psutil # super user rights could be required (use sudo for instance)
```

## Usage
### Arduino
Tested on Arduino Uno and Arduino Nano.

Simply upload the sketch to you Arduino device.

Only pin 10 is used to communicate with the AmpMeter.
### Python
Set you port in "(project_folder)/python/preferences.json".

Launch with:
```
python cpu.py
```
