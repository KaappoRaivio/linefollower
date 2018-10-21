from ev3dev import ev3
import time


motor = ev3.Motor("out1")
motor.run_forever()
time.sleep(1)
motor.stop()