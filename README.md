# Denial of Service Code (codename:MACFEVER)

This repository contains a Python script designed to demonstrate a denial of service (DoS) vulnerability in macOS file handling by rapidly consuming desktop space. The script generates a large file and copies it multiple times. **This code is intended for research and educational purposes only.**

## Description

The script generates a file and it multiplies rapidly at the desktop folder of macOS. This can lead to rapid disk space consumption and cause system instability permanently requiring users to reinstall the whole macOS.

## Warning

**Important Notice**: 

- **For Research Purposes Only**: This script is intended solely for educational and research purposes to illustrate how a denial of service (DoS) attack can occur by consuming disk space.
- **Use with Caution**: Running this script can causes system crashes or data loss and hence run this in virtual machine or set limit in the code to 10 see below for more details.
- **Controlled Environment**: Always run this script in a controlled environment, such as a virtual machine or an isolated testing system, to avoid any unintended damage.
- **Legal and Ethical Responsibility**: Misuse of this script can be illegal and unethical. Do not use this script to harm or disrupt any systems without explicit permission.

The author is not responsible for any damage caused by the misuse of this script.

## Usage

- `write_large_file`: Generates a large file with random binary data.
- `multiply`: Copies the generated file multiple times.


### Example

```python
def main():
    file = "/path/to/your/file.txt"
    new_dir = "/path/to/destination/directory"
    
    write_large_file(file)
    
    number_of_copies = 10  # Adjust this to a safe number
    multiply(file, new_dir, number_of_copies)
