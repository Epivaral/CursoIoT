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
- Explicar qué es IoT y cómo puede ayudarnos.
- Conceptos básicos de hardware: explicar que es y cómo funciona el módulo que utilizamos
- Conceptos básicos de los sensores y actuadores: cómo funciona un sensor y cómo podemos medirlos
- Conceptos básicos del software: qué es un servicio en la nube y los servicios que utilizamos (base de datos, programación, análisis de datos, visualización de datos) y cómo podemos comunicarnos con un dispositivo.

## Módulo 2: Obtención de datos
- Configuración y programación básica de nuestro dispositivo ESP8266
- Ejemplo simple sobre cómo conectar distintos sensores y actuadores:
  - Encender y apagar LED
  - Push Button
  - Intensidad de LED (PWM)
  - LED RGB (PWM)
  - Potenciómetro (ADC)
  - Modulo Serial
  - Fotorresistencia (ADC)
  - Sensor distancia (HC-SR04)
  - Sensor humedad/temperatura (DHT22)
  - Motor DC (Driver TB6612FNG)
  - Buzzer (alertas auditivas)
  - Servo
  - Control temperatura análogo (TMP36)
  - Sensor efecto hall (Interrupts)
  - Pantalla OLED (I2C)

## Módulo 3: Habilitación de un dispositivo IoT para usar servicios en la nube
- Introducción a MicroPython
  - Configurar nuestro dispositivo para usar Micropython
- Configuración de nuestro dispositivo IoT para leer datos (librería WIFI)
  - Network Scan
  - Modo Station
  - Modo Cliente
  - Modo Access Point
  - Web Server y utilización de Angular para interfaz de usuario enriquecida
  - Desplegar lectura de sensores en web server
  - Controlar un servo en WebServer
- Comunicar nuestro dispositivo IoT a los servicios en la nube (Utilizando servicios de Azure)
  - Conectarnos a Azure IoT Hub
  - Enviar telemetría a Azure IoT Hub
  - Recibir comandos desde Azure IoT Hub

## Módulo 4: Análisis de datos
- Uso de procesos ETL para la limpieza y preparación de datos (servicios Azure)
- Creación de un panel interactivo para visualizar los datos capturados (utilizando PowerBI)

## Módulo 5: Retroalimentación del sistema
- Configuración de un simple sistema sensor-actuador
- Configuración de un sistema simple de registro y respuesta de datos

## Modulo 6: Otras configuraciones
- Sleep
- Persistir data
- OTA (over the air updates)
- Otros boards mas potentes
  - ESP32
  - Raspberry PI
- Dispositivos Edge (ejemplo utilizando Raspberry PI y ESP8266)
- Ejemplo real 1: Pronto
- Ejemplo real 2: Pronto
- Ejemplo real 3: monitor de calidad de aire para hogar (2 dispositivos)
  - Monitorear calidad de aire/temperatura/humedad
  - Encender/apagar cualquier maquinaria o equipo bajo niveles no adecuados
  - Un dispositivo monitorea el aire
  - Otro dispositivo se encarga de operar el equipo externo
  - Consola de operación disponible en la nube
  - Configuración de alertas

## Módulo 7: Escalado de nuestra aplicación IoT (modulo teórico)
- Que es una aplicación escalable
- Consideraciones para hacer aplicaciones escalables.
- Manejo de errores
- Seguridad de nuestros dispositivos
- Consideraciones de seguridad y privacidad de los datos recolectados.
- Mejores prácticas para optimizar rendimiento de nuestras soluciones IoT

