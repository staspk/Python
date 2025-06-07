import random, string


def AssertClass(var_name:str, obj, class_type):
    if type(obj) is not class_type:
        raise Exception(f"AssertClass({var_name}): must be a {class_type.__name__}, not: {type(obj).__name__}")
    
def AssertList(var_name:str, the_list:list, min_len:int=1, max_len:int=None):
    if not isinstance(the_list, list):
        raise Exception(f"AssertList({var_name}): must be a list, not: {type(the_list)}")
    if len(the_list) < min_len:
        raise Exception(f"AssertList({var_name}): length of list under min_len: {min_len}")
    if(max_len) and len(the_list) > max_len:
        raise Exception(f"AssertList({var_name}): length of list exceeds max_len: {max_len}")

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