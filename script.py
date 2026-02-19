import sys
from typing import Any
from kozubenko.print import Print



def Arg1(required=True) -> Any:
    """
    **EXAMPLE:**
    ```python
    from kozubenko import script
    search:str = script.Arg1()
    ```
    """
    if len(sys.argv) < 2:
        Print.red('search.py: Missing: arg1 -> search:str')
        sys.exit(1)
    return sys.argv[1]



class Script:

    @staticmethod
    def Arg1(required=True) -> Any:
        if len(sys.argv) < 2:
            Print.red('search.py: Missing: arg1 -> search:str')
            sys.exit(1)
        return sys.argv[1]







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