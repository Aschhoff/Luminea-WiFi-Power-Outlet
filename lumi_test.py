import machine
from machine import Pin
import time

led = Pin(2,Pin.OUT)    # LED
rel = Pin(15,Pin.OUT)   # select for current or voltage
sel = Pin(12,Pin.OUT)   # current or voltage
pow = Pin(5,Pin.IN)     # Energy
amp = Pin(14,Pin.IN)    # current or voltage
tast = Pin(13,Pin.IN)   # Front button

sel.value(1)            # Select to 1 => Pin 14 Current

def power():            # Energy measurement
    timeout=0
    leist=0
    korr=2              # adjust value
    
    while timeout < 10000:
        timeout+=1
        puls1=pow.value()
        time.sleep_us(100)
        puls2=pow.value()
        if puls1 > puls2:   # wait for falling edge
            leist= machine.time_pulse_us(pow,0,1000000) # Pulse lenght in us
            break
    if leist >0:
        leist=int(korr*(1000000/leist))  # 100000 ca 10Watt, korr 
    return(leist)

def switch(bef):
    if bef==1:
        rel.value(1)    # Relais  On
        led.value(0)    # Led  On       
        on=power()      # measure energy
        if on > 0:      # is power realy on
            return("ON OK")
        else:
            return("ON ERR")
        
    if bef==0:
        rel.value(0)    # Relais  Off
        led.value(1)    # Led  off      
        off=power()
        if off == 0:    # is power realy off
            return("OFF OK")
        else:
            return("OFF ERR")       

def button(s):
    global toggle
    ta=time.time()
    time.sleep_ms(50)
    st=tast.value()     # Debounce
    if st == 1: return
    while st == 0:      # get time till button realeased
        st=tast.value()
        te=time.time()
        time.sleep_ms(100)
    if te-ta > 5:
        print("Button long pressed!")
        # file delete reset... do something
    else:
        print("Button short pressed")
        # toggle power
        toggle=1-toggle
        ok=switch(toggle)   # switch Relais
        print(ok)
        

toggle=0
tast.irq(trigger=Pin.IRQ_FALLING, handler=button) # IRQ when button pressed
while True:
    toggle=1-toggle
    switch(toggle)
    print("Energy= ",power())
    time.sleep(5)
 
