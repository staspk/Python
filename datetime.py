from datetime import datetime


def local_time() -> str:
    """
    **Returns:**
        - local_time in format: `2025-03-18 16:30:55`
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def local_time_as_legal_filename() -> str:
    """
    **Returns:**
        - `datetime.now()` string in format that won't throw exception if used as filename
        e.g: `2025-03-18 16:30:55`
    """
    return datetime.now().strftime('%Y-%m-%d %H.%M.%S')