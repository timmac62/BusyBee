import time
import board
import digitalio
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

mode_button = digitalio.DigitalInOut(board.SLIDE_SWITCH)
mode_button.direction = digitalio.Direction.INPUT
mode_button.pull = digitalio.Pull.UP

# Update to utilize newer board with Bluetooth

# GitHub  is disconnected?

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

flash_rate = 1.0

while True:
    if mode_button.value is True:
        pixels.fill(RED)
        pixels.show()
        time.sleep(flash_rate)
        pixels.fill(OFF)
        pixels.show()
        time.sleep(flash_rate)
    else:
        pixels.fill(OFF)
        pixels.show()
