# InteractiveLighting

# Installation

## WLED

* Step 1: Make sure the hardware is setup correctly and that your ESP32 is connected to your laptop/PC. If this is not done, refer to [Hardware Installation](documentation/installationHardware.md)
* Step 2: Surf to [WLED](https://install.wled.me) and install WLED version 0.14.3 or the newest if you feel comfortable about any UI or other differences.
* Step 3: Restart the ESP-32. This will start the new software and it will now host an Access Point named WLED-AP. Connect to it using the password wled1234 and WLED will automatically open in your browser. If it doesn't, you can surf to [4.3.2.1](http://4.3.2.1). Keep in mind that you won't have any internet access while connected but we will fix this in a moment.
* Step 4: Connect WLED to your local network. Firstly, click on the config button at the top of the screen, then go to WIFI Setup. Click on the scan button and wait for it to scan. Once it's done, you should see a list of available networks. Select the one you want and enter the password if needed in the appropriate box. Optional: If you want to, you can change the link of this website. To do so, scroll down until you find the box labelled "mDNS address". Change the value to the link you want. After this is done, you should save and restart your ESP-32. The access point should no longer exist and you should instead connect to the network you selected. You can now go back to the WLED control panel with either the original url or the new one you set up.
* Step 5: Setup the hardware on WLED. Go back to the config and select LED Preferences. The values I am providing is for our project and the hardware we used. If you are using different hardware, please look up and enter the correct values. We found in our tests that putting the maximum current to 1000 mA works fine. LED Voltage is put to WS2815(12mA). LED Outputs, select SK6812/WS2814 RGBW. Color order: BRG, Swap: W & G. Length is 50. In our hardware setup, we put our Datapin on pin 7. If you used differently, change GPIO to the correct datapin which in our case is 7.

* Optional step 6: MQTT Setup. Skip this if you are not using MQTT. Go back to your config and select Sync Interfaces. Scroll down to the MQTT section and enable it. Fill in your credentials and you should be done.


## LedFX

LedFX is used for the audio oriented effects. Installation is fairly straight forward. Surf to [LedFX](https://www.ledfx.app/download-ledfx/) and download the latest version. Unzip the file and run LedFX.exe. It should give you a warning but it's perfectly safe. When it opens, it will hide itself. Click on the hidden icons button on your task bar to open it. Right click LedFX and select open. It should open a website in your browser. Follow the introduction steps and you should be good to go.

However if for some reason LEDfx can not be used we will need to make use of MQTT to send our data. For this we use a self made program which you can find [here](AudioReactivity.md)