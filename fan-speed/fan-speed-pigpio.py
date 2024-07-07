import pigpio
from time import sleep

# The pin that the fan is connected to
FAN_PIN = 19

# Create a pigpio instance
pi = pigpio.pi()

try:
    while True:
        # Gradually increase the fan speed from 0% to 100%
        for speed in range(0, 101):
            pi.set_PWM_dutycycle(FAN_PIN, speed)
            print(f"Fan speed: {speed}%")  # Print the current fan speed
            sleep(0.1)

        # Gradually decrease the fan speed from 100% to 0%
        for speed in range(100, -1, -1):
            pi.set_PWM_dutycycle(FAN_PIN, speed)
            print(f"Fan speed: {speed}%")  # Print the current fan speed
            sleep(0.1)
except KeyboardInterrupt:
    pass

# Stop the PWM signal
pi.set_PWM_dutycycle(FAN_PIN, 0)
pi.stop()