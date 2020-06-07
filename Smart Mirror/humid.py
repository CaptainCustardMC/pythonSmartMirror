import sys
import os
import Adafruit_DHT
from time import sleep
from Tkinter import *

pinNum=17

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, pinNum)
    temp=temperature,"C", humidity,"%"
    if humidity>80:
        print ("Humidity too high!")
        os.system("shutdown now")
    print (temp)

