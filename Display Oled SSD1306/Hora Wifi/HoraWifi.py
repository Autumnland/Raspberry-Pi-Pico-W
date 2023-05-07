import machine
import utime
import network
import ntptime
from ssd1306 import SSD1306_I2C

# Configurar el bus I2C
i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8))

# Configurar el OLED Display
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

# Configurar la conexión WiFi
ssid = 'TecNM_ITT'
password = ''
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while not wifi.isconnected():
    pass

# Sincronizar la hora con el servidor de tiempo NTP
ntptime.settime()

# Función para convertir el tiempo UTC a PST-8
def utc_to_pst8(utc):
    return (utc - 28800) % 86400

# Mostrar la hora en la pantalla OLED
while True:
    # Obtener la hora actual en PST-8
    utc_time = utime.time()
    pst8_time = utc_to_pst8(utc_time)
    
    # Convertir la hora a un formato legible
    hours = (pst8_time // 3600) % 24
    minutes = (pst8_time // 60) % 60
    seconds = pst8_time % 60
    
    # Mostrar la hora en la pantalla OLED
    oled.fill(0)
    oled.text("{:02d}:{:02d}:{:02d} PST-8".format(hours, minutes, seconds), 0, 0)
    oled.show()
    
    # Esperar 1 segundo antes de volver a obtener la hora
    utime.sleep(1)
