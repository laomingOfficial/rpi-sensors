import RPi.GPIO as GPIO
import time

pin_red = 5
pin_green = 6
pin_blue = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_red, GPIO.OUT)
GPIO.setup(pin_green, GPIO.OUT)
GPIO.setup(pin_blue, GPIO.OUT)
pwm_red = GPIO.PWM(pin_red, 100)  # 100Hz frequency
pwm_green = GPIO.PWM(pin_green, 100)
pwm_blue = GPIO.PWM(pin_blue, 100)
dc = 0
delaySec = 0.1
pwm_red.start(dc)
pwm_green.start(dc)
pwm_blue.start(dc)


def destroy():
    pwm_red.stop()
    pwm_green.stop()
    pwm_blue.stop()
    GPIO.output(pin_red, GPIO.LOW)
    GPIO.output(pin_green, GPIO.LOW)
    GPIO.output(pin_blue, GPIO.LOW)
    GPIO.cleanup()


def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def map255to100(x):
    return map(x, 0, 255, 0, 100)


def rainbow():
    while True:
        for i in range(255):
            pos = i
            if pos < 85:
                pwm_red.ChangeDutyCycle(map255to100(pos*3))
                pwm_green.ChangeDutyCycle(map255to100(255-pos*3))
                pwm_blue.ChangeDutyCycle(map255to100(0))
            elif pos < 170:
                pos -= 85
                pwm_red.ChangeDutyCycle(map255to100(255-pos*3))
                pwm_green.ChangeDutyCycle(map255to100(0))
                pwm_blue.ChangeDutyCycle(map255to100(pos*3))
            else:
                pos -= 170
                pwm_red.ChangeDutyCycle(map255to100(0))
                pwm_green.ChangeDutyCycle(map255to100(pos*3))
                pwm_blue.ChangeDutyCycle(map255to100(255-pos*3))
            time.sleep(delaySec)


if __name__ == "__main__":
    try:
        rainbow()
    except KeyboardInterrupt:
        destroy()
