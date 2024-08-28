import pyautogui
import random
import time
import threading
import keyboard

stop_flag = False

def move_cursor_randomly():
    global stop_flag
    screen_width, screen_height = pyautogui.size()
    
    while not stop_flag:
        # Generate random coordinates within the screen boundaries
        x = random.randint(0, screen_width - 1)
        y = random.randint(0, screen_height - 1)
        
        # Move the cursor to the random coordinates
        pyautogui.moveTo(x, y)
        
        # Wait for 10 seconds
        time.sleep(120) # 600

def listen_for_quit():
    global stop_flag
    keyboard.wait('q')
    stop_flag = True
    print("Quitting...")

if __name__ == "__main__":
    print("Automated cursor control activated... Enter 'q' to stop.")
    # Start the cursor movement in a separate thread
    move_thread = threading.Thread(target = move_cursor_randomly)
    move_thread.start()
    
    # Listen for the quit signal
    listen_for_quit()
    
    # Wait for the move thread to finish
    move_thread.join()
