# ESP32 LED toggle using a pushbutton and internal pull-up resistor
from machine import Pin
import time

# GPIO definitions
LED_PIN = 4
BUTTON_PIN = 18

# Configure LED output pin
led = Pin(LED_PIN, Pin.OUT)
led.value(0)

# Configure button input pin
# Internal pull-up enabled:
# released = 1
# pressed = 0
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

# Current LED state
led_state = False

while True:
    # Button pressed
    if button.value() == 0:
        
        # debounce delay
        time.sleep_ms(50)
        
        # verify button is still pressed
        if button.value() == 0:
            # Toggle LED state
            led_state = not led_state
            
            # Update LED output
            led.value(led_state)

            # Wait until button release
            # This prevents multiple toggles from a
            # single long press.
            while button.value() == 0:
                time.sleep_ms(10)
            
            # release debounce
            time.sleep_ms(50)
    
    # Reduce CPU usage
    time.sleep_ms(10)
