from gpiozero import MotionSensor
import os

pinNumber=4 # Pin Number from the GPIO layout on your Raspberry Pi
pir = MotionSensor(pinNumber)
while True:
    pir.wait_for_motion()
    print("Motion Detected")
    os.system("xset dpms force on")
    pir.wait_for_no_motion()
    print("Motion Stopped")

