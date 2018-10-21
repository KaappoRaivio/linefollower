from ev3dev import ev3

leftMotor = ev3.LargeMotor("outA")
rightMotor = ev3.LargeMotor("outB")

colorSensor = ev3.ColorSensor("in1")
colorSensor.mode = "COL-REFLECT"

unit = leftMotor.count_per_rot

while True:
    intensity = colorSensor.value()
    
    leftSpeed = intensity/100
    rightSpeed = (100-intensity)/100

    leftMotor.run_forever(speed_sp=leftSpeed)
    rightMotor.run_forever(speed_sp=rightSpeed)

