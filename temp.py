import ds18x20
import machine
import onewire
import time

from machine import Pin

ow = onewire.OneWire(Pin(27))
led = Pin("LED", Pin.OUT)

ds = ds18x20.DS18X20(ow)

addresses = ds.scan()
print(addresses)

time.sleep(1)

def read_temp(ds, addr):
    ds.convert_temp()
    value = ds.read_temp(addr)

    print(f"temp: {value}")
    led.toggle()


while True:
    read_temp(ds, addresses[0])

    time.sleep(5)
