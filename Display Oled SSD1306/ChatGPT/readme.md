## En esta practica vamos a conectar la Raspberry Pi Pico W con la inteligencia artificial de ChatGPT.

Para eso vamos a necesitar los siguiente componentes:

- Un protoboard
- Una Raspberry Pi Pico W
- Display Oled SSD1306
- 1 Boton de dos pines
- Unos cuantos cables dupont machos

Otra cosa que necesitaras en conseguir tu propia API de ChatGPT, para eso ve al siguiente enlace:

Antes de hacer cualquier cosa necesitamos tener nuestra Raspberry completamente limpia.

Para empezar lo que tenemos que hacer es entrar a Thonny y instalar CircuitPython(generico) en la Raspberry.

Cuando se acabe de instalar notaremos que nuestra Raspberry aparecera como si fuera algun tipo de USB y podremos acceder a los archivos que tenga esta.

Hasta aqui ya deberias tener descargado los archivos que deje, asi que vamos a descomprimir el archivo con el siguiente nombre: CircuitPython_GetSuperpower_PicoW_OpenAI.

Al acabar de descomprimirlo entramos a la carpeta que nos da y notaremos que hay otras 2 carpetas, vamos a entrar a la que se llama CircuitPython 8.x, ya adentro copiamos todo y lo pegamos dentro de nuestra Raspberry, al hacer eso empezara a pasar todo lo que copiamos, en algun momento antes de acabar nos mostrara un mensaje de si deseamos remplazar algunos archivos, asi que daremos que si.

Cuando alla terminado entramos a la carpeta de setings y pegamos el siguiente codigo:

```

OPENAI_API_KEY="Aqui pegaras tu API de ChatGPT"
WIFI_SSID="Aqui colocaras el nombre de tu red wifi"
WIFI_PASSWORD="Aqui colocaras la contrasenia de tu wifi"

```

