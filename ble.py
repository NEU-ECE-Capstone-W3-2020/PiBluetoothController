from bluepy import btle

nordic_uuid="6e400001-b5a3-f393-e0a9-e50e24dcca9e"

class ScanDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print "Discovered device", dev.addr
            for (adtype, desc, value) in dev.getScanData():
                if value == nordic_uuid:
                    print "DISCOVERED BLE BEACON!"
                    print "  %s = %s" % (desc, value)
        elif isNewData:
            print "Received new data from", dev.addr

scanner = btle.Scanner().withDelegate(ScanDelegate())
devices = scanner.scan()

