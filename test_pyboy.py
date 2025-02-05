# test_pyboy.py

from pyboy import PyBoy
from pyboy.utils import WindowEvent
import time

# Replace with the path to your Pokémon Crystal ROM file.
ROM_PATH = "/mnt/c/Users/phini/Desktop/rom/Pokemon - Crystal Version (UE) (V1.1) [C][!].gbc"

def main():
    # Initialize PyBoy.
    # Use 'headless' mode if you do not want the emulator window to pop up.
    # To see the window, simply omit the 'window_type' parameter.
    pyboy = PyBoy(ROM_PATH, window="null")
    print("Emulator started and ROM loaded successfully!")

    # Let the game run for a few frames to ensure everything is working.
    for i in range(100):  # run 100 ticks
        pyboy.tick()  # advance the emulator one frame
        if i == 10:
            # Simulate pressing the START button after 10 frames.
            print("Pressing START button...")
            pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
        if i == 12:
            # Release the START button after a couple of frames.
            pyboy.send_input(WindowEvent.RELEASE_BUTTON_START)
        
        # Optional: add a small sleep to slow down the loop (useful in non-headless mode)
        time.sleep(0.01)

    print("Test run completed. Shutting down emulator...")
    pyboy.stop()

if __name__ == "__main__":
    main()