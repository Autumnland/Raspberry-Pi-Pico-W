import network

# Configuración de la red WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Escaneo de redes cercanas
nets = wlan.scan()
print("Se encontraron las siguientes redes WiFi:\n")
for net in nets:
    ssid = net[0].decode("utf-8")
    rssi = net[3]
    print("- %s (RSSI: %d dB)" % (ssid, rssi))