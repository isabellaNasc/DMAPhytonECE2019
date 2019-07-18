###traffic_light

from gpiozero import LED
from time import sleep

led1= LED(4)
led2= LED(17)
led3= LED(22)

led1.on()
sleep(5)
led1.off()
led2.on()
sleep(5)
led2.off()
led3.on()
sleep(5)
led3.off()
