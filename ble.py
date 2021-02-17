from bluepy import btle

nordic_uuid="6e400001-b5a3-f393-e0a9-e50e24dcca9e"
device_mac=""

class ScanDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print "Discovered device", dev.addr
        elif isNewData:
            print "Received new data from", dev.addr

scanner = btle.Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(1.0)

for dev in devices:
    for (adtype, desc, value) in dev.getScanData():
        if value == nordic_uuid:
            print "Discovered capstone device!"
            device_mac = dev.addr
            print device_mac
            print dev.addr


print "Device mac!", device_mac
p = btle.Peripheral(device_mac, "random")

try:
    service = p.getServiceByUUID(nordic_uuid)
    characteristics = service.getCharacteristics()
    for c in characteristics:
        print c.propertiesToString()
        if (c.supportsRead()):
            v = c.read()
            print v
finally:
    p.disconnect()
