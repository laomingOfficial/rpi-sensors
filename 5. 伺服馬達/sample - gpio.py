import RPi.GPIO as GPIO
import time

pin_servo = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_servo, GPIO.OUT)
pwm_servo = GPIO.PWM(pin_servo, 50)  # 50Hz frequency
pwm_servo.start(0)


def destroy():
    pwm_servo.stop()
    GPIO.cleanup()


# 輸入0 ～ 180度即可
# 別超過180度
def setDirection(angle):
    # 0 = 停止轉動
    # 2 = 0度
    # 7 = 90度
    # 12 = 180度
    duty = 2 + (angle / 18)
    pwm_servo.ChangeDutyCycle(duty)
    # 消除抖動
    time.sleep(0.3)
    pwm_servo.ChangeDutyCycle(0)
    print("角度=", angle, "-> duty=", duty)


def run():
    for angle in range(0, 181, 10):
        setDirection(angle)
        time.sleep(1)


if __name__ == "__main__":
    try:
        run()
    finally:
        destroy()
