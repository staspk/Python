

class Parse():
    def first_positive_number(string:str) -> tuple[str|int] | tuple[str|None]:
        """
        Starts at beginning of a string.

        **Returns:**  
            - (rest of string, positive_number:int) ***OR***
            - (string, None)
        """
        number:str = ""
        for i,char in enumerate(string):
            if i == 0:
                if not ('1' <= char <= '9'):
                    return (string, None)
                number += char
            elif '0' <= char <= '9':
                number += char
        
        return (string, int(number))