#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
import time
import json
from PIL import Image, ImageDraw, ImageFont
from waveshare_epd import epd2in13_V3

def read_json_data(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON data from '{json_file}'.")
        return None

def draw_table(draw, title, data, font):
    # Table title
    title_width = 240  # Adjust as needed
    title_height = 30   # Adjust as needed
    x_title, y_title = 10, 10

    draw.rectangle([x_title, y_title, x_title + title_width, y_title + title_height], outline=0, fill=255)  # White background
    draw.text((x_title + 5, y_title + 4), title, font=font, fill=0)  # Black text

    # Table header
    header = ["Name", "RSSI", "MAC"]
    col_width = [80, 40, 120]
    row_height = 20
    x, y = 10, y_title + title_height + 5  # Adjust the vertical position

    for i, header_text in enumerate(header):
        draw.rectangle([x, y, x + col_width[i], y + row_height], outline=0, fill=255)  # White background
        draw.text((x + 5, y + 4), header_text, font=font, fill=0)  # Black text
        x += col_width[i]

    # Table data
    y += row_height
    for entry in data:
        x = 10
        for i, key in enumerate(header):
            draw.rectangle([x, y, x + col_width[i], y + row_height], outline=0, fill=255)  # White background
            draw.text((x + 5, y + 4), str(entry.get(key, "")), font=font, fill=0)  # Black text
            x += col_width[i]
        y += row_height


def main():
    json_file = "/home/pi/Wall-of-Flippers/Flipper.json"
    data = read_json_data(json_file)

    if data is None:
        sys.exit(1)

    epd = epd2in13_V3.EPD()
    epd.init()
    epd.Clear(0xFF)

    # Drawing on the image
    image = Image.new('1', (epd2in13_V3.EPD_HEIGHT, epd2in13_V3.EPD_WIDTH), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)

    # Use default font from Pillow
    font = ImageFont.load_default()

    title = "Wall of Flipper"

    # Draw the table
    draw_table(draw, title, data, font)

    # Display the image on the screen for X seconds, edit this value if you want to increase the amount of time the value will be shown
    epd.display(epd.getbuffer(image))
    time.sleep(20)

    # Clear the display
    epd.Clear(0xFF)

    # Sleep to save power
    epd.sleep()

if __name__ == "__main__":
    main()