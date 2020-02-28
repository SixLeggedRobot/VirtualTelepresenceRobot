#pair1-rightfront,leftmid,rightrear
#pair2-leftfront,rightmid,leftrear

from adafruit_servokit import ServoKit
import time
kit=ServoKit(channels=16 , address=0x40)
kit1=ServoKit(channels=16 , address=0x41)

rf0=kit.servo[0]
rf1=kit.servo[1]
rf2=kit.servo[2]
rm0=kit.servo[4]
rm1=kit.servo[5]
rm2=kit.servo[6]
rr0=kit.servo[8]
rr1=kit.servo[9]
rr2=kit.servo[10]

lf0=kit1.servo[12]
lf1=kit1.servo[13]
lf2=kit1.servo[14]
lm0=kit1.servo[8]
lm1=kit1.servo[9]
lm2=kit1.servo[10]
lr0=kit1.servo[0]
lr1=kit1.servo[1]
lr2=kit1.servo[2]
while True:
    #pair1
    rf1.angle=150
    lm1.angle=30
    rr1.angle=150
    time.sleep(0.2)

    rf0.angle=100
    lf0.angle=120
    lm0.angle=80
    rm0.angle=60
    rr0.angle=100
    lr0.angle=120
    time.sleep(0.2)

    rf1.angle=100
    lm1.angle=80
    rr1.angle=100
    
    #pair2
    lf1.angle=30
    rm1.angle=150
    lr1.angle=30
    time.sleep(0.2)
    
    lf0.angle=80
    rf0.angle=60
    rm0.angle=100
    lm0.angle=120
    lr0.angle=80
    rr0.angle=60
    time.sleep(0.2)
    
    lf1.angle=80
    rm1.angle=100
    lr1.angle=80

        
    
    