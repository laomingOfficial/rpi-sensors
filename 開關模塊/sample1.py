import RPi.GPIO as GPIO
import time


pin_button = 19
pin_led = 21
delaySec = 0.1

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_button, GPIO.IN)
GPIO.setup(pin_led, GPIO.OUT)


def destroy():
    GPIO.output(pin_led, GPIO.LOW)
    GPIO.cleanup()


def showResult():
    while True:
        input_result = GPIO.input(pin_button)
        GPIO.output(pin_led, input_result)
        print(input_result)
        time.sleep(delaySec)


if __name__ == "__main__":
    try:
        showResult()
    except KeyboardInterrupt:
        destroy()
