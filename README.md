# Denial of Service Code (codename:MACFEVER)

This repository contains a Python script designed to demonstrate a denial of service (DoS) vulnerability in macOS file handling by rapidly consuming desktop space. The script generates a large file and copies it multiple times. **This code is intended for research and educational purposes only.**

## Description

The script generates a file and it multiplies rapidly at the desktop folder of macOS. This can lead to rapid copies at the desktop folder and cause system instability(due to finder trying to load all the files) permanently requiring users to reinstall the whole macOS. This code does not prompt system to ask permission for access into folders for generating and multiplying the file. **The access for folders is required in normal circumstances for any script or application but this does not require because of the vulnerability in the mac file handling. This could potentially be exploited in the other cases for adding this code into some other script and then running this via python interpreter for multiply different purposes.**

## WARNING

**Important Notice**: 

- **For Research Purposes Only**: This script is intended solely for educational and research purposes to illustrate how a denial of service (DoS) attack can occur by consuming desktop folder.
- **Use with Caution**: RUNNING THIS SCRIPT WILL CAUSE SYSTEM CRASHES OR DATA LOSS AND HENCE RUN THIS IN A VIRTUAL MACHINE.
- **Controlled Environment**: ALWAYS RUN THIS SCRIPT IN A CONTROLLED ENVIRONMENT, SUCH AS A VIRTUAL MACHINE OR AN ISOLATED TESTING SYSTEM, TO AVOID ANY UNINTENDED DAMAGE.
- **Legal and Ethical Responsibility**: Misuse of this script can be illegal and unethical. Do not use this script to harm or disrupt any systems without explicit permission.

The author is not responsible for any damage caused by the misuse of this script.

## Usage

- `write_large_file`: Generates a file with random binary data.
- `multiply`: Copies the generated file multiple times.

## Adjustments

- in line 6, `for i in range(10000):` modify the number to generate the number of characters needed in a single line of the file.
- in line 3, `def write_file(file_name, line_length=1000):` modify the line length to generate number of lines needed.
