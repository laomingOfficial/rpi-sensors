import RPi.GPIO as GPIO
import time


pin_button = 19
pin_led = 21
delaySec = 0.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_button, GPIO.IN)
GPIO.setup(pin_led, GPIO.OUT)


def destroy():
    GPIO.output(pin_led, GPIO.LOW)
    GPIO.cleanup()


def showResult():
    ledMode = False
    while True:
        input_result = GPIO.input(pin_button)
        if input_result == True:
            ledMode = not ledMode
            print(ledMode)
            GPIO.output(pin_led, ledMode)

        time.sleep(delaySec)


if __name__ == "__main__":
    try:
        showResult()
    except KeyboardInterrupt:
        destroy()
