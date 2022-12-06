from collections import deque
import doctest
from typing import Optional

FILE_INPUT = "puzzles/day06_input.txt"
BUFFER_START_OF_PACKET = 4
BUFFER_START_OF_MESSAGE = 14


def index_after_marker(line: str, buffer_size: int) -> Optional[int]:
    """
    >>> index_after_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4)
    7
    >>> index_after_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14)
    19
    """
    buffer: deque[str] = deque(maxlen=buffer_size)
    for i, char in enumerate(line):
        buffer.append(char)
        if len(set(buffer)) == buffer_size:
            return i + 1
    return None


if __name__ == "__main__":
    assert not doctest.testmod().failed

    with open(FILE_INPUT) as f:
        lines = [line.rstrip() for line in f.readlines() if line]

    print(index_after_marker(lines[0], BUFFER_START_OF_PACKET))
    print(index_after_marker(lines[0], BUFFER_START_OF_MESSAGE))
    exit()
