
import board

led = digitalio.DigitalInOut(board.GP25)

led.direction = digitalio.Direction.OUTPUT

led.value = True
print("working")
