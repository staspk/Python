import os
import random, string

def AssertBool(var_name:str, _bool):
    """
    Use to enforce type annotations. Will raise Exception if _bool is not a bool.
    """
    if type(_bool) is not bool:
        raise Exception(f"AssertBool({var_name}): must be a bool (True or False), not: {type(_bool)}")

def AssertClass(var_name:str, obj, _class):
    """
    Use to enforce type annotations. Will raise Exception if obj is not a type of _class.
    """
    if type(obj) is not _class:
        raise Exception(f"AssertClass({var_name}): must be a {_class.__name__}, not: {type(obj).__name__}")

def AssertInt(var_name:str, _int:int, min_val:int=None, max_val:int=None):
    """
    Use to enforce type annotations. Will raise Exception:
    * if _int is not a int
    * len(_list) < min_val (*optional*)
    * len(_list) > max_val (*optional*)
    """
    if type(_int) is not int:
        raise Exception(f"AssertInt({var_name}): must be an int, not: {type(_int)}")
    if(min_val) and _int < min_val:
        raise Exception(f"AssertInt({var_name}): value of int < min_val: {min_val}")
    if(max_val) and _int > max_val:
        raise Exception(f"AssertInt({var_name}): value of int > max_val: {max_val}")

def AssertList(var_name:str, _list:list, min_len:int=None, max_len:int=None):
    """
    Use to enforce type annotations. Will raise Exception:
    * if _list is not a list
    * len(_list) < min_len (*optional*)
    * len(_list) > max_len (*optional*)
    """
    if not type(_list) is list:
        raise Exception(f"AssertList({var_name}): must be a list, not: {type(_list)}")
    if(min_len) and len(_list) < min_len:
        raise Exception(f"AssertList({var_name}): length of list under min_len: {min_len}")
    if(max_len) and len(_list) > max_len:
        raise Exception(f"AssertList({var_name}): length of list exceeds max_len: {max_len}")

def AssertPathExists(var_name:str, path:str):
    """
    Use to enforce path exists. If not, raises Exception.
    * Equivalent to Powershell's Test-Path.
    """
    if not os.path.exists(path):
        raise Exception(f"parse_footnotes_html({var_name}): html file to parse does not exist. var_name: {path}")

class Utils:
    def get_randomized_string(str_length):
        return ''.join(random.choices(string.ascii_letters, k=str_length))
    
    def list_to_str(list:list[str], char_separator = " "):
        """
        `list_to_str(['a', 'b', 'c'], ';') -> 'a;b;c'`
        """
        string = ""
        for i in range(len(list)):
            if i == (len(list) - 1):
                string += list[i]
            else:
                string += list[i] + char_separator
        
        return string