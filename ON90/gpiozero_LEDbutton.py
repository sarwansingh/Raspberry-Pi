from gpiozero import LED, Button
from signal import pause

led = LED(14)
button = Button(24)

button.when_pressed = led.on
button.when_released = led.off

pause()