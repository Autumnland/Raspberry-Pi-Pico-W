import machine
import ssd1306
import network
import time

# Configuración de la pantalla SSD1306
i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Configuración de Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

# Función para mostrar las redes Wi-Fi en la pantalla
def mostrar_redes():
    redes = wifi.scan()
    for i, red in enumerate(redes):
        oled.fill(0)
        oled.text("Redes Wi-Fi:", 0, 0)
        ssid = red[0].decode("utf-8")
        oled.text(ssid, 0, 10)
        time.sleep(1)
        oled.show()

# Bucle principal
while True:
    mostrar_redes()