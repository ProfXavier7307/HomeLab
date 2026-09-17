# PiTV

> **Status:** Functional Raspberry Pi TV interface with ongoing feature development. Core launcher, HDMI display/audio, Bluetooth input, weather access, utility pages, and game streaming are working.

## Project Overview

PiTV is a custom Raspberry Pi-based interface I built to turn a non-smart television into a simple, dedicated media and information display.

The project uses a **Raspberry Pi 4B with 8 GB of RAM** running Raspberry Pi OS and launches a custom local interface in fullscreen Chromium. The goal was to create something closer to a lightweight smart-TV dashboard than a normal desktop: large buttons, quick access to services, local weather information, system controls, game streaming, and minimal interaction with the underlying operating system.

Rather than purchasing a replacement TV, I used existing hardware and built the interface around the way I actually wanted to use the display.

## Hardware

- **Raspberry Pi 4B**
- **8 GB RAM**
- Raspberry Pi OS
- HDMI connection to a non-smart television
- Heatsink and active fan cooling
- Elevated mounting / threaded standoffs for airflow
- Bluetooth keyboard with integrated touchpad for control

## Project Goals

- Convert a non-smart TV into a useful connected display
- Create a simple TV-friendly launcher instead of exposing the normal desktop
- Practice Raspberry Pi / Linux configuration
- Build and iterate on a custom local web interface
- Integrate streaming-service shortcuts and local information pages
- Provide weather and radar access from the couch
- Add TV-friendly system controls such as volume, networking, and power options
- Make Bluetooth input and HDMI audio behave reliably after reboot
- Add local-network game streaming from a more powerful PC

## Core Interface

PiTV launches a custom local dashboard in **fullscreen Chromium**.

The interface was designed around large, easy-to-select controls for use from across the room rather than a traditional keyboard-and-mouse desktop workflow.

The launcher included or was designed to include quick access to services such as:

- Netflix
- Disney+
- Hulu
- Prime Video
- Max / HBO
- Local weather
- News
- Radar
- Game streaming
- System utilities

The interface went through multiple revisions as I added controls and reorganized the layout.

## Display Configuration

One of the first issues was display overscan / edge cutoff on the television.

I corrected the visible area using HDMI margin adjustments. The working values were approximately:

```text
Left / Right: 40 px
Top / Bottom: 25 px
```

This allowed the Chromium interface to fit the physical TV correctly without important controls being cut off at the edges.

## HDMI Audio

HDMI audio was configured and tested successfully through the Raspberry Pi.

The system used the Raspberry Pi OS audio stack, including **PipeWire / WirePlumber**, and audio output was routed over HDMI to the television.

This was important because PiTV was intended to behave like an appliance: video and audio both needed to work without manually reconfiguring the desktop each time.

## Bluetooth Input

A Bluetooth keyboard / touchpad combination was used as the primary remote-input device.

I configured automatic reconnection using a `systemd`-based approach so the input device could reconnect after startup without requiring the normal Bluetooth settings interface each time.

This gave me experience with:

- Bluetooth pairing and reconnection
- Linux service behavior
- `systemd`
- Startup automation
- Troubleshooting hardware that works interactively but not automatically after reboot

## Weather and Local Information

Weather access became one of the more useful parts of PiTV.

The launcher included local weather information and access to radar, with a focus on making severe-weather information easy to reach quickly from the TV.

### Local News / Weather

I integrated links/pages for local News 9 weather information. During development, the weather page worked while one of the news links required correction, which became part of the iterative troubleshooting process.

### NOAA Weather Page

I also built a simplified NOAA weather view based on the National Weather Service MapClick forecast for my area.

The project used the approximate MapClick coordinates:

```text
Latitude:  35.4552
Longitude: -97.264
```

The goal was to make NOAA information easier to read from a television than the standard weather website.

Features developed or planned around this page included:

- Simplified forecast graphs
- A button to open the original NOAA page
- Hourly forecast information
- A locally cached / refreshed copy for faster access

## Radar Page

PiTV also included a radar concept that combined two different types of situational information:

- **Weather radar**
- **Aircraft radar / tracking**

This gave the interface a dedicated page for viewing both weather conditions and nearby aircraft activity from the TV.

## Utility Controls

As the project evolved into a later interface revision, I began adding a utility row so basic Pi functions could be controlled without leaving the TV interface.

Utilities included or were planned around:

- PiTV settings
- Volume controls
- Power / shutdown menu
- Network tools
- Weather-emergency mode
- Quick access to diagnostic information

I specifically chose **not** to add a screensaver because I wanted the interface to remain immediately available rather than introducing another layer to dismiss.

## Launcher / Recovery Workflow

