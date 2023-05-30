## En esta practica vamos a conectar la Raspberry Pi Pico W con la inteligencia artificial de ChatGPT.

### Componentes necesarios:

- Un protoboard
- Una Raspberry Pi Pico W
- Display Oled SSD1306
- 1 Boton de dos pines
- Unos cuantos cables dupont machos

### Conexion de los componentes:

- Puerto GND de la pantalla a cualquier GND de la Raspberry
- puerto VCC de la pantalla a 3V3(out) de la Raspberry

Los puertos SCL y SDA ya dependen del codigo al igual que la conexion del boton, pero en este caso se conectan de la siguiente manera:

- Puerto SCL de la pantalla a GP17 de la Raspberry
- Puerto SDA de la pantalla a GP16 de la Raspberry
- Unos de los pines del boton debe estar conectado a cualquier GND de la Raspberry y el otro al GP14

Se veria asi:

<p align="center"><img src="https://github.com/Autumnland/Raspberry-Pi-Pico-W/assets/112134604/598fa940-90f5-4f78-b200-82fefe214ee4" align="center" width="344" height="321"/></p>

### Explicacion:

Antes de hacer cualquier cosa necesitamos tener nuestra Raspberry completamente limpia.

Para empezar lo que tenemos que hacer es entrar a Thonny y instalar CircuitPython(generico) en la Raspberry.

Cuando se acabe de instalar notaremos que nuestra Raspberry aparecera como si fuera algun tipo de USB y podremos acceder a los archivos que tenga esta.

Hasta aqui ya deberias tener descargado los archivos que deje, asi que vamos a descomprimir el archivo con el siguiente nombre: CircuitPython_GetSuperpower_PicoW_OpenAI.

Al acabar de descomprimirlo entramos a la carpeta que nos da y notaremos que hay otras 2 carpetas, vamos a entrar a la que se llama CircuitPython 8.x, ya adentro copiamos todo y lo pegamos dentro de nuestra Raspberry, al hacer eso empezara a pasar todo lo que copiamos, en algun momento antes de acabar nos mostrara un mensaje, el mensaje nos dira si deseamos reemplazar algunos archivos, asi que daremos que si.

Cuando alla terminado entramos a un archivo que se llama settings y pegamos el siguiente codigo:

```
OPENAI_API_KEY="Aqui pegaras tu API de ChatGPT"
WIFI_SSID="Aqui colocaras el nombre de tu red wifi"
WIFI_PASSWORD="Aqui colocaras la contrasenia de tu wifi"
```

Para completar una parte necesitaras conseguir es tu propia API de ChatGPT, para eso ve al siguiente enlace: <A HREF="https://platform.openai.com/account/api-keys"> https://platform.openai.com/account/api-keys </A>

Una vez que pegaste el codigo y llenaste los datos restantes nos pasamos a Thonny.

Solo abres el codigo que deje y lo guardas en tu Raspberry como main.py, eso para que no necesites compilarlo cada rato y se ejecute solo
