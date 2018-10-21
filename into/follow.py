from ev3dev import ev3

leftMotor = ev3.LargeMotor("outA")
rightMotor = ev3.LargeMotor("outB")

colorSensor = ev3.ColorSensor("in1")
colorSensor.mode = "COL-REFLECT"

unit = leftMotor.count_per_rot

try:
    while True:
        intensity = colorSensor.value()
        print(intensity)
        
        leftSpeed = -intensity/100*unit
        rightSpeed = -(100-intensity)/100*unit

        leftMotor.run_forever(speed_sp=leftSpeed)
        rightMotor.run_forever(speed_sp=rightSpeed)

finally:
    leftMotor.stop(stop_action="coast")
    rightMotor.stop(stop_action="coast")
