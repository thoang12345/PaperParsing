import os
from pathlib import Path
import re

def clear_terminal():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')
        
def gimmeFileNames(path):
    folder = Path(path)
    file_names = [file.name for file in folder.iterdir() if file.is_file()]

    return file_names