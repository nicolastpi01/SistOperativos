from enum import Enum

class State(Enum):
    NEW        =        1
    READY      =        2
    RUNNING    =        3
    WAITING    =        4
    TERMINATED =        5