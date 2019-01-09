# Luminea-WiFi-Power-Outlet
How to flash Luminea WiFi Power Outlet 

I bought an WiFi Power Outlet by Pearl, it is realy small and compact.
but it can only be operated via the internet.But I needed an Wifi power Outlet
for my own purposes with micropython.

First step: open the housing with the four screws on the back.
Now you see the PCB.

see plug01.jpg

## Warning do not operate on mains voltage !!!

in order to remove the board two solder joints have to be removed L-in and N-in
next to the relais.

Next step: in order to flash the ESP we have to solder the wires
Vcc, Ground, Tx, Rx and IO 0 for FlashMode

see plug02.jpg

To flash the ESP :
we have to use a separate power supply with 3.3 Volt with at least 200 mA
and we need a USB to UART Adapter.Be careful with the Chinese PL230x, you need a special driver.
But ok, to flash an ESP  many tutorial you will find in the net.

I used uPyCraft and the latest micropython ESP8266.bin to flash.
Don't forget to bring IO 0 to ground befor power on the ESP, to switch to flash mode!
Sometimes i needed several tries zu get in erase/flash mode. I don't know, maybe is it the cheep
UART adapter.


## Description of the PIN I/O

I use the PIN numbering from micropython:

- PIN  2  Output   switch on / off the green LED
- PIN 15  Output   switch the Power Relais
- PIN 12  Output   wired to the Select Input of  HLW 8012
- PIN 05  Input    wired to the CF Output of  HLW 8012
- PIN 14  Input    wired to the CF1 Output of  HLW 8012
- PIN 13  Input    state of the fronttaster

## Description of the HLW 8012

HLW 8012 is an special ic for measuring the voltage, current and power.
It convert a analog voltage to a square wave signal on CF and CF1 
- CF is the power consumption 1Hz ~ 12 Watt, 10Hz ~ 120 Watt ....
- CF1 is either voltage (1) or current (0) dependent on the level on the PIN 12 (Select)

A simple example is given by lumi_test.py

### to test your program you must disconnect all wires!

The best solution is to operate the WiFi switch over the air!
In boot.py and wifi.py configure your WiFi settings and enable the WebREPL
I tried out the WebREPL and a simple FTP Server, it works fine


viel Spass
**Detlev Aschhoff
info@vmais.de**
