# IoT & Big Data Coursework

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Coursework repository for the **Software Engineering for IoT and Big Data (ISIB_M)** course.

This repository contains practical activities and assignments focused on **Internet of Things (IoT)** concepts, embedded systems, digital inputs and outputs, and data-oriented applications using technologies such as **ESP32**, **MicroPython**, and **Wokwi**.

## Table of Contents

- Background
- Projects
- Requirements
- Install
- Usage
- Project Structure
- License

## Background

This repository contains coursework developed for the **Software Engineering for IoT and Big Data (ISIB_M)** course.

The main objective is to explore fundamental IoT concepts through practical exercises using simulated embedded systems. The activities focus on programming an **ESP32** with **MicroPython**, designing simple digital input/output applications, and testing circuits using the **Wokwi** simulator.

The repository is organized as a collection of independent activities. Each activity contains its own source code, circuit definition, and documentation.

Current activities include:

1. **ESP32 LED Toggle Button** — Controls an LED using a push button, including input debouncing and the ESP32 internal pull-up resistor.
2. **ESP32 Push Button Counter Stop** — Counts button presses during timed intervals and records the maximum number of presses achieved during a session.

Additional coursework activities can be added to the repository as new projects.

## Projects

### ESP32 LED Toggle Button

A MicroPython activity that implements a simple digital input/output application using an ESP32.

A push button is used to toggle a red LED between `ON` and `OFF` states. The application uses the ESP32's internal pull-up resistor and implements basic software debouncing.

**Main concepts:**

- ESP32 digital input/output
- MicroPython GPIO programming
- Push buttons
- LED control
- Internal pull-up resistors
- Software debouncing
- Wokwi circuit simulation

  **Location:**

```
esp32-led-toggle-button/
```

### ESP32 Push Button Counter Stop

A MicroPython activity that counts push button presses during consecutive **2-second time windows**.

The application uses two buttons:

- A **Count button** to increment the current number of presses.
- A **Stop button** to finish the current counting session.

At the end of each time window, the current count is displayed through the serial monitor. The maximum count achieved during the session is stored as a record.

**Main concepts:**

- ESP32 digital inputs
- MicroPython GPIO programming
- Multiple push buttons
- Software debouncing
- Timed counting windows
- Serial monitor output
- Session management
- Wokwi circuit simulation

  **Location:**

```
esp32-pushbutton-counter-stop/
```

## Requirements

The coursework projects are primarily designed to run using the following tools and technologies:

- ESP32 DevKit C V4
- MicroPython
- Wokwi
- Python/MicroPython source files
- A web browser for Wokwi simulation

Physical hardware is not required for the current activities because the circuits can be simulated using Wokwi.

Some individual projects may have additional hardware or software requirements. See the `README.md` inside each project directory for project-specific requirements.

## Install

There is no global installation or package setup required for the current coursework.

To run an individual activity:

1. Open the project directory.
2. Open the project in [Wokwi](https://wokwi.com/).
3. Load the project's `diagram.json` circuit configuration.
4. Load the `main.py` MicroPython application.
5. Start the simulation.
6. Follow the instructions provided in the project's README.

For activities that produce output through the ESP32 serial interface, open the Wokwi serial monitor to observe the application output.

## Project Structure

The repository is organized by coursework activity:

```
iot-bigdata-coursework/
├── esp32-led-toggle-button/
├── esp32-pushbutton-counter-stop/
└── README.md
```

Each project follows a similar structure.

### `diagram.json`

Contains the Wokwi circuit configuration, including the ESP32, electronic components, and their connections.

### `main.py`

Contains the MicroPython implementation for the activity.

### `README.md`

Contains the documentation specific to the activity, including its objective, requirements, installation instructions, usage, and project structure.

## License

[MIT](LICENSE) © LePeanutButter
