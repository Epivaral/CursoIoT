import socket
from max30102 import MAX30102, MAX30105_PULSE_AMP_MEDIUM
import _thread
from machine import sleep, SoftI2C, Pin 
from utime import ticks_diff, ticks_us, ticks_ms

import spo2_algorithm
import telegram

import wifimgr
import ssd1306
import ntptime
import esp32
import uselect as select
import usocket

i2c = SoftI2C(sda=Pin(21),scl=Pin(22),freq=400000)

#----------------------------------------------
wake_1 = Pin(35,Pin.IN, None)


led = machine.Pin(2, machine.Pin.OUT)
led.value(1)

rtc = machine.RTC()
rtc.datetime((2022, 10, 21, 2, 10, 32, 36, 0))

wifi_switch = machine.Pin(13,Pin.IN, None)

habilitar_wifi = wifi_switch.value()

#----------------------------------------------

#guardar lecturas a archivo
def GuardaData(freq_,spo2_):
    (year, month, day, weekday, hours, minutes, seconds, subseconds) = rtc.datetime()
    fecha = str(year)+'-'+"{:02d}".format(month)+'-'+"{:02d}".format(day)+' '+"{:02d}".format(hours)+':'+"{:02d}".format(minutes)+':'+"{:02d}".format(seconds)
    a = open("data.dat", "a")
    a.write(freq_+'|'+spo2_+'|'+fecha+"\n")
    a.close()

#pantalla OLED
oled_width = 128
oled_height = 64

oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.init_display()

toggle = True

def despliegaMedida(spo2_,freq_, temp_, m):
    oled.fill(0)
    if (m):
        oled.text('Midiendo, espere...', 0, 0) 
    oled.text('SPO2: {:.2f}%'.format(spo2_), 0, 25)
    oled.text('BMP: {:.2f}'.format(freq_), 0, 35)
    oled.text('T: {:.0f} grados'.format(temp_), 0, 45)
    oled.show()
    
def despliegaTexto():
    oled.fill(0)
    oled.text('Presione dedo', 0, 30)
    oled.text('contra el sensor', 0, 40)
    oled.show()
    
    
def despliegaIP(IP):
    oled.fill(0)
    oled.text('Direccion IP', 0, 30)
    oled.text(IP, 0, 40)
    oled.show()
#FIN pantalla OLED


#----------------------------------------------
if habilitar_wifi == 1:
    # configuramos WLAN
    wlan = wifimgr.get_connection()
    telegram.send_to_telegram('Oximetro encendido')

    if wlan is None:
        while True:
            pass  # you shall not pass :D
        
led.value(0)
despliegaTexto()

#----------------------------------------------
# Pagina HTML
# ---------  webserver ------------
if habilitar_wifi == 1:
    #seteamos el RTC con NTP time
    # https://mpython.readthedocs.io/en/master/library/micropython/ntptime.html
    try:
        ntptime.settime()
    except OSError as e1:
        pass
                
    header = "HTTP/1.1 200 OK\n"
    header += "Content-Type: text/html\n"
    header += "Connection: close\n\n"

    # tomado de la documentacion
    # https://docs.micropython.org/en/latest/library/usocket.html#usocket.socket
    s = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
    s.bind(('', 8080)) #la direccion 
    s.listen(10)

    f = open("Pagina1.html", "r")
    pagina1 = f.read()
    f.close()

def CargaPagina1():
    retorno =""
    #non-blocking socket
    #https://docs.micropython.org/en/latest/library/select.html
    r, w, err = select.select((s,), (), (), 1)
    if r:
        for readable in r:
            conn, addr = s.accept()
            try:
                request = conn.recv(1024)  
                #Leemos el request del cliente
                retorno = str(request)
                
                # Mandamos el header y pagina web
                conn.send(header)
                B_ = []
                S_ = []
                t_ = []
                
                with open("data.dat") as file_in:
                    for line in file_in:
                        #lines.append(line)
                        tmpLine = line.replace("\n","").split("|")
                        B_.append(tmpLine[0])
                        S_.append(tmpLine[1])
                        t_.append("'"+tmpLine[2]+"'")
                
                pag = pagina1.replace("<BPM>",",".join(B_))
                pag = pag.replace("<SPO2>",",".join(S_))
                pag = pag.replace("<t>",",".join(t_))
                
                conn.sendall(pag)
                conn.close()
            except OSError as e:
                pass
    return retorno
    