Because PiTV is intended to launch directly into a TV interface, I also created a simple one-click way to relaunch the fullscreen Chromium interface from the desktop if the browser was closed or the kiosk session needed to be restarted.

This made recovery easier without requiring terminal commands every time.

## Game Streaming

Game streaming was successfully integrated into PiTV using **Luna** on the Raspberry Pi as the client and **Sunshine** on the host PC.

This allows games running on a more powerful computer elsewhere on the local network to be streamed to the television through the Raspberry Pi, extending PiTV beyond a media launcher into a lightweight game-streaming endpoint.

Getting this working required configuring both sides of the connection and troubleshooting the original sign-in/API issue before arriving at a working Luna + Sunshine setup.

This part of the project gave me experience with:

- Client/server game-streaming architecture
- Host and client configuration
- Local-network streaming
- Authentication / connection troubleshooting
- Integrating an external application into a custom TV workflow
- Separating front-end launcher issues from the underlying streaming stack

## Architecture

```text
                    Non-Smart Television
                           |
                         HDMI
                           |
                    +-------------+
                    | Raspberry Pi|
                    | 4B / 8 GB   |
                    | Raspberry Pi|
                    | OS          |
                    +------+------+ 
                           |
                  Fullscreen Chromium
                           |
      +--------------------+--------------------+
      |                    |                    |
 Streaming /          Weather /             PiTV
 Game Access          Radar / NOAA           Utilities
      |                    |                    |
      +--------------------+--------------------+
                           |
                    Local PiTV UI
                           |
                        Luna Client
                           |
                      Local Network
                           |
                    Sunshine Host PC

Bluetooth keyboard / touchpad -> Raspberry Pi
HDMI audio -> Television
```

## Design Approach

A major part of this project was treating the Raspberry Pi less like a desktop computer and more like a dedicated appliance.

That meant focusing on:

- Automatic startup behavior
- Fullscreen UI design
- Reliable input reconnects
- Correct TV scaling
- HDMI audio
- Simple recovery when something fails
- Large controls readable at television distance
- Reducing the need to interact with the Linux desktop directly
- Integrating local-network game streaming into the same TV workflow

## Troubleshooting Examples

### Overscan / Cropped Interface

**Problem:** Parts of the UI were cut off by the television.

**Solution:** Adjusted HDMI margins until the full interface fit within the visible area.

### Bluetooth Reconnection

**Problem:** The keyboard / touchpad could pair successfully but needed to reconnect reliably after reboot.

**Solution:** Added startup/service automation so the Bluetooth device could reconnect automatically.

### HDMI Audio

**Problem:** Audio needed to consistently use the television rather than another output path.

**Solution:** Configured and tested the PipeWire / WirePlumber audio path for HDMI output.

### Game Streaming Integration

**Problem:** An earlier game-streaming integration attempt produced an API/sign-in issue and the sign-in flow did not work correctly.

**Solution:** Continued troubleshooting and ultimately implemented a working **Luna client + Sunshine host** setup for local-network game streaming.

This was a useful example of not treating the first failed integration as the end of the feature; I changed the implementation and kept testing until the streaming path worked reliably.

## Skills Demonstrated

This project demonstrates hands-on experience with:

- Raspberry Pi hardware
- Raspberry Pi OS / Linux administration
- Chromium kiosk / fullscreen workflows
- Local web-interface design
- HTML / CSS / JavaScript integration
- Linux startup automation
- `systemd`
- Bluetooth troubleshooting
- HDMI display configuration
- PipeWire / WirePlumber audio configuration
- Weather-data integration
- NOAA / NWS resources
- Local-network game streaming
- Sunshine host configuration
- Luna client configuration
- UI design for large displays
- Iterative troubleshooting and feature development
- Repurposing existing hardware instead of replacing it

## Project Log

### August 2026 — PiTV Initial Build

- Set up Raspberry Pi 4B 8 GB on Raspberry Pi OS
- Built a fullscreen Chromium launcher for the TV
- Corrected television overscan using HDMI margins
- Configured HDMI audio
- Configured Bluetooth keyboard / touchpad automatic reconnection
- Added local weather and streaming-service access
- Created a one-click way to relaunch PiTV from the desktop

### August 2026 — Interface Expansion

- Expanded the launcher with additional streaming services
- Added a utility-row concept for settings, volume, power, networking, and weather functions
- Chose to keep the system without a screensaver
- Added weather and aircraft radar concepts
- Built a simplified NOAA forecast page using local NWS data
- Experimented with game-streaming integration
- Encountered an initial API/sign-in issue during development
- Reworked the game-streaming setup and successfully configured **Luna + Sunshine** for local-network streaming

---

**Project by Alexander Rodriquez**

This document will be updated if PiTV receives additional interface revisions or integrations.