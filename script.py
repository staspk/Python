import sys
from typing import Any
from kozubenko.print import Print



def Arg1(value="", *, required=True) -> str:
    """
    **EXAMPLE:**
    ```python
    from kozubenko import script
    search:str = script.Arg1()
    search:str = script.Arg1("Angel of the Lord")  # force value
    search:str = script.Arg1(required=False) or "Angel of the Lord"  # Arg1 preferred, default value if missing
    ```
    """
    arg1 = arg(1)

    if value:
        return value

    if arg1.missing() and required is True:
        Print.red('Arg1 Missing!')
        sys.exit(1)

    if arg1.exists():
        return sys.argv[1]
    
    if required is False:
        return ""
    
    raise Exception("Arg1(): Unexpected Runtime Path")


class arg(int):
    def __init__(self, index):
        self.index = index

    def exists(self):
        if len(sys.argv) < self+1: return False
        return True

    def missing(self):
        if len(sys.argv) < self+1: return True
        return False






#-------------------------------------------
#      Fossil Record
#-------------------------------------------
def ScriptArg_1(default_value=None) -> str:
    """
    NOTE: an older attempt at this

    returns `sys.argv[1]`, default_value, or raises Exception if both are missing
    """
    if len(sys.argv) < 2:
        if default_value is not None:
            return default_value
        raise Exception(f"sys.argv[1] does not exist && no default_value passed into ScriptArg_1. len(sys.argv): {len(sys.argv)}")
    
    return sys.argv[1]