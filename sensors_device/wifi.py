import network
import secrets
from time import sleep


def wifi_init():
    print('Connecting to WiFi Network...')

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    print('Waiting for wifi chip to power up...')
    sleep(3)

    wlan.connect(secrets.SSID, secrets.PASSWORD)
    print('Waiting for access point to log us in.')
    sleep(3)

    if wlan.isconnected():
        print('Success! We have connected to your access point!')
        print('Try to ping the device at', wlan.ifconfig()[0])
    else:
        print('Failure! We have not connected to your access point!  Check your secrets.py file for errors.')

    return wlan

if __name__ == '__main__':
    wifi_init()
