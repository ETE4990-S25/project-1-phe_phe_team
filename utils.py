import os
import time
import sys

def clear_screen():
    "Clear the console screen."
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.03):
    "print text with a typing effect."
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()