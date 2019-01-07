import machine
from machine import Pin
import time

led = Pin(2,Pin.OUT)
rel = Pin(15,Pin.OUT)
sel = Pin(12,Pin.OUT)
pow = Pin(5,Pin.IN)
amp = Pin(14,Pin.IN)
tast = Pin(13,Pin.IN)

sel.value(1)   # Select auf 1 => Pin 14 Strom messen


def power():
    timeout=0
    cf=0
    leist=0
    while timeout < 10000:
        timeout+=1
        puls1=pow.value()
        time.sleep(0.001)
        puls2=pow.value()
        if puls1 > puls2:
            leist= machine.time_pulse_us(pow,0,10000000)
            break
    if leist >0:
        leist=int(1000000/leist)  # 100000 ca 10Watt
    return(leist)

def switch(bef):
    if bef=="ON":
        rel.value(1)   # Relais  AN
        #time.sleep(0.5)
        on=power()
        if on > 0:
            return("ON OK")
        else:
            return("ON ERR")
        
    if bef=="OFF":
        rel.value(0)   # Relais  Aus
        #time.sleep(0.5)
        off=power()
        if off == 0:
            return("OFF OK")
        else:
            return("OFF ERR")       

