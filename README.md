# Aqui encontraras algunas practicas hechas con la Raspberry Pi Pico W
## Que es la raspberry pi pico w?

Es una versión actualizada de la Raspberry Pi Pico, una placa de desarrollo de bajo costo y de tamaño reducido diseñada por Raspberry Pi Foundation. La Pico W es una variante que incluye conectividad inalámbrica, lo que significa que puede conectarse a redes Wi-Fi para facilitar la comunicación y el acceso a Internet.

La Raspberry Pi Pico W está basada en el microcontrolador RP2040, desarrollado por Raspberry Pi Foundation. Este microcontrolador es un chip de bajo consumo de energía y de alto rendimiento que utiliza un núcleo ARM Cortex-M0+. La Pico W también incluye 2MB de memoria flash integrada y soporte para interfaces de hardware como GPIO, I2C, SPI, UART y PWM.

La adición de conectividad inalámbrica en la Pico W la hace ideal para proyectos de IoT (Internet de las cosas) y aplicaciones que requieren comunicación sin cables. Puedes utilizarla para crear dispositivos conectados, como sensores, controladores de actuadores y proyectos de automatización del hogar, que se pueden controlar y monitorear de forma remota a través de una red Wi-Fi.

Al igual que la Raspberry Pi Pico original, la Pico W es una placa de desarrollo de bajo costo y de código abierto, lo que significa que su diseño y especificaciones técnicas están disponibles para el público. Esto permite a los usuarios crear sus propias aplicaciones y proyectos personalizados utilizando esta placa como base.

<p align="center"><img src="https://github.com/Autumnland/Raspberry-Pi-Pico-W/assets/112134604/e791e189-024b-48f5-8093-998c31c07c0d" align="center" width="300" height="300"/></p>

## Estas son sus pricipales caracteristicas:

1. Microcontrolador: Está basada en el microcontrolador RP2040 de Raspberry Pi Foundation, que utiliza un núcleo ARM Cortex-M0+ de doble núcleo a 133 MHz.

2. Conectividad inalámbrica: La Raspberry Pi Pico W incorpora un chip de conectividad inalámbrica 2.4 GHz, lo que le permite conectarse a redes Wi-Fi y utilizar protocolos como Wi-Fi 802.11b/g/n.

3. Memoria: Dispone de 2MB de memoria flash integrada para almacenar programas y datos.

4. Interfaces de hardware: La Pico W cuenta con una variedad de interfaces de hardware, incluyendo:

    - GPIO: Ofrece 26 pines GPIO programables, que permiten la conexión de dispositivos externos y la interacción con ellos.
    - I2C: Soporta el protocolo de comunicación I2C, que permite la conexión de periféricos y sensores.
    - SPI: Proporciona una interfaz SPI (Serial Peripheral Interface) para la comunicación con otros dispositivos compatibles con SPI.
    - UART: Incluye una interfaz UART (Universal Asynchronous Receiver-Transmitter) para la comunicación serial.
    - PWM: Ofrece canales PWM (Pulse Width Modulation) para el control de actuadores como motores y servomotores.

5. Alimentación: Se alimenta a través de un conector micro-USB o mediante pines GPIO específicos.

6. Programación: Puede ser programada utilizando el lenguaje de programación MicroPython, así como C/C++ utilizando el entorno de desarrollo integrado (IDE) oficial o herramientas de desarrollo de terceros.

7. Tamaño y factor de forma: Tiene un tamaño compacto y utiliza un factor de forma similar a una placa de desarrollo estándar, lo que facilita su integración en proyectos y prototipos.

Estas son solo algunas de las características principales de la Raspberry Pi Pico W. La placa ofrece una amplia flexibilidad y capacidades para el desarrollo de proyectos de IoT y electrónica, combinando un microcontrolador potente y una conectividad inalámbrica.

## Esta es la distribución de los pines de la raspberry Pi Pico W:

![image](https://github.com/Autumnland/Raspberry-Pi-Pico-W/assets/112134604/0044dd7f-0c1d-4017-b464-33d4fbd8daad)


## Cual es la IDE que usaremos?

Es Thonny.

<p align="center"><img src="https://github.com/Autumnland/Raspberry-Pi-Pico-W/assets/112134604/b33aaf4e-bbee-4b9d-a95b-b4a3201550de" align="center" width="300" height="300"/></p>

## Donde lo puedo descargar?

Este es el enlace que te envia a su pagina: <A HREF="https://thonny.org/"> https://thonny.org/ </A>

## Como se usa?

Una vez que entramos debemos nos dirigimos a la parte inferior de la derecha y observaremos que dice python 3 local.

<p align="center"><img src="https://github.com/Autumnland/Raspberry-Pi-Pico-W/assets/112134604/6f8bae85-e6ef-4741-9e15-583ba4ce547c" align="center" width="600" height="600"/></p>

Damos un clic ahi y nos mostrara si queremos instalar MycroPython o CircuitPython.

<p align="center"><img src="https://github.com/Autumnland/Raspberry-Pi-Pico-W/assets/112134604/9a2f32f4-9beb-4564-9e76-905b4f5f4037" align="center" width="245" height="99"/></p>

Daremos clic a la que deseamos y seleccionamos lo siguiente (en mi caso mostrare Micropython pero es el mismo procedimiento para CircuitPython):

<p align="center"><img src="https://github.com/Autumnland/Raspberry-Pi-Pico-W/assets/112134604/17ede04b-8f60-48a7-aef4-18dcb5c23af2" align="center" width="600" height="600"/></p>

Ya seleccionado le damos a instalar, cuando acabe el proceso de instalacion nos mostrara lo siguiente:

<p align="center"><img src="https://github.com/Autumnland/Raspberry-Pi-Pico-W/assets/112134604/f429d67b-20b9-4556-aebd-58889f1da8b7" align="center" width="600" height="600"/></p>

Una vez que nos aparezca asi ya podemos empezan a hacer uso de la IDE.

## Donde puedo instalar las librerias si es que las necesito?

Nota importante: recuerda haber seleccionado tu raspberry pi pico antes de empezar a hacer esto ya que sino no te aparecera igual a como se muestran en los siguientes pasos, para seleccionarla te diriges a la parte inferior derecha, como si fueras a instalar Micropython pero ahora te mostrara la pico y en que puerto se encuentra.

Te aparecera algo asi:

<p align="center"><img src="https://github.com/Autumnland/Raspberry-Pi-Pico-W/assets/112134604/8d2f69e8-7e2d-45dc-a214-8147743f33a2" align="center" width="250" height="99"/></p>

En la parte superior central podemos encontrar el apartado de herramientas, daremos clic ahi.

<p align="center"><img src="https://github.com/Autumnland/Raspberry-Pi-Pico-W/assets/112134604/bf91445a-45d6-4403-aa9c-db911050f075" align="center" width="600" height="600"/></p>

Una vez que dimos clic nos aparecera lo siguiente:

<p align="center"><img src="https://github.com/Autumnland/Raspberry-Pi-Pico-W/assets/112134604/e84c57c0-a7b2-41d6-a432-c2deaf1831c5" align="center" width="270" height="146"/></p>

Solo damos clic en gestionar paquetes y nos aparecera lo siguiente:

<p align="center"><img src="https://github.com/Autumnland/Raspberry-Pi-Pico-W/assets/112134604/093f7d2c-7b12-4af1-bae1-bfbcd8132f48" align="center" width="600" height="600"/></p>

Ahi es donde nosotros podemos empezar a buscar las librerias necesarias paara hacer uso de nuestros programas.
