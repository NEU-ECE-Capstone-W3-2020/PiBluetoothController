from bluepy.btle import *

# connect to device
per = Peripheral("d7:3d:77:bf:db:b3", "random")
notify_uuid = '6e400003-b5a3-f393-e0a9-e50e24dcca9e'

last_str = ""

while True:
    try:
        # set callback for notifications
        per.setDelegate(MyDelegate())

        for c in per.getCharacteristics():
            # print(c.propertiesToString())
            if "READ" in c.propertiesToString():
                if c.uuid == notify_uuid:
                    cur_str = c.read().decode("utf-8")
                    if cur_str != last_str:
                        print(cur_str)
