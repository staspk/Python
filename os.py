import os, shutil, pathlib, subprocess, pickle
from typing import Any, Self


C_DRIVE = "C:\\"
def WINDOWS_APPDATA(): return os.getenv("APPDATA")

def Parent(path:str) -> str:
    return os.path.dirname(path)

def Application_Data_Directory(app_name:str) -> str:
    """
    - **Windows:** *`C:/Users/{user}/AppData/Roaming/{ApplicationName}`*  
    - **Mac/Linux:** *`home/{user}/.{ApplicationName}/`*
    """
    if os.name == 'nt': path = os.path.join(os.getenv("APPDATA"), app_name)
    else:               path = os.path.join(os.path.expanduser("~"), f'.{app_name}')
    os.makedirs(path, exist_ok=True)
    return path

def Downloads_Directory() -> str:
    r"""
    - **Windows:** returns downloads value under: `Registry:SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders`
    - **Mac/Linux:** returns `~/Downloads`
    """
    if os.name == 'nt':
        import winreg
        key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'

        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key) as key:
            Downloads_Directory = winreg.QueryValueEx(key, downloads_guid)[0]
            return Downloads_Directory
        
    elif os.name == 'posix':  # Both Mac and Linux
        return os.path.join(os.path.expanduser("~"), "Downloads")
    
class Path(str):
    """
    Allows one to use `Path` constructor instead of `os.path.join`. Is a `str`, at it's core.

    **Example:**
        >>>  Path(SPOTIFY_USER_DATA_DIR, self.name, 'Spotify Extended Streaming History')
    """
    def __new__(cls, path, *paths:str):
        return super(Path, cls).__new__(cls, os.path.join(path, *(path for path in paths if path is not None)))
    
    def exists(self):
        return os.path.exists(self)

class File(Path):
    """
    inherits `Path` -> allows you to use `File()` constructor instead of `os.path.join`. Is a `str`, at it's core.
    """
    def fp(self, mode='w', encoding=None): return open(self, mode, encoding=encoding)
    
    def contents(self, encoding=None) -> str:
        with open(self, 'r', encoding=encoding) as file:
            return file.read()
        
    def append(self, string:str, encoding='UTF-8') -> Self:
        directory = os.path.dirname(self)
        if not os.path.exists(directory): os.makedirs(directory, exist_ok=True)

        with open(self, 'a', encoding=encoding) as file:
            file.write(string)

        return self

    def save(self, string:str, encoding='UTF-8') -> Self:
        directory = os.path.dirname(self)
        if not os.path.exists(directory): os.makedirs(directory, exist_ok=True)

        with open(self, 'w', encoding=encoding) as file:
            file.write(string)

        return self
    
    def save_binary(self, obj:Any) -> Self:
        """ Uses pickle, btw """
        directory = os.path.dirname(self)
        if not os.path.exists(directory): os.makedirs(directory, exist_ok=True)

        with open(self, 'wb') as file:
            pickle.dump(obj, file)

        return self
    
    def load_binary(self) -> Any:
        """ Uses pickle, btw """
        with open(self, 'rb') as file:
            return pickle.load(file)

    def open(self) -> Self:
        """ Opens in Notepad++ """
        NOTEPAD_PP = File(C_DRIVE, 'Program Files', 'Notepad++', 'notepad++.exe')
        subprocess.Popen([NOTEPAD_PP, self])
        return self

    def exists(self) -> Self|None:
        if os.path.isfile(self): return self
        return None
    
    def move(self, destination:str) -> Self:
        """ Will overwrite file at destination, if exists """
        if os.path.exists(self):
            if not os.path.exists(Parent(destination)): os.makedirs(Parent(destination), exist_ok=True)
            pathlib.Path(self).replace(destination)

    def delete(self) -> Self:
        if os.path.exists(self): pathlib.Path(self).unlink(self)

    def Exists(path:str, *paths:str) -> str|None:
        """
        Returns the `path`, or `False`
        """
        file = os.path.join(path, *paths)
        if os.path.isfile(file): return file
        return None
    
class LogFile(File):
    def prepend(self, text:str, encoding='UTF-8'):
        existing_text = ""
        if self.exists():
            existing_text = self.contents(encoding=encoding)

        with open(self, 'w', encoding=encoding) as file:
            file.write(text + existing_text)

class Directory(Path):
    """
    inherits `Path` -> allows you to use `Directory()` constructor instead of `os.path.join`. Is a `str`, at it's core.
    """
    @property
    def parent(self) -> Directory:
        return Directory(pathlib.Path(self).parent)

    def exists(self) -> Self|None:
        if os.path.isdir(self): return self
        return None
    
    def empty(self) -> Self|None:
        """ i.e: no files in directory """
        return self if not any(pathlib.Path(self).iterdir()) else None

    def delete(self) -> Self:
        if os.path.isdir(self): shutil.rmtree(self)
    
    def Exists(path:str, *paths:str) -> str|False:
        """
        Returns the combined `path`, or `Falsse`
        """
        dir = os.path.join(path, *paths)
        if os.path.isdir(dir): return dir
        return None
    
    def Files(path:str, filter:str=None) -> list[File]:
        """
        **Returns:**
            `List<absolute paths>` at `path`. Can `filter` by `[str] in filename`.

        **Example:**
        >>>  if files := Directory.files(EXTENDED_STREAMING_HISTORY, 'Streaming_History_Audio'):
        """
        files:list[File] = []
        if os.path.exists(path):
            for file in os.listdir(path):
                if filter and filter in file: files.append(File(path, file))
                else:                         files.append(File(path, file))
        return files
