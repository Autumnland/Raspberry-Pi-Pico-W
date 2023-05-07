#Programa para encender el led de la pico
#Hecho por Luis Eduardo
#02/03/2023

from picozero import pico_led
from time import sleep

while True:
    pico_led.on()
    sleep(0.5)
    pico_led.off()
    sleep(0.5)