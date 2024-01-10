

# Table of Contents
- [Introduction](#doc_intro)
- [How to Install Guide](#doc_how_to_install)
- [Execute Wall of Pwn Flipper](#doc_execute)

<br><br>

# Wall of Flippers on a pwnagotchi <a name = "doc_intro"></a>

The first goal was to install [Wall of Flippers](https://github.com/K3YOMI/Wall-of-Flippers/tree/main) on Raspberry Pi Zero. 

The only Raspberry Pi Zero i had was a full kit (E-ink waveshare V3 and battery) from my [Pwnagotchi](https://github.com/evilsocket/pwnagotchi) i then decided to print the data from the Flipper.json file from Wall of Flipper scan to my e-ink screen.

It's a basic guide of how to install dependecies for Wall of Flipper and for WaveShare V3 e-ink display.

# How to Install Guide <a name = "doc_how_to_install"></a>

## Raspberry Pi Zero Install

### Way 1
Use [Raspberry Pi Imager](https://www.raspberrypi.com/software/) in os type select Raspberry Pi OS Lite 32-bit.
Click on the bottom right and enter your wifi ssid and password (Used to connect via ssh to your RPI Zero).
Flash your SD card

### Way 2
Download the Raspberry Pi OS Lite 32-bit version on [Raspberry Pi website](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-32-bit) and flash it on your SD card with [BalenaEtcher](https://etcher.balena.io).

If you want to connect via SSH over USB to your RPI Zero follow [this](https://artivis.github.io/post/2020/pi-zero/)

> Use SSH to connect to your flipper by default user=pi and password=raspberry

## Prepare Raspberry Pi Zero for the next step

### Package installation

    sudo apt-get update && sudo apt-get upgrade -y

    sudo apt-get install git

    sudo apt-get install python3-pip

### Activate SPI module

    sudo raspi-config

Navigate to Interfacing Options.
Enable SPI.
Reboot your Pi

    sudo reboot

Verify SPI kernel loaded

    lsmod | grep spi

> You should see : spi-bcm2835



## Install Wall of Flipper

Just follow the Debian Linux Install Guide on [Wall of flipper](https://github.com/K3YOMI/Wall-of-Flippers/tree/main) github.

Here is the step by step guide in case :

	sudo apt-get install libglib2.0-dev
 	sudo apt-get install python3-bluez
	python3 -m venv .venv
	source .venv/bin/activate

    python3 -m pip install -r requirements.txt

    deactivate

Try to launch Wall of Flipper with :
    sudo bash wof.sh

> Enter 1 then enter 0 (RPI0 default HCI=0) if it works just ctrl+c to exit

## Install WaveShare V3 dependencies

### Clone Waveshare repository

    cd
    git clone https://github.com/waveshare/e-Paper.git

### Basic package

    sudo apt-get install python3-numpy

### Python package

    source /home/pi/Wall-of-Flippers/.venv/bin/activate

    cd /home/pi/e-paper/RaspberryPi_JetsonNano/python/

    sudo python3 setup.py install

    pip3 install spidev -> in venv don't need to use pip3 specifically, pip is sufficient 
    pip3 install Pillow --> Normally already in the setup.py from waveshare
    pip3 install gpiozero (not sure if required)


## Test WaveShare screen

    cd /home/pi/e-paper/RaspberryPi_JetsonNano/python/examples
    sudo python3 epd_2in13_V3_test.py

# Execute Wall of Pwn Flipper <a name = "doc_execute"></a>

    git clone https://github.com/MarkusR0st/wall-of-pwn-flipper.git

    cd wall-of-pwn-flipper

    python3 wall-of-pwn.py

# IN PROGRESSCreate an startup script <a name = "doc_startup"></a>

The startup script will run wall of flipper and wall of pwnagotchi in background at startup.
It'll update the screen every 10 seconds.


# What's next ? 

- Create a pwnagotchi plugin to run wall of pwn flipper and show information on screen
- Create a script to launch wall of pwn flipper and wall of pwn at startup
- Clean up script and guide
- Make a lighter version of wall of pwn flipper ?
- Add date to the table ? (Add date to the Flipper.json file)
- Add GPS coordinate ?

# Notes

This guide is not a reference of best practice to do this install. It works for me but may not work for you.
The code is really basic as i'm not a developper and only have basic knowledge of Python.
Don't hesitate to submit issue and create pull request.
