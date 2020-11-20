#!/usr/bin/env python

"""
 Maak een teller. Je hebt een drukknop die optelt en één die naar beneden telt.
 """

from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Button
import time

__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


remote_factory = PiGPIOFactory(host='192.168.1.31')
Button1 = Button(pin=17, pin_factory=remote_factory)
Button2 = Button(pin=22, pin_factory=remote_factory)
Button3 = Button(pin=23, pin_factory=remote_factory)

def main():
    counter = 0
    while True:
        if Button1.is_pressed:
            time.sleep(1)
            counter = counter + 1
            print(counter)
        if Button2.is_pressed:
            time.sleep(1)
            counter = counter - 1
            print(counter)
        if Button3.is_pressed:
            time.sleep(1)
            counter = 0
            print(counter)

if __name__ == '__main__':  # code to execute if called from command-line#
    main()
