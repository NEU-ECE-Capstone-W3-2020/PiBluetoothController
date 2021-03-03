from bluepy.btle import *
import time
import serial

ser = serial.Serial(
        port='/dev/ttyUSB0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        timeout=1
)
counter=0
ser.flush()

# connect to device
notify_uuid = '6e400003-b5a3-f393-e0a9-e50e24dcca9e'

last_str = ""

while True:
    try:
        # set callback for notifications
        # per.setDelegate(MyDelegate())
        per = Peripheral("d7:3d:77:bf:db:b3", "random")
        for c in per.getCharacteristics():
            # print(c.propertiesToString())
            if "READ" in c.propertiesToString():
                if c.uuid == notify_uuid:
                    cur_str = c.read().decode("utf-8")
                    if cur_str != last_str:
                        print(cur_str)
                        ser.write(bytes(cur_str + '\n', "utf8"))
                        line = ser.readline().decode('utf-8')
                        print("got ", line)
                        per.disconnect()
                        time.sleep(3)
    except:
        continue