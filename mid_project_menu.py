from enum import Enum, auto

class Option(Enum):
    GET_ALL_STUDENTS = auto()
    GET_SPECIFIC_STUDENT = auto()
    SAVE_NEW_STUDENT = auto()
    CHANGE_STUDENT_NAME = auto()
    CHANGE_STUDENT_AGE = auto()
    DELETE_STUDENT = auto()
    EXIT = auto()

def printError(option):
    print("Error: Option [" + option + "] does not exist. Please try again")
