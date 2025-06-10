import sys

def print_list(list:list):
    for item in list:
        print(f'{item}\n')

def print_dict(dict:dict):
    for key, value in dict.items():
        print(f'{key}: {value}\n')
    
def print_yellow(text:str, new_line=True):
    if sys.stdout.isatty():
        print(f"\033[93m{text}\033[0m", end='\n' if new_line else "")
    else:
        print(f"{text}", end="\n" if new_line else "")

def print_white(text:str, new_line=True):
    if sys.stdout.isatty():
        print(f"\033[97m{text}\033[0m", end="\n" if new_line else "")
    else:
        print(f"{text}", end="\n" if new_line else "")

def print_gray(text:str, new_line=True):
    if sys.stdout.isatty():
        print(f"\033[37m{text}\033[0m", end="\n" if new_line else "")
    else:
        print(f"{text}", end="\n" if new_line else "")

def print_dark_gray(text:str, new_line=True):
    if sys.stdout.isatty():
        print(f"\033[90m{text}\033[0m", end="\n" if new_line else "")
    else:
        print(f"{text}", end="\n" if new_line else "")

def print_cyan(text:str, new_line=True):
    if sys.stdout.isatty():
        print(f"\033[96m{text}\033[0m", end="\n" if new_line else "")
    else:
        print(f"{text}", end="\n" if new_line else "")

def print_blue(text:str, new_line=True):
    if sys.stdout.isatty():
        print(f"\033[36m{text}\033[0m", end="\n" if new_line else "")
    else:
        print(f"{text}", end="\n" if new_line else "")

def print_dark_green(text:str, new_line=True):
    if sys.stdout.isatty():
        print(f"\033[32m{text}\033[0m", end="\n" if new_line else "")
    else:
        print(f"{text}", end="\n" if new_line else "")

def print_green(text:str, new_line=True):
    if sys.stdout.isatty():
        print(f"\033[92m{text}\033[0m", end="\n" if new_line else "")
    else:
        print(f"{text}", end="\n" if new_line else "")

def print_dark_red(text:str, new_line=True):
    if sys.stdout.isatty():
        print(f"\033[31m{text}\033[0m", end="\n" if new_line else "")
    else:
        print(f"{text}", end="\n" if new_line else "")

def print_red(text:str, new_line=True):
    if sys.stdout.isatty():
        print(f"\033[91m{text}\033[0m", end="\n" if new_line else "")
    else:
        print(f"{text}", end="\n" if new_line else "")

def print_dark_yellow(text:str, new_line=True):
    if sys.stdout.isatty():
        print(f"\033[33m{text}\033[0m", end="\n" if new_line else "")
    else:
        print(f"{text}", end="\n" if new_line else "")

def print_yellow(text:str, new_line=True):
    if sys.stdout.isatty():
        print(f"\033[93m{text}\033[0m", end="\n" if new_line else "")
    else:
        print(f"{text}", end="\n" if new_line else "")