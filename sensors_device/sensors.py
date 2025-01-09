import dht
import ds18x20
import onewire
import time

from machine import I2C, Pin

import requests
import scd4x

from secrets import API_KEY
from wifi import wifi_init


API_URL = 'http://192.168.5.100:8000/sensors'
PING_URL = 'http://192.168.5.100:8000/ping'

headers_get = {
    'X-API-Key': API_KEY
}

headers_post = {
    'Accept:': 'application/json',
    'Content-Type': 'application/json',
    'X-API-Key': API_KEY
}


def setup_and_test_sensors():
    # I2C sensors setup
    i2c = I2C(id=0, scl=Pin(9), sda=Pin(8), freq=100000)  # on Arduino Nano RP2040 Connect tested
    scd = scd4x.SCD4X(i2c)

    # 1Wire sensor setup
    ow = onewire.OneWire(Pin(27))
    ds = ds18x20.DS18X20(ow)

    # DHT22 sensor setup
    dht_sensor = dht.DHT22(Pin(17))

    led = Pin("LED", Pin.OUT)

    # I2C test
    i2c_scan_result = i2c.scan()
    print(f"I2C devices: {i2c_scan_result}")

    # 1Wire test
    ow_scan_result = ds.scan()
    print(f"OW devices: {ow_scan_result}")
    
    time.sleep(2)

    scd.start_periodic_measurement()
    time.sleep(5)

    ds1820_addr = ow_scan_result[0]
    ds.convert_temp()

    return scd, ds, ds1820_addr, dht_sensor, led


def main():
    wifi_init()

    r = requests.get(PING_URL, headers=headers_get)
    print(f"HTTP conn status code: {r.status_code}")
    print(f"HTTP conn response: {r.json()}")
    r.close()

    scd, ds, ds1820_addr, dht_sensor, led = setup_and_test_sensors()

    while True:
        led.on()

        dht_temp = None
        dht_humidity = None
        ow_temp = None
        scd_temp = None
        scd_humidity = None
        scd_co2_ppm_level = None

        # SCD
        if scd.data_ready:
            scd_temp = scd.temperature
            scd_humidity = scd.relative_humidity
            scd_co2_ppm_level = scd.CO2

        # 1Wire
        ds.convert_temp()
        ow_temp = ds.read_temp(ds1820_addr)

        # DHT22
        dht_sensor.measure()
        dht_humidity = dht_sensor.humidity()
        dht_temp = dht_sensor.temperature()

        data = [
            {
                "regname": "ow_temp",
                "value": str(ow_temp),
                "dt": "2025-01-09T11:22:33"
            },
            {
                "regname": "dht_temp",
                "value": str(dht_temp),
                "dt": "2025-01-09T11:22:33"
            },
            {
                "regname": "scd_temp",
                "value": str(scd_temp),
                "dt": "2025-01-09T11:22:33"
            },
            {
                "regname": "dht_humidity",
                "value": str(dht_humidity),
                "dt": "2025-01-09T11:22:33"
            },
            {
                "regname": "scd_humidity",
                "value": str(scd_humidity),
                "dt": "2025-01-09T11:22:33"
            },
            {
                "regname": "scd_co2_ppm_level",
                "value": str(scd_co2_ppm_level),
                "dt": "2025-01-09T11:22:33"
            }
        ]

        for i in data:
            print(i)
        try:
            r = requests.post(API_URL, headers=headers_post, json=data, timeout=5)
            print(f"POST status code: {r.status_code}")
            r.close()
        except OSError as e:
            print(f"POST failure: {str(e)}")

        led.off()

        time.sleep(20)


if __name__ == "__main__":
    main()
