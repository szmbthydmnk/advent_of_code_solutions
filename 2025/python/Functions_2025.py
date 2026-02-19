import functools
from pathlib import Path
from typing import Iterator

def read_lines(file_path: Path) -> Iterator[str]:
    """
    Read lines from a file and yield them as stripped strings.

    :param file_path: Path to the file to be read
    :type file_path: Path
    :return: Iterator yielding stripped lines from the file
    :rtype: Iterator[str]
    """
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    text_lines = file_path.read_text(encoding='utf-8')
    for line in text_lines.splitlines():
        yield line.strip()

#################################################################################


def log_call(func):
    """Simple decorator to log function calls."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper



def SeparateRanges(File : str) -> list:
    """Separate ranges from a file into a list of integer pairs."""
    Ranges = []             # List to hold the ranges
    for line in File:       # There is probably only one line in this file but whatever
        line = line.strip() 
        range_pairs = line.split(',')   # Split by comma to get individual ranges
        for pair in range_pairs:        # Split each range into start and end
            start, end = pair.split('-')    
            Ranges.append([int(start), int(end)])
    return Ranges



def is_ID_repeated_twice(ID: int) -> bool:
    str_ID = str(ID)

    # So far redundant but check for leading zeros
    if str_ID[0] == '0':
        return False

    # Check for repeated sequences
    
    length = len(str_ID)
    
    if length % 2 == 0:
        half = length // 2
        if str_ID[:half] == str_ID[half:]:
            return False
    
    return True


def is_ID_repeated_Nth(ID: int) -> bool:
    str_ID = str(ID)

    # Redundant check: Check for leading zeros
    if str_ID[0] == '0':
        return False

    length = len(str_ID)

    # Check for any lengh for the repeated sequence
    for sequence_length in range(1, length // 2 + 1):
        if length % sequence_length == 0:
            length_divisor = length // sequence_length

            if str_ID[:sequence_length] * length_divisor == str_ID:
                return False
    
    return True