#----------------------------------------------
#variables BMP
MAX_HISTORY = 10
history = []
beats_history = []
beat = False
beats = 0

#Variable SPo2
spo2 = 0
    

    
sensor = MAX30102(i2c=i2c) 

sensor.setup_sensor()
sensor.set_sample_rate(1000)
sensor.set_fifo_average(32)
sensor.set_active_leds_amplitude(MAX30105_PULSE_AMP_MEDIUM)
sensor.set_led_mode(2)
sleep(1)

t_start = ticks_us()  # Starting time of the acquisition  


def get_BPM_SPO2():
    #codigo basado en: https://youtu.be/FzkNvoLysQE
    
    #variables SPO2
    ir_data = [1,1,1,1,1,1,1,1,1,1]
    red_data = [1,1,1,1,1,1,1,1,1,1]

    # Set the size of the moving average filter
    window_size = 10
    max_samples = 50
    
    
    
    while True:
        global history
        global beats_history
        global beat
        global beats
        global t_start
        global spo2

        sensor.check()
        
        # Check if the storage contains available samples
        if sensor.available():
            # Access the storage FIFO and gather the readings (integers)
            red_reading = sensor.pop_red_from_storage()
            ir_reading = sensor.pop_ir_from_storage()
            
            red_data.append(red_reading)
            ir_data.append(ir_reading)
            
            if len(red_data) >= max_samples:
                # Delete old samples to keep the lists at "max_samples" samples
                red_data.pop(0)
                ir_data.pop(0)
            
            spo2 = spo2_algorithm.calculate_spo2(red_data, ir_data, window_size)        
            
            value = (red_reading+ir_reading)/2 #promedio de los 2 sensores
            
            history.append(value)
            # Get the tail, up to MAX_HISTORY length
            history = history[-MAX_HISTORY:]
            minima = 0
            maxima = 0
            threshold_on = 0
            threshold_off = 0

            minima, maxima = min(history), max(history)

            threshold_on = (minima + maxima * 3) // 4   # 3/4
            threshold_off = (minima + maxima) // 2      # 1/2
            
            
            if value > 1000:
                if not beat and value > threshold_on:
                    beat = True 
                    led.on()
                    
                    t_us = ticks_diff(ticks_us(), t_start)
                    t_s = t_us/1000000
                    f = 1/t_s
                
                    bpm = f * 60
                    
                    if bpm < 500:
                        t_start = ticks_us()
                        beats_history.append(bpm)                    
                        beats_history = beats_history[-MAX_HISTORY:] 
                        beats = round(sum(beats_history)/len(beats_history) ,2)
                        
                        
                if beat and value< threshold_off:
                    beat = False
                    led.off()
                
                
                
            else:
                if wake_1.value() !=1:
                    despliegaTexto()
                beats = 0.00
                led.off()


#Threads para calcular BPM y SPO2, se hace
# en threads porque los delays de otras tareas causan mediciones incorrectas

_thread.start_new_thread(get_BPM_SPO2, ())

delta5s = 0

#tratamos de que la primera lectura sea guardada en el archivo data.dat
# aun si solo se hace una lectura muy rapidamente antes del threshold (5 segundos)
t1 = 0

while True:
    try:
        if habilitar_wifi == 1:
            CargaPagina1()
        
        if(beats>50 and beats<180):
            
            despliegaMedida(spo2,beats, sensor.read_temperature(),False)
            delta5s = ticks_diff(ticks_ms(), t1)
            
            if(delta5s>5000):
                GuardaData(str(round(beats,2)),str(round(spo2,2))) #guardamos en el archivo
                t1 = ticks_ms()
                
        if(beats>30 and beats<50):
            despliegaMedida(spo2, beats, sensor.read_temperature(),True)
            
            
        while (wake_1.value() ==1 and habilitar_wifi == 1):
            #mientras se tenga presionado, desplegar IP
            despliegaIP(wlan.ifconfig()[0])
            
        
        
    except Exception as e:
        print(e)


