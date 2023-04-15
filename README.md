# sharewifi

This script generates a QR code containing the WiFi network name and password for the currently connected network on Windows and Unix-based operating systems.

## Dependencies
This script requires the following dependencies to be installed:
1. Python 3
2. qrcode library (can be installed via pip) : ```pip install qrcode```

Or you can directory install it via pip:

```pip install sharewifi```

## Usage
To use this script, simply run the ```sharewifi.py``` file. If the script is unable to detect a connected WiFi network, it will display an error message.

The script will generate a QR code containing the WiFi network name and password for the currently connected network. This QR code can be scanned using a mobile device to quickly connect to the WiFi network without manually entering the network name and password.

## Operating System Compatibility

This script has been tested on Windows and Unix-based operating systems. However, it may not work on all systems depending on the configuration and network setup.

## Disclaimer
This script is intended for educational and informational purposes only. The author is not responsible for any misuse or damage caused by the use of this script. Use at your own risk.
