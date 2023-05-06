import machine
from ssd1306 import SSD1306_I2C

# Configurar el bus I2C
i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8))

# Configurar el OLED Display
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

# Mostrar "Hola Mundo" en la pantalla OLED
oled.fill(0)
oled.text("Hola Mundo", 0, 0)
oled.show()