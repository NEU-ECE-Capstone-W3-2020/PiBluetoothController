from bluepy import btle
print "Connecting..."
dev = btle.Peripheral("D7:3D:77:BF:DB:B3") 
print "Services..."
for svc in dev.services:
    print str(svc)

