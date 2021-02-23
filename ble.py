import struct
from bluepy.btle import *

# callback class
class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print(data)

# connect to device
per = Peripheral("d7:3d:77:bf:db:b3", "random")
notify_uuid = '6e400003-b5a3-f393-e0a9-e50e24dcca9e'

try:
    # set callback for notifications
    per.setDelegate(MyDelegate())

    # enable notification
    # setup_data = b"\x01\x00"
    # notify = per.getCharacteristics(uuid=notify_uuid)[0]
    # notify_handle = notify.getHandle() + 1
    # write 1 to the notify characteristic to subscribe to notifications?
    # per.writeCharacteristic(notify_handle, setup_data, withResponse=True)
    
    for c in per.getCharacteristics():
        # print(c.propertiesToString())
        if "READ" in c.propertiesToString():
            if c.uuid == notify_uuid:
                print(c.read().decode("utf-8"))
finally:
    per.disconnect()