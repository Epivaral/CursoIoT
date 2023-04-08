# Curso IoT
Material complementario del curso: INTRODUCCIÓN A IOT, ALMACENAMIENTO EN LA NUBE Y ANÁLISIS DE DATA

<img src="/img/d1.png" width="300">

 <img src="/img/ytIcon.png" width="100">
 Curso disponible aqui: <a href="https://www.youtube.com/playlist?list=PL22a5HPkoCQb2UCUi800SvnNu_HrKVk-G">Playlist Youtube</a> 
 
 ---
## Hardware

Modulos IoT para este curso, no necesitas todos, con un NodeMCU es mas que suficiente: 

- <a href="https://www.amazon.com/HiLetgo-Internet-Development-Wireless-Micropython/dp/B081CSJV2V">NodeMCU ESP8266</a>
- <a href="https://www.sparkfun.com/products/13711">SparkFun ESP8266 Thing - Dev Board</a>
- <a href="https://www.amazon.com/SongHe-Development-Dual-Mode-Bluetooth-Antenna/dp/B08246MCL5">ESP32</a>
- <a href="https://www.raspberrypi.org/products/raspberry-pi-4-model-b/">Raspberry Pi 3 o 4 (preferiblemente 4)</a>
- Distintos tipos de <a href="https://www.amazon.com/HiLetgo-Sensors-Assortment-Raspberry-Projects/dp/B01N5910XS">sensores</a> y <a href="https://www.amazon.com/Miuzei-Helicopter-Airplane-Remote-Control/dp/B07NSVKZP7">actuadores</a>

## Software

- <a href="https://azure.microsoft.com/en-us/free/">Cuenta de Azure</a>
- <a href="https://powerbi.microsoft.com/en-us/">PowerBI</a>
- <a href="https://www.arduino.cc/en/software">Arduino IDE</a>
- <a href="https://micropython.org/">MicroPython</a>
- <a href="https://thonny.org/">Thonny</a>
- <a href="https://code.visualstudio.com/">VSCode</a>
- <a href="https://visualstudio.microsoft.com/">Visual Studio</a>

 ---
 ## Modulo 1: Conceptos básicos
- <a href="https://www.youtube.com/watch?v=HuZQsPen9S4">Explicar qué es IoT y cómo puede ayudarnos.</a>
  - Conceptos básicos de hardware: explicar que es y cómo funciona el módulo que utilizamos
  - Conceptos básicos de los sensores y actuadores: cómo funciona un sensor y cómo podemos medirlos
  - Conceptos básicos del software: qué es un servicio en la nube y los servicios que utilizamos (base de datos, programación, análisis de datos, visualización de datos) y cómo podemos comunicarnos con un dispositivo.

## Módulo 2: Obtención de datos
Material complementario <a href="/Modulo 2/">Aqui ⬇</a>
- <a href="https://www.youtube.com/watch?v=DoEXbU-nT84">Configuración y programación básica de nuestro dispositivo ESP8266</a>
- Ejemplo simple sobre cómo conectar distintos sensores y actuadores:
  - <a href="https://www.youtube.com/watch?v=zQ4-adT0BSA">Encender y apagar LED</a>
  - <a href="https://www.youtube.com/watch?v=ASPIfFUboGs">Push Button</a>
  - <a href="https://www.youtube.com/watch?v=4Zcyb7DkYb8">Pulse Width Modulation</a>
  - <a href="https://www.youtube.com/watch?v=EF4Zmd-J-as">ADC</a>
  - <a href="https://www.youtube.com/watch?v=Pde4dbyZxSI">Sensor distancia (HC-SR04)</a>
  - <a href="https://www.youtube.com/watch?v=UKmICfz_fGk">Sensor humedad/temperatura (DHT22)</a>
  - <a href="https://www.youtube.com/watch?v=NvnP0YtsOvw">Motor DC (Driver TB6612FNG)</a>
  - <a href="https://www.youtube.com/watch?v=pxHsRv2epHE">Sensor efecto hall (Interrupts)</a>
  - <a href="https://www.youtube.com/watch?v=9Lu98LXeJOA">Servo</a>
  - <a href="https://www.youtube.com/watch?v=6NS6sh36p_A">Pantalla OLED (I2C)</a>

