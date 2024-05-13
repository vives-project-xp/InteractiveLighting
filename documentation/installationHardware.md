# Interactive Lighting

## Hardware Installation

### LED Strip 2814

Connect the correct cables to your power supply and ESP-32. The red cable should go to the positive side and white to ground. Connect the green cable to your datapin on your ESP-32, in our case GPIO 7 and the other white cable to the ground on your ESP-32. There should be a provided JST-Connector that should give you the green and other white cable.

Power your ESP-32 with a micro-usb cable or a 5V power supply. You can optionally put it in a breadboad and connect the cables that way.

## ESP-32

Power your ESP-32 with a micro-usb cable or a 5V power supply. You can optionally put it in a breadboad and connect the cables that way.

## Levelshifter

Because the WS2814 expects its data to be at 5V and the ESP sends its data at 3V3 this can have some unintended consequences. THe solution to this problem is to use a levelshifter. We opted to make our own however if you want to use a single component that too can be done. Do make sure the data can be sent at at least 1MHz.

### Schematic

- Levelshifter
![Level Shifter Documentation](/documentation/Images/Levelshifter.png)

- Electrical scheme
![Electrical scheme](/documentation/Images/Elektrisch%20schema.png)

## Software Installation

After comleting this you can go to the [Software](/documentation/installationSoftware.md) guide.
