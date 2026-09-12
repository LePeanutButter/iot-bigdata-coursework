# ESP32 push button counter and stop system using internal pull-up resistors
from machine import Pin
import utime

# GPIO definitions
PIN_BUTTON_COUNT = 25
PIN_BUTTON_STOP  = 26

# Configure button input pins
# Internal pull-up enabled:
# released = 1
# pressed = 0
Button_Count = Pin(PIN_BUTTON_COUNT, Pin.IN, Pin.PULL_UP)
Button_Stop  = Pin(PIN_BUTTON_STOP,  Pin.IN, Pin.PULL_UP)


# System parameters
VENTANA_MS = 2000
DEBOUNCE_MS = 30

# Counting state variables
cuenta_actual = 0
record_maximo = 0


# Software debounce function
def boton_presionado(boton):
    # Button pressed
    if boton.value() == 0:
        inicio = utime.ticks_ms()

        # Wait while button remains pressed
        while boton.value() == 0:
            if utime.ticks_diff(utime.ticks_ms(), inicio) >= DEBOUNCE_MS:
                return True

            # Reduce CPU usage
            utime.sleep_ms(1)

    return False


# Main counting function
def iniciar_conteo():
    global cuenta_actual
    global record_maximo

    # Reset variables at start
    cuenta_actual = 0
    record_maximo = 0

    print("Hit the Stop button to finish\n")

    inicio_ventana = utime.ticks_ms()

    while True:
        # Check STOP button immediately
        if boton_presionado(Button_Stop):

            print()
            print("Stop button pressed")
            print("Maximum record:", record_maximo)

            cuenta_actual = 0
            record_maximo = 0

            # Wait until STOP button release
            while Button_Stop.value() == 0:
                utime.sleep_ms(10)
            return

        # Check Button_Count
        if boton_presionado(Button_Count):

            cuenta_actual += 1

            # Wait until button release to prevent multiple counts
            while Button_Count.value() == 0:
                # STOP button takes priority
                if Button_Stop.value() == 0:
                    break

                utime.sleep_ms(1)

        # Check if 2-second window has elapsed
        ahora = utime.ticks_ms()

        if utime.ticks_diff(ahora, inicio_ventana) >= VENTANA_MS:
            # Update record
            if cuenta_actual > record_maximo:
                record_maximo = cuenta_actual

            print("Current count:", cuenta_actual)

            # Prepare next window
            cuenta_actual = 0
            inicio_ventana = ahora


# Main program loop
while True:
    iniciar_conteo()
    print("Hit the Count button to start over\n")

    while True:
        if boton_presionado(Button_Stop):
            while Button_Stop.value() == 0:
                utime.sleep_ms(10)

        if boton_presionado(Button_Count):
            # Wait for button release
            while Button_Count.value() == 0:
                utime.sleep_ms(1)

            print("New session started")
            break

        utime.sleep_ms(1)

