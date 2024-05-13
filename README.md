# Interactive Lighting

![Game room](./documentation/Images/gamelightingroom.jpg)

## Table of Contents

- [Introduction](#introduction)
- [Project Goals](#project-goals)
- [Features](#features)
- [Technical Overview](#technical-overview)
     - [Software](#software)
     - [Hardware](#hardware)
- [User Interface](#user-interface)
     - [Webpage](#webpage)
          - [Home Page](#home-page)
          - [Effect Page](#effect-page)
          - [About Page](#about-page)
     - [Ambient Sound Integration](#ambient-sound-integration)
- [Installation and Setup](documentation/installationHardware.md)
- [Summary] (#Summary)
- [End Conclusion](#end-conclusion)
- [Members](#members)

## Introduction

The Interactive Lighting Project aims to create an immersive lighting system for gaming rooms, offering users interactive options that dynamically change lighting effects based on ambient sound or user control. The lighting setup, which can be mounted on a Velcro panel, provides versatility in placement near a power outlet. This README provides an extensive overview of the project's objectives, technical details, and an installation guide.

## Project Goals

The primary objective of this project is to develop a customizable and expandable lighting system for gaming rooms. The system should enrich gaming experiences by responding to in-game sounds in real-time, allowing users to interact with the lighting in various ways and adjust colors and patterns to match their preferences.

## Features

- User-Controlled Lighting: The lighting system enables users to interact with it via a webpage, offering flexibility in customization.
- Customizable Settings: Users can adjust lighting colors, brightness, and patterns to create their desired gaming atmosphere.

## Technical Overview

### Software

- **WLED:** This versatile software library controls LED strips, providing a range of effects and customization options.
- **Fusion 360:** Used for designing and prototyping the physical components of the lighting system.
- **Visual Studio Code:** Utilized for writing the code for the online interface.
- **LedFx:** A network-based LED effect engine designed to deliver advanced real-time audio effects to various devices.

### Hardware

- **ESP32:** A powerful microcontroller providing ample processing power and connectivity options.
- **24V Power Supply:** Supplies power to the LED strips and other components.
- **DC/DC Converter:** Ensures efficient power conversion and regulation.
- **WS2812 LED Strips:** Addressable LED strips capable of displaying a wide range of colors and patterns.
- **Ceiling Mounting Hardware:** Initially considered for mounting the LED strips but replaced with a Velcro panel for easier installation and flexibility.
- **JST Connectors:** Facilitate easy connection and disconnection of components.
- **Velcro:** Offers a versatile mounting solution for attaching the LED strips to a panel or surface, enabling flexible placement.

## User Interface

The user interacts with the LEDs through a webpage. They can control colors, settings, and effects.

### Webpage

A website has been developed to provide full control over the lights. It features different sections for LED control such as color, brightness adjustment, on/off control (Home page), effect selection (Effects page), and information about the project (About page).

#### Home Page

This page allows control of the general LED settings. Users can adjust the solid color, brightness, and turn the lights on or off. There's a left side with a color picker and buttons for predefined colors, and a right side with controls for power and brightness, as well as a button for random effects.

![Home page](./documentation/Images/homepage.png)

#### Effect Page

Here, users can choose from a variety of effects available in WLED. They can either search for specific effects or browse through the entire list to select one, enabling them to create a unique gaming atmosphere.

![Effect page](./documentation/Images/effectpage.png)

#### About Page

This page provides detailed information about the project's goals, features, and technical specifications. It's intended for informational purposes only and does not offer LED control.

![About page](./documentation/Images/aboutpage.png)

### Ambient Sound Integration

To enhance the gaming experience, sound integration has been implemented.

#### LedFx

LedFx was chosen for sound integration as it takes audio input and converts it into real-time light effects for LEDs.

#### Usage Guide

The webpage provides simple and user-friendly control. The LED strips' rearrangeability, facilitated by Velcro and JST connectors, allows for multiple configurations.

## Summary



## Members

- Ibe Packo
- Lennart Fonteyne
- Yarno Otte
- Joren Vandewalle
