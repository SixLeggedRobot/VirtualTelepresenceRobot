from adafruit_servokit import ServoKit
import time
kit=ServoKit(channels=16 , address=0x40)
kit2=ServoKit(channels=16 , address=0x41)
kit.servo[0].angle=90
time.sleep(0.4)
kit.servo[1].angle=90
time.sleep(0.4)
kit.servo[2].angle=90
time.sleep(0.4)
kit.servo[4].angle=90
time.sleep(0.4)
kit.servo[5].angle=90
time.sleep(0.4)
kit.servo[6].angle=90
time.sleep(0.4)
kit.servo[8].angle=90
time.sleep(0.4)
kit.servo[9].angle=90
time.sleep(0.4)
kit.servo[10].angle=90
time.sleep(0.4)



kit2.servo[0].angle=90
time.sleep(0.4)
kit2.servo[1].angle=90
time.sleep(0.4)
kit2.servo[2].angle=90
time.sleep(0.4)
kit2.servo[8].angle=90
time.sleep(0.4)
kit2.servo[9].angle=90
time.sleep(0.4)
kit2.servo[10].angle=90
time.sleep(0.4)
kit2.servo[12].angle=90
time.sleep(0.4)
kit2.servo[13].angle=90
time.sleep(0.4)
kit2.servo[14].angle=90
