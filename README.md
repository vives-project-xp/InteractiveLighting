# InteractiveLighting

![Game room](./documentation/Images/gamelightingroom.jpg)

## Table of Contents

- [Introduction](#introduction)
- [Project Goals](#project-goals)
- [Features](#features)
- [Technical overview](#technical-overview)
     - [Software](#software)
     - [Hardware](#hardware)
- [User Interface](#user-interface)
     - [Webpage](#webpage)
          - [Home page](#home-page)
          - [Effect page](#effect-page)
          - [About page](#about-page)
     - [Ambient Sound Integration](#ambient-sound-integration)
- [Installation and Setup](documentation/installationHardware.md)
- [End conclusion](#end-conclusion)
- [Members](#members)

## Introduction

The Interactive Lighting Project is designed to create an immersive lighting system for the gaming room, offering users interactive options that dynamically change lighting effects based on ambient sound or controlled by the user. The lighting setup can be mounted on a Velcro panel, allowing it to be positioned anywhere near a power outlet. This README offers a comprehensive overview of the project's goals, technical specifications, and an installation guide.

## Project Goals

The primary goal of this project is to create a customizable and expandable lighting system for gaming rooms. The system should enhance gaming experiences by responding to in-game sound in real-time. Users can interact with the lighting in various ways, adjusting color and patterns to suit their preferences.

## Features

- User-Controlled Lighting: The lighting system allows users to interact with the system via a webpage, offering flexibility in customization.
- Customizable Settings: Users can adjust lighting colors, brightness, and patterns to create their desired atmosphere.

## Technical overview

### Software

- WLED: A versatile software library for controlling LED strips, offering various effects and customization options.
- Fusion 360: Used for designing and prototyping the physical components of the lighting system.
- Visual Studio Code: Used for writing the code for our online interface.
- LedFx: LedFx is a network based LED effect engine designed to deliver advanced real-time audio effects to a wide variety of devices.

### Hardware

- ESP32: A powerful microcontroller providing ample processing power and connectivity options.
- 24V Power Supply: To provide the necessary power for the LED strips and other components.
- DC/DC Converter: Ensures efficient power conversion and regulation.
- WS2812 LED Strips: Addressable LED strips capable of displaying a wide range of colors and patterns.
- Ceiling Mounting Hardware: Initially considered for mounting the LED strips, later replaced with a panel with velcro for easier installation and flexibility.
- JST Connectors: Used for connecting and disconnecting components easily.
- Velcro: This serves as a versatile mounting solution for attaching the LED strips to a panel or surface. It offers flexibility and adjustability in the placement of the lighting components.

## User Interface

Because we use the velcro panel and work with linking cables, we are able to make a shape for the leds and change it later on. The user can interact with the leds on our webpage. They can change colors, settings and effects.

### Webpage

We've put together a website that lets you take full control of your lights. There are different sections for controlling your LED settings like the color, brightness and to turn them on/off (Home page), or choose a cool effect (Effects page), and even learning a bit about what inspired us to create this (About page).

#### Home page

On this page you can control the general led settings. The solid color, the brightness and a button to turn them on or off. There is also a random effect button.
There is a left side and a right side. On the left side there is a big colorpicker to choose your own color. Next to the colorpicker there are 4 button for pure blue, red, green or white color.
On the right side, there is a button to turn the lights on or off. Below you can choose the brightness and a random effect.

![Home page](./documentation/Images/homepage.png)

#### Effect page

Here, you can choose from all the effects available in WLED. You can use the search bar to find a specific effect, or you can browse through the entire list to select one. Allowing you to create a unique atmosphere for the gaming room.

![Effect page](./documentation/Images/effectpage.png)

#### About page

This page is intended for informational purposes only, you cannot control the LEDs from here. It provides detailed information about the project, including its goals, features, and technical specifications. If you're looking to control the lighting system, refer to the dedicated control page where you can customize LED effects and effects.

![About page](./documentation/Images/aboutpage.png)

### Ambient Sound Integration

When you are playing a game, the sound and the music is something that you always need. You need to hear shots, monsters, footsteps and manny more things. Thats why we choose to add an sound integration.

#### LedFx

We were looking for a sound integration using WLED, and we quickly arrived at [LedFx](https://github.com/LedFx/LedFx). LedFx takes audio input and processes the data into real-time light to LEDs.

#### Using Guide

## Members

- Ibe Packo
- Lennart Fonteyne
- Yarno Otte
- Joren Vandewalle
