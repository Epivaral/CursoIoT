from machine import Pin, I2C
from time import sleep
import ssd1306

#-----------------
import network


wlan = network.WLAN(network.STA_IF) 
wlan.active(True)
listado = wlan.scan()
print('Redes detectadas: ', len(listado))
#---------------------

i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


def despliegaTexto(ssid):
    oled.fill(0)
    oled.text('Red '+str(i+1) , 0, 5)
    oled.text(ssid, 0, 20)
    oled.show()
    
i = 0

def cambia_estado(pin):
    sleep(0.5)
    global i
    if i>=len(listado)-1:
        i=0
    else:
        i = i+1

pir = Pin(14, Pin.IN, Pin.PULL_UP)

pir.irq(cambia_estado,Pin.IRQ_FALLING)

while True:
    despliegaTexto(listado[i][0])
    