import board
import analogio

adc = analogio.AnalogIn(board.GP26)

def read_temperature():
    adc_raw = adc.value
    print(f"Raw ADC value: {adc_raw}")
    ADC_VREF = 3.3
    ADC_MAX_RAW = 65536
    adcVoltage = adc_raw * ADC_VREF / ADC_MAX_RAW
    print(f"ADC Voltage: {adcVoltage}")
