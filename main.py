from ev3dev import ev3
import time

print("trying to get motor handle")


# motor.run_forever()
m = ev3.Motor('outA')
m.run_forever(speed_sp=500)

time.sleep(5)
m.run_forever(speed_sp=1000)

m.stop(stop_action="coast")
time.sleep(5)