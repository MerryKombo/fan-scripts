from gpiozero import PWMOutputDevice
from time import sleep

# The pin that the fan is connected to
FAN_PIN = 19

# Create a PWM device at the given pin with a frequency of 25Hz
fan = PWMOutputDevice(FAN_PIN, frequency=25)

try:
    while True:
        # Gradually increase the fan speed from 0% to 100%
        for speed in range(0, 101):
            fan.value = speed / 100.0
            print(f"Fan speed: {speed}%")  # Print the current fan speed
            sleep(0.1)

        # Gradually decrease the fan speed from 100% to 0%
        for speed in range(100, -1, -1):
            fan.value = speed / 100.0
            print(f"Fan speed: {speed}%")  # Print the current fan speed
            sleep(0.1)
except KeyboardInterrupt:
    pass

# The fan will stop automatically when the script exits