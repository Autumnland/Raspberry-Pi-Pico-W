import machine
import utime
from ssd1306 import SSD1306_I2C

# Configurar el bus I2C
i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8))

# Configurar el OLED Display
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

# Función para leer la temperatura de la Raspberry Pi Pico
def get_temperature():
    temp_sensor = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = temp_sensor.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    return temperature

# Mostrar la temperatura en la pantalla OLED
while True:
    oled.fill(0)
    oled.text("Temp: {:.1f} C".format(get_temperature()), 0, 0)
    oled.show()
    utime.sleep(0.01)
