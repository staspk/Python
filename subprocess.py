import subprocess
from .os import C_DRIVE, File

NOTEPAD_PP = File(C_DRIVE, 'Program Files', 'Notepad++', 'notepad++.exe')

class Subprocess:
    def Notepad(file:str):
        """ Opens a file in Notepad++ """
        subprocess.Popen([NOTEPAD_PP, file])