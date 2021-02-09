# Bluetooth Controller for Raspberry Pi 

## Setup

**Run these commands on your device:**

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

If you see a bunch of MAC addresses printing at this point, the bluetooth radio is configured correctly.

