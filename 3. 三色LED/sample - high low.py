import RPi.GPIO as GPIO
import time

pin_red = 5
pin_green = 6
pin_blue = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_red, GPIO.OUT)
GPIO.setup(pin_green, GPIO.OUT)
GPIO.setup(pin_blue, GPIO.OUT)


def destroy():
    GPIO.output(pin_red, GPIO.LOW)
    GPIO.output(pin_green, GPIO.LOW)
    GPIO.output(pin_blue, GPIO.LOW)
    GPIO.cleanup()


def show():
    while True:
        # 亮紅， 暗綠和藍 = 紅
        GPIO.output(pin_red, GPIO.HIGH)
        GPIO.output(pin_green, GPIO.LOW)
        GPIO.output(pin_blue, GPIO.LOW)
        time.sleep(1)

        # 亮紅和綠， 暗藍 = 黃
        GPIO.output(pin_red, GPIO.HIGH)
        GPIO.output(pin_green, GPIO.HIGH)
        GPIO.output(pin_blue, GPIO.LOW)
        time.sleep(1)

        # 亮綠， 暗紅和藍 = 綠
        GPIO.output(pin_red, GPIO.LOW)
        GPIO.output(pin_green, GPIO.HIGH)
        GPIO.output(pin_blue, GPIO.LOW)
        time.sleep(1)

        # 亮綠和藍， 暗紅 = 淺藍？
        GPIO.output(pin_red, GPIO.LOW)
        GPIO.output(pin_green, GPIO.HIGH)
        GPIO.output(pin_blue, GPIO.HIGH)
        time.sleep(1)

        # 亮藍， 暗綠和紅 = 藍
        GPIO.output(pin_red, GPIO.LOW)
        GPIO.output(pin_green, GPIO.LOW)
        GPIO.output(pin_blue, GPIO.HIGH)
        time.sleep(1)

        # 亮紅和藍， 暗綠 = 粉紅
        GPIO.output(pin_red, GPIO.HIGH)
        GPIO.output(pin_green, GPIO.LOW)
        GPIO.output(pin_blue, GPIO.HIGH)
        time.sleep(1)

        # 亮紅和藍和綠 = 白
        GPIO.output(pin_red, GPIO.HIGH)
        GPIO.output(pin_green, GPIO.HIGH)
        GPIO.output(pin_blue, GPIO.HIGH)
        time.sleep(1)

        # 暗紅和藍和綠 = 沒亮燈
        GPIO.output(pin_red, GPIO.LOW)
        GPIO.output(pin_green, GPIO.LOW)
        GPIO.output(pin_blue, GPIO.LOW)
        time.sleep(1)


if __name__ == "__main__":
    try:
        show()
    except KeyboardInterrupt:
        destroy()
