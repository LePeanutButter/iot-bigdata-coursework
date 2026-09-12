# ESP32 Push Button Counter Stop

A MicroPython activity for counting push button presses within timed intervals using an ESP32 and Wokwi.

## Table of Contents

- Background
- Requirements
- Install
- Usage
- Project Structure

## Background

This activity is part of the **Software Engineering for IoT and Big Data** course.

The objective is to implement a digital input application using an **ESP32**, **MicroPython**, and the **Wokwi** simulator.

The application uses two push buttons:

- A **Count button** to increment the current number of button presses.
- A **Stop button** to finish the current counting session.

The system counts button presses during **2-second time windows**. At the end of each window, the current count is displayed and the maximum count achieved during the session is recorded.

The push buttons are configured using the ESP32's internal **pull-up resistors**. The implementation also includes a software **debouncing** mechanism to prevent a single physical button press from being interpreted as multiple presses.

The Stop button has priority over the Count button and can be used to terminate the current counting session.

## Requirements

- ESP32 DevKit C V4
- MicroPython
- Wokwi
- Two push buttons

No physical hardware is required to run the activity because the circuit can be simulated using Wokwi.

## Install

No additional dependencies are required.

To run the activity:

1. Open the project in [Wokwi](https://wokwi.com/).
2. Load the `diagram.json` circuit configuration.
3. Use a MicroPython-compatible ESP32 environment.
4. Load `main.py`.
5. Start the simulation.
6. Open the serial monitor to view the counting results.

## Usage

Once the simulation starts, the system waits for the **Count button** to start a counting session.

During a session:

- Press the **Count button** to increment the current count.
- The system counts presses during 2-second windows.
- At the end of each window, the current count is displayed in the serial monitor.
- The highest count reached in any 2-second window is stored as the record.
- Press the **Stop button** to finish the session.

Example serial monitor output:

```
Hit the Stop button to finish

Current count: 5
Current count: 7
Current count: 4

Stop button pressed
Maximum record: 7

Hit the Count button to start over
```

After the session is stopped, the system waits for the **Count button** to start a new session.

The application also waits for each button to be released before accepting another press. This prevents a single long press from being counted multiple times.

The **Stop button takes priority** while the Count button is being held.

## Project Structure

```
esp32-pushbutton-counter-stop/
├── diagram.json
├── main.py
└── README.md
```

### `diagram.json`

Contains the Wokwi circuit definition, including the ESP32, the two push buttons, and their connections to GPIO 25, GPIO 26, and GND.

### `main.py`

Contains the MicroPython implementation for reading both push buttons, debouncing the inputs, counting button presses in 2-second windows, tracking the maximum count, and controlling the counting sessions.

### `README.md`

Contains the documentation for the activity.
