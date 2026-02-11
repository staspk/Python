class Str:
    def From(items:list, separator="\n\n") -> str:
        """ Transforms list into a pretty string. """
        string = ""
        for item in items:
            string += f'{item}{separator}'

        return string[:-1]

class String:
    def isEmptyOrWhitespace(string:str) -> bool:
        if not string or string.isspace():
            return True
        return False