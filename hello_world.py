import machine
import time

def main():
  led = machine.Pin("LED", machine.Pin.OUT)

  while True:
    led.off()
    print("OFF")
    time.sleep(1)

    led.on()
    print("ON")
    time.sleep(1)

if __name__=="__main__":
  main()
