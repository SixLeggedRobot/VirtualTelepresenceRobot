import RPi.GPIO as GPIO
import time
from adafruit_servokit import ServoKit
kit=ServoKit(channels=16 , address=0x40)
kit1=ServoKit(channels=16 , address=0x41)
rf0=kit1.servo[0]
rf1=kit1.servo[1]
rf2=kit1.servo[2]
rm0=kit.servo[8]
rm1=kit.servo[9]
rm2=kit.servo[10]
rr0=kit.servo[4]
rr1=kit.servo[5]
rr2=kit.servo[6]

lf0=kit1.servo[8]
lf1=kit1.servo[9]
lf2=kit1.servo[10]
lm0=kit1.servo[12]
lm1=kit1.servo[13]
lm2=kit1.servo[14]
lr0=kit.servo[0]
lr1=kit.servo[1]
lr2=kit.servo[2]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG=17
ECHO=27


GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

time.sleep(5)

def stop():
    rf1.angle=100
    time.sleep(1)
    lm1.angle=80
    time.sleep(1)
    rr1.angle=100
    time.sleep(3)

    lf1.angle=80
    time.sleep(1)
    rm1.angle=100
    time.sleep(1)
    lr1.angle=80

    rf2.angle=100
    time.sleep(1)
    lm2.angle=80
    time.sleep(1)
    rr2.angle=100
    time.sleep(1)


    lf2.angle=80
    time.sleep(1)
    rm2.angle=100
    time.sleep(1)
    lr2.angle=80
    time.sleep(1)

    rf0.angle=90
    rm0.angle=90
    rr0.angle=90
    time.sleep(1)
    lf0.angle=90
    lm0.angle=90
    lr0.angle=90
    time.sleep(2)
def forward():
    rf1.angle=160
    lm1.angle=20
    rr1.angle=160
    time.sleep(1)
    #1st tringular gait up

    rf0.angle=70
    lf0.angle=90
    rm0.angle=90
    lm0.angle=110
    rr0.angle=70
    lr0.angle=90
    time.sleep(1)
    #1st tgait swing

    rf1.angle=110#come back with lil push
    lm1.angle=70
    rr1.angle=110
    time.sleep(2)  #switch gait

    #rf1.angle=100
    #lm1.angle=80
    #rr1.angle=100***/#initial

    #pair2
    lf1.angle=20
    rm1.angle=160
    lr1.angle=20
    time.sleep(1)

    lf0.angle=110
    rf0.angle=90
    rm0.angle=70
    lm0.angle=90
    lr0.angle=110
    rr0.angle=90
    time.sleep(1)

    lf1.angle=70
    rm1.angle=110
    lr1.angle=70
    time.sleep(2)

def back():

def left():

def right():

stop()
count=0

while True:
    i=0
    avgDistance=0
    for i in range(5):
        GPIO.output(TRIG, False)
        time.sleep(0.1)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
            pass
        pulse_start = time.time()
        while GPIO.input(ECHO)==1:
            pass
        pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance=pulse_duration*17150
        distance=round(distance,2)
        avgDistance=avgDistance+distance

    avgDistance=avgDistance/5
    print avgDistance

    flag=0
    if avgDistance < 15:
        count=count+1
        stop()
        time.sleep(1)
        back()
        time.sleep(1)
        if(count%3 == 1) & (flag==0):
            right()
            flag=1
        else:
            left()
            flag=0
        time.sleep(1)
        stop()
        time.sleep(1)
    else:
        forward()
        flag=0
