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

At this point try running `sudo blescan`. You should be able to see your device. Here is the output for my current beacon:

```
Device (new): d7:3d:77:bf:db:b3 (random), -42 dBm 
	Short Local Name: 'BEACO'
	Flags: <06>
	Tx Power: <00>
	Complete 128b Services: <6e400001-b5a3-f393-e0a9-e50e24dcca9e>
```

*Note: This will all be irrelevant eventually but at the beginning of development I'm hard-coding the MAC address for simiplicity*
