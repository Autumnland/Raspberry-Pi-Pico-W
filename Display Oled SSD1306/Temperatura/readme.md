## En esta practica vamos a conectar la Raspberry Pi Pico W con un Display Oled SSD1306 para imprimir la temperatura que tiene la Raspberry.

### Componentes necesarios:

- Un protoboard
- Una Raspberry Pi Pico W
- Display Oled SSD1306
- Unos cuantos cables dupont machos

### Conexion de los componentes:

- Puerto GND de la pantalla a cualquier GND de la Raspberry
- puerto VCC de la pantalla a 3V3(out) de la Raspberry

Los puertos SCL y SDA ya dependen del codigo, pero en este caso se conectan de la siguiente manera:

- Puerto SCL de la pantalla a GP9 de la Raspberry
- Puerto SDA de la pantalla a GP8 de la Raspberry

Se veria asi:

<p align="center"><img src="https://github.com/Autumnland/Raspberry-Pi-Pico-W/assets/112134604/ed6588d0-2e65-491b-8694-be1ce74a748c" align="center" width="361" height="332"/></p>

### Explicacion:

Necesitamos que la Raspbery este completamente limpia.

Entramos a Thonny y instalamos MicroPython(Raspberry Pi pico) a nuestra Raspberry.

Al acabar de instalar descargamos las siguientes librerias:

- micropython_ssd1306

Solo faltaria descargar el codigo, abrirlo y guardarlo en la Raspberry como main.py para que se ejecute solo.
