# Luminea-WiFi-Power-Outlet
How to flash Luminea WiFi Power Outlet 

I bought an WiFi Power Outlet by Pearl, it is realy small and compact.
but it can only be operated via the internet.But I needed an Wifi power Outlet
for my own purposes with micropython.

First step: open the housing with the four screws on the back.
Now you see the PCB.

see plug01.jpg

# Warning do not operate on mains voltage

in order to remove the board two solder joints have to be removed L-in and N-in
next to the relais.

Next step: in order to flash the ESP we have to solder the wires
Vcc, Ground, Tx, Rx and IO 0 for FlashMode

see plug02.jpg

To flash the ESP :
we have to use a separate power supply with 3.3 Volt with at least 200 mA
and we need a USB to UART Adapter.Be careful with the Chinese PL230x, you need a special driver.
But ok, to flash an ESP  many tutorial are in the net.

I used uPyCraft and the latest micropython ESP8266 bin to flash.
Don't forget to bring IO 0 to ground befor power on the ESP to switch to flash mode!


# Description of the PIN IO

its late will be continued soon ....

