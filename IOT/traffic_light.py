# from gpiozero import LED,buzzer,DistanceSensor
# from time import sleep

# red = LED(17)
# yellow = LED(27 )
# green = LED(22)
# buzzer = Buzzer(18)
# sensor = DistanceSensor(echo=23, trigger=24)
from gpiozero import LED, Buzzer, DistanceSensor
from time import sleep

# Traffic lights
red = LED(17)
yellow = LED(22)
green = LED(25)

# Buzzer
buzzer = Buzzer(27)

# Ultrasonic sensor
sensor = DistanceSensor(
    echo=24,
    trigger=23,
    max_distance=2
)

while True:

    # =========================
    # RED LIGHT
    # =========================
    red.on()
    yellow.off()
    green.off()

    print("RED - Stop")

    # Monitor for objects for 5 seconds
    for i in range(30):
        distance = sensor.distance * 100

        print(f"Distance: {distance:.1f} cm")

        if distance < 20:
            print("OBJECT DETECTED ")

            buzzer.on()
            sleep(0.2)
            buzzer.off()
            buzzer.on()
            sleep(0.2)
            buzzer.off()

        sleep(0.4)

    # =========================
    # YELLOW LIGHT
    # =========================
    red.off()
    yellow.on()
    green.off()

    print("YELLOW - Get Ready")
    # Monitor for objects for 5 seconds
    for i in range(3):
        distance = sensor.distance * 100

        print(f"Distance: {distance:.1f} cm")

        if distance < 20:
            print("OBJECT DETECTED ")

            buzzer.on()
            sleep(0.2)
            buzzer.off()
            buzzer.on()
            sleep(0.2)
            buzzer.off()

        sleep(1.5)

    sleep(2)

    # =========================
    # GREEN LIGHT
    # =========================
    red.off()
    yellow.off()
    green.on()

    print("GREEN - Go")
    buzzer.off()

    sleep(10)

