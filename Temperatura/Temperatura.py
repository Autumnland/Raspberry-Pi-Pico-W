import machine
import utime

sensortemp = machine.ADC(4)
factorconversion = 3.3 / 65365

while True:

     rawValue = sensortemp.read_u16() * factorconversion
     temperatura = 27 - (rawValue - 0.706) / 0.001721
     print(temperatura)
     utime.sleep(0.1)
