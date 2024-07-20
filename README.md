# Denial of Service Code (codename:MACFEVER)

This repository contains a Python script designed to demonstrate a denial of service (DoS) vulnerability in macOS file handling by rapidly consuming desktop space. The script generates a large file and copies it multiple times. **This code is intended for research and educational purposes only.**

## Description

The script generates a file and it multiplies rapidly at the desktop folder of macOS. This can lead to rapid copies at the desktop folder and cause system instability within seconds **(due to finder trying to load all the files and causing the CPU Load to go all the way up)**, permanently requiring users to reinstall the whole macOS.

The author is not responsible for any damage caused by the misuse of this code.

## Usage

- `write_large_file`: Generates a file with random binary data.
- `multiply`: Copies the generated file multiple times.

## Adjustments

- in line 6, `for i in range(10000):` modify the number to generate the number of characters needed in a single line of the file.
- in line 3, `def write_file(file_name, line_length=1000):` modify the line length to generate number of lines needed.
