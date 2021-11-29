import RPi.GPIO as GPIO
import time
from StepperMotor import StepperMotor

pin_stepper = [23, 24, 27, 22]

GPIO.setmode(GPIO.BCM)
stepperMotor = StepperMotor(pin_stepper)
# max 15rpm
stepperMotor.rpm = 10


def destroy():
    GPIO.cleanup()


def run():
    stepperMotor.move_to(90)
    time.sleep(1)
    stepperMotor.move_to(180)
    time.sleep(1)
    stepperMotor.move_to(270)
    time.sleep(1)
    stepperMotor.move_to(0)
    time.sleep(1)


if __name__ == "__main__":
    try:
        run()
    finally:
        destroy()
