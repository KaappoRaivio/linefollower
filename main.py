from ev3dev import ev3
import time

print("trying to get motor handle")
motor = ev3.Motor("outA")
print("got ")
# motor.run_forever()
m = ev3.Motor('outA')

# m.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action="hold")
# time.sleep(5)
m.run_direct(speed_sp=900, stop_action="hold")
time.sleep(5)
