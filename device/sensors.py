import dht
import ds18x20
import onewire
import time

from machine import I2C, Pin

import scd4x


def main():
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

    while True:
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

        print("###############################")
        print(f"DS1820 Temperature:\t{ow_temp}")
        print(f"DHT22 Temperature:\t{dht_temp}")
        print(f"SCD41 Temperature:\t{scd_temp}")
        print("---")
        print(f"DHT22 humidity:\t{dht_humidity}")
        print(f"SCD41 humidity:\t{scd_humidity}")
        print("---")
        print(f"CO2 ppm level:\t\t{scd_co2_ppm_level}")
        led.toggle()

        time.sleep(15)


if __name__ == "__main__":
    main()
