import RPi.GPIO as GPIO
import time

pin_red = 5
pin_yellow = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_red, GPIO.OUT)
GPIO.setup(pin_yellow, GPIO.OUT)
pwm_red = GPIO.PWM(pin_red, 100)  # 100Hz frequency
pwm_yellow = GPIO.PWM(pin_yellow, 100)  # 100Hz frequency
dc = 0
delaySec = 0.1
pwm_red.start(dc)
pwm_yellow.start(dc)


def destroy():
    pwm_red.stop()
    pwm_yellow.stop()
    GPIO.output(pin_red, GPIO.LOW)
    GPIO.output(pin_yellow, GPIO.LOW)
    GPIO.cleanup()


def show():
    while True:
        # 逐漸亮紅
        for dc in range(0, 101, 5):
            pwm_red.ChangeDutyCycle(dc)
            time.sleep(delaySec)

        # 逐漸暗紅
        for dc in range(100, -5, -5):
            pwm_red.ChangeDutyCycle(dc)
            time.sleep(delaySec)

        # 逐漸亮黃
        for dc in range(0, 101, 5):
            pwm_yellow.ChangeDutyCycle(dc)
            time.sleep(delaySec)

        # 逐漸暗黃
        for dc in range(100, -5, -5):
            pwm_yellow.ChangeDutyCycle(dc)
            time.sleep(delaySec)

        # 逐漸亮黃 同時 逐漸暗紅
        for dc in range(0, 101, 5):
            pwm_yellow.ChangeDutyCycle(dc)
            pwm_red.ChangeDutyCycle(100-dc)
            time.sleep(delaySec)

        # 逐漸暗黃 同時 逐漸亮紅
        for dc in range(100, -5, -5):
            pwm_yellow.ChangeDutyCycle(dc)
            pwm_red.ChangeDutyCycle(100-dc)
            time.sleep(delaySec)

        # 逐漸暗紅 同時 逐漸亮黃
        for dc in range(100, -5, -5):
            pwm_red.ChangeDutyCycle(dc)
            pwm_yellow.ChangeDutyCycle(100-dc)
            time.sleep(delaySec)

        # 逐漸亮紅 同時 逐漸暗黃
        for dc in range(0, 101, 5):
            pwm_red.ChangeDutyCycle(dc)
            pwm_yellow.ChangeDutyCycle(100-dc)
            time.sleep(delaySec)


if __name__ == "__main__":
    try:
        show()
    except KeyboardInterrupt:
        destroy()
