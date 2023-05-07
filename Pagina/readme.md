## En esta practica vamos a conectar la Raspberry Pi Pico W con un Display Oled SSD1306 para imprimir la hora exacta, obteniendola de internet.

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

### Explicacion:

Necesitamos que la Raspbery este completamente limpia.

Entramos a Thonny y instalamos MicroPython(Raspberry Pi pico) a nuestra Raspberry.

Al acabar de instalar descargamos las siguientes librerias:

- micropython_ssd1306
- picozero

Solo faltaria descargar el codigo, abrirlo y guardarlo en la Raspberry como main.py para que se ejecute solo.

Otra cosa antes de ejecutar, hay una parte del codigo que te indica que datos modificaras para su ejecucion.

Esta es la parte que modificaras:

![image](https://user-images.githubusercontent.com/112134604/236651838-4798ab24-9b4d-415b-b112-34deed37b40d.png)
