import RPi.GPIO as GPIO
import time

pin_red = 5
pin_yellow = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_red, GPIO.OUT)
GPIO.setup(pin_yellow, GPIO.OUT)


def destroy():
    GPIO.output(pin_red, GPIO.LOW)
    GPIO.output(pin_yellow, GPIO.LOW)
    GPIO.cleanup()


def show():
    while True:
        # 亮紅， 暗黃 = 紅
        GPIO.output(pin_red, GPIO.HIGH)
        GPIO.output(pin_yellow, GPIO.LOW)
        time.sleep(1)

        # 亮紅和黃 = 橙
        GPIO.output(pin_red, GPIO.HIGH)
        GPIO.output(pin_yellow, GPIO.HIGH)
        time.sleep(1)

        # 亮黃，暗紅 = 黃
        GPIO.output(pin_red, GPIO.LOW)
        GPIO.output(pin_yellow, GPIO.HIGH)
        time.sleep(1)

        # 暗紅和黃 = 沒亮燈
        GPIO.output(pin_red, GPIO.LOW)
        GPIO.output(pin_yellow, GPIO.LOW)
        time.sleep(1)


if __name__ == "__main__":
    try:
        show()
    except KeyboardInterrupt:
        destroy()
