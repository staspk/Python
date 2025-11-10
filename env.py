import os, threading
from definitions import ENV


class Env:
    Vars = {}
    PATH_TO_ENV_FILE = ENV
    loaded = False
    mutex = threading.Lock()

    def Load(key_to_delete:str = None):
        Env.Vars = {}
        if os.path.exists(Env.PATH_TO_ENV_FILE):
            with open(Env.PATH_TO_ENV_FILE, 'r') as file:
                for line in file:
                    if '=' in line:                                     # Each line must have a "=", truthy (string) key,value, to be written into the record
                        key, value = (line.strip()).split('=', 1)       
                        if key and key != key_to_delete:                #  key_to_delete deleted
                            Env.Vars[key] = value
        Env.overwrite()
        Env.loaded = True

    def Save(key:str, value:str):
        Env.mutex.acquire()
        if key and value:
            if Env.loaded is False: Env.Load()
            Env.Vars[key] = value
            Env.overwrite()
        Env.mutex.release()
        
    def Delete(key:str):
        Env.Load(ENV, key_to_delete=key)

    def overwrite():
        directory = os.path.dirname(Env.PATH_TO_ENV_FILE)
        if not os.path.exists(directory): os.makedirs(directory, exist_ok=True)
        lines = ""
        for key, value in Env.Vars.items(): lines += f'{key}={value}\n'
        with open(Env.PATH_TO_ENV_FILE, 'w') as file:
            file.write(lines[:-1])
