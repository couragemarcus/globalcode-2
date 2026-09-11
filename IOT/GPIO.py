from gpiozero import LED, Buzzer, DistanceSensor
from time import sleep

# Components
led = LED(17)
buzzer = Buzzer(27)

sensor = DistanceSensor(
    echo=24,
    trigger=23,
    max_distance=2
)

while True:
    distance = sensor.distance * 100  # convert meters to cm

    print(f"Distance: {distance:.1f} cm")

    if distance < 20:
        led.on()
        buzzer.on()
    else:
        led.off()
        buzzer.off()

    sleep(0.1)



