# Bluetooth Controller for Raspberry Pi 

## Setup BLE

**Run all commands on your device:**

```bash
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo apt-get install bluez bluez-firmware pi-bluetooth
bluetoothctl
agent on
default-agent
scan on
```

If you see a bunch of MAC addresses printing at this point, the bluetooth radio is configured correctly and you can `exit` the bluetoothctl shell.

# Setup Python
```bash
sudo apt-get install python-pip
sudo apt-get install libglib2.0-dev
sudo pip install bluepy
```

# Running the Script

**In order to scan for devices you must run the command with sudo:**
`sudo python ble.py`
