# ESP32 LED Toggle Button

A MicroPython activity for controlling an LED with a push button using an ESP32 and Wokwi.

## Table of Contents

- Background
- Requirements
- Install
- Usage
- Project Structure

## Background

This activity is part of the **Software Engineering for IoT and Big Data** course.

The objective is to implement a simple digital input/output application using an **ESP32**, **MicroPython**, and the **Wokwi** simulator.

The application uses a push button to toggle the state of an LED. Each valid button press changes the LED state from:

- `OFF` to `ON`
- `ON` to `OFF`

The push button is configured using the ESP32's internal **pull-up resistor**. The implementation also includes a basic **debouncing** mechanism to prevent a single physical button press from being interpreted as multiple presses.

## Requirements

- ESP32 DevKit C V4
- MicroPython
- Wokwi
- One red LED
- One `220 Ω` resistor
- One push button

No physical hardware is required to run the activity because the circuit can be simulated using Wokwi.

## Install

No additional dependencies are required.

To run the activity:

1. Open the project in [Wokwi](https://wokwi.com/).
2. Load the `diagram.json` circuit configuration.
3. Use a MicroPython-compatible ESP32 environment.
4. Load `main.py`.
5. Start the simulation.

## Usage

Once the simulation starts, the LED is initially turned off.

Press the push button to toggle the LED:

```
Button press → LED ON
Button press → LED OFF
Button press → LED ON
Button press → LED OFF
```

The application waits for the button to be released before accepting another press. This prevents a single long press from causing multiple state changes.

## Project Structure

```
esp32-led-toggle-button/
├── diagram.json
├── main.py
└── README.md
```

### `diagram.json`

Contains the Wokwi circuit definition, including the ESP32, LED, resistor, push button, and their connections.

### `main.py`

Contains the MicroPython implementation for reading the push button and controlling the LED.

### `README.md`

Contains the documentation for the activity.
