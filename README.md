

# Keylogger Tool

A simple keylogger implemented in Python using the `pynput` library. This tool logs keystrokes to a specified text file for later analysis.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Disclaimer](#disclaimer)
- [License](#license)

## Installation

To run this keylogger, you need to have Python installed on your system. You also need to install the `pynput` library. You can install it using pip:

```bash
pip install pynput
```

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/keylogger.git
    cd keylogger
    ```

2. Run the keylogger script:

    ```bash
    python keylogger.py
    ```

3. The keylogger will start, and you can begin typing. Press the `ESC` key to stop the keylogger. The logged keys will be saved in `key_log.txt`.

### Log File Format

The log file (`key_log.txt`) will have the following format:

```
Keylogger Log
====================
key1 key2 key3 [ENTER] key4 [TAB] key5 [SHIFT]
```

- Regular keys are logged as typed.
- Special keys like Enter, Tab, and Backspace are represented in brackets for clarity.

## Features

- Logs keystrokes to a specified text file.
- Represents special keys like Enter, Tab, Backspace, and Shift for better readability.
- Simple command-line interface to start and stop the keylogger.

## Disclaimer

This tool is intended for educational purposes only. Unauthorized use of a keylogger can violate privacy laws and ethical standards. Ensure you have permission from the device owner before running this tool.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