## Módulo 3: Habilitación de un dispositivo IoT para usar servicios en la nube
Material complementario <a href="/Modulo 3/">Aqui ⬇</a>
- <a href="https://www.youtube.com/watch?v=0CmfkGMnhA4">Introducción a MicroPython</a>
  - Configurar nuestro dispositivo para usar Micropython
- Configuración de nuestro dispositivo IoT para leer datos (librería WIFI)
  - <a href="https://www.youtube.com/watch?v=t-UXmWUz__4">Network Scan</a>
  - <a href="https://www.youtube.com/watch?v=sqay7rE_KRw">Modo Station</a>
  - <a href="https://www.youtube.com/watch?v=PGnoUtts3Ok">Modo Cliente</a>
  - <a href="https://www.youtube.com/watch?v=-z6-nZJdeBE">Modo Access Point</a>
  - <a href="https://www.youtube.com/watch?v=HjbEAuQXr1M">Web Server y utilización de Angular para interfaz de usuario enriquecida</a>
  - <a href="https://www.youtube.com/watch?v=RrHxOLSw3Jg">Desplegar lectura de sensores en web server</a>
  - <a href="https://www.youtube.com/watch?v=dEINx31FY00">Controlar un servo en WebServer</a>
- Comunicar nuestro dispositivo IoT a los servicios en la nube (Utilizando servicios de Azure)
  - <a href="https://www.youtube.com/watch?v=akre5_b_Eys">Conectarnos a Azure IoT Hub</a>
  - <a href="https://www.youtube.com/watch?v=BEc8bBKQDgU">Enviar telemetría a Azure IoT Hub</a>
  - <a href="https://www.youtube.com/watch?v=g5eH2h7WpdI">Recibir comandos desde Azure IoT Hub</a>

## Módulo 4: Análisis de datos
Material complementario <a href="/Modulo 4/">Aqui ⬇</a>
- <a href="https://www.youtube.com/watch?v=FtnQwAeIObw">Uso de procesos ETL para la limpieza y preparación de datos (servicios Azure)</a>
- <a href="https://www.youtube.com/watch?v=Wg2sIpVqDMo">Creación de un panel interactivo para visualizar los datos capturados (utilizando PowerBI)</a>

## Módulo 5: Retroalimentación del sistema
Material complementario <a href="/Modulo 5/">Aqui ⬇</a>
- <a href="https://www.youtube.com/watch?v=tObz4KHemeo">Configuración de un simple sistema sensor-actuador</a>
- <a href="https://www.youtube.com/watch?v=U1Ahw6HjE5s">Configuración de un sistema simple de registro y respuesta de datos</a>

## Modulo 6: Otras configuraciones
Material complementario <a href="/Modulo 6/">Aqui ⬇</a>
- <a href="https://www.youtube.com/watch?v=sraDWQduinE">Sleep</a>
- <a href="https://www.youtube.com/watch?v=1ezEOdePxiU">Persistir data</a>
- <a href="https://www.youtube.com/watch?v=_YsNYwx1vgc">OTA (over the air updates)</a>
- <a href="https://www.youtube.com/watch?v=xAELw8mDLFM">Otros boards mas potentes</a>
  - ESP32
  - Raspberry PI

## Módulo 7: Aplicacion real
- Oxímetro digital capaz de medir el oxígeno en la sangre por medio del sensor max30102 y un ESP 32.
  - Lista de posibles funcionalidades:
    - Diseño para ser portátil, optimizar el uso de batería siempre que sea posible
    - Opción a conexión wifi, si no se tiene una red cerca, guardar mediciones en la memoria FLASH
    - Control web con sistema de alarma en caso de que no se haya hecho medición en N horas
