# Raspberry Pi Code CanSat 2023-2024
import digitalio
import board
import time
# import analogio
import mf52
# import busio
# import adafruit_bmp280
# import adafruit_rfm9x
# import radio
# import bmp280

# packet_count = 0

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

print("Hello world")

while True:
    led.value = True
    print(led.value)
    time.sleep(1)

# adc = analogio.AnalogIn(board.GP26)

# adc_raw = adc.value
# print(f"Raw ADC value: {adc_raw}")

# therm_r = (adc_v * 10000)/(3.3 - adc_v)     #10000 is R1, 3.3 is ADC_VREF

# math.log()
# print(f"{temperature}")


# print("raw = {:5d} volts = {:5.2f} temp = {:5.2f}".format(adc_raw, adc_voltage, temperature))


# i2c = busio.I2C(scl = board.GP15, sda = board.GP14)
# bmp280_sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)
# bmp280_sensor.temperature

# def read_temperature():
#     return bmp280_sensor.temperature

# cansat_temperature = bmp280.read_temperature()
# print(cansat_temperature)

# print("T: {:.3f} P: {:.2f}".format(cansat_temperature, cansat_pressure))

# spi = busio.SPI(clock=board.GP2, MOSI=board.GP3, MISO=board.GP4)

# cs = digitalio.DigitalInOut(board.GP6)
# reset = digitalio.DigitalInOut(board.GP7)

# rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.0)

# print("RFM9x radio ready")

# def send(message):
#     rfm9x.send(message)

# radio.send("Test from CanSat!")
# print("Radio message sent")

# radio.send("[CANSAT NAME] Temperature {:.2f} Pressure {:.0f}".format(room_temp, room_pressure))

# def try_read():
#     return rfm9x.receive(timeout=1.0)

# def rssi():
#     return rfm9x.rssi

# radio_message = radio.try_read()

# if radio_message is not None:
#     print("Radio RX {:d} {:s}".format(packet_count, str(radio_message, 'ascii')))
#     print("RSSI: {:3d}db".format(radio.rssi()))
#     packet_count = packet_count + 1
