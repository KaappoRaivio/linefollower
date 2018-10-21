from ev3dev import ev3
import time

print("trying to get motor handle")
motor = ev3.Motor("outA")
print("got ")
motor.run_forever()
time.sleep(1)
motor.stop()