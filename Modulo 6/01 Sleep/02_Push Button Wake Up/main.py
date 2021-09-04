import machine
from machine import Pin, I2C
from time import sleep
import ssd1306
import utime


i2c = I2C(scl=Pin(5), sda=Pin(4))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


def mensaje_despertar():
    oled.fill(0)
    oled.text('Desperte!',0,1)
    oled.show()
    utime.sleep(5)


# codigo tomado de: https://docs.micropython.org/en/latest/esp8266/quickref.html#deep-sleep-mode
def dormir(t):
    
    
    # configure RTC.ALARM0 to be able to wake the device
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

    if machine.reset_cause() == machine.DEEPSLEEP_RESET:
      mensaje_despertar()

    # set RTC.ALARM0 to fire after X milliseconds (waking the device)
    rtc.alarm(rtc.ALARM0, t)

    oled.fill(0)
    oled.text('Deep Sleep...',0,30)
    oled.show()

    # put the device to sleep
    machine.deepsleep()
  


# dormir por 1 segundo
dormir(1000)
