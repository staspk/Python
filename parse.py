

def substring_between(string:str, char1:str|int, char2:str|int) -> str:
    """ No safety built-in - will throw! """
    right = string.split(f'{char1}')[1]
    return right.split(f'{char2}')[0]
