
def connect():

    import network
    import time


    ip        = "192.168.10.201" # only for fixed IP
    subnet    = '255.255.255.0'
    gateway   = '192.168.10.1'
    dns       = '8.8.8.8'


    ssid      = "YourSSID"
    password  =  "Your Password"


    station = network.WLAN(network.STA_IF)

    if station.isconnected() == True:
        print("Already connected")
        return


    station.active(True)

    #station.ifconfig((ip,subnet,gateway,dns))  # activate for fixed IP


    station.connect(ssid,password)

    station.isconnected()

    while not station.isconnected():
        time.sleep(0.2)
        print("*")
        #pass

    print("Wifi OK!")

    print(station.ifconfig())


 


def disconnect():


    import network


    station = network.WLAN(network.STA_IF)


    station.disconnect()


    station.active(False)


    print("WiFi Off!")



