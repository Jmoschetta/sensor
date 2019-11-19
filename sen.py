#Declaramos las dependencias
from gpiozero import PWMLED, LED
import spidev
import time
import os
from time import sleep
#declaramos variables globales 
led = PWMLED(15)
led_azul = LED(14)
led_rojo = LED(15)
#declaramos la función para abrir el puesrto spi
spi = spidev.SpiDev()#declaramos el objeto 
spi.open(0,0)#SPIO
spi.max_speed_hz= 1000000#declaramos la velocidad de trasnmision 1Mhz

#declaracion de funciones
def leerCanal(canal):#recuerda que hablamos del canal del integrado
    adc = spi.xfer2([1, (8+canal)<<4,0]) 
    data = ((adc[1]&3) << 8) + adc[2]
    return data
def controlLed(leerSensor):
    if(leerSensor < 500 ):
        led.value = 1
    elif(leerSensor > 900 ):
        led.value = 0.5
    else:
        led.value = 0 

while True:
        
      
      
    
    led_rojo.on()
    sleep(1)
    led_rojo.off()
    sleep(1)
      print('Valor sensor {}'.format(leerSensor))
      