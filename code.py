import digitalio
import board
import time
import mf52

led = digitalio. DigitalInOut(board.LED)
led.direction = digitalio. Direction.OUTPUT

while True:
    led.value = not led.value
    time.sleep(1)
    mf52.read_temperature()

