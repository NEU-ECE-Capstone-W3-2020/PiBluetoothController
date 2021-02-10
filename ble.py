from bluepy import btle

nordic_uuid="6e400001-b5a3-f393-e0a9-e50e24dcca9e"

class ScanDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print "Discovered device", dev.addr
            try:
                test_dev = btle.Peripheral(dev.addr, btle.ADDR_TYPE_RANDOM)
                for service in test_dev.services:
            	    print str(service.uuid)
            	    if service.uuid.getCommonName() == nordic_uuid:
            		print "AND BINGO WAS HIS NAMO!!!"
            		exit()
            except:
                print "Not our device !!"
        elif isNewData:
            print "Received new data from", dev.addr

scanner = btle.Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)

for dev in devices:
    print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
    for (adtype, desc, value) in dev.getScanData():
        print "  %s = %s" % (desc, value)
