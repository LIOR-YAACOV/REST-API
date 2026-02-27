from mid_project_requests import *
from mid_project_menu import Option
from mid_project_input_validaition import *
from mid_project_utils import *

if __name__ == "__main__":
    try:
        ip_addr = getIPaddress()
        port = getPort()
        while True:
            printMenu()
            option = CheckOptionValidity()
            if option == Option.GET_ALL_STUDENTS:
                getAllStudent(ip_addr, port)
            if option == Option.GET_SPECIFIC_STUDENT:
                getSpecificStudent(ip_addr, port)
            if option == Option.SAVE_NEW_STUDENT:
                addStudent(ip_addr, port)
            if option == Option.CHANGE_STUDENT_NAME:
                changesStudentName(ip_addr, port)
            if option == Option.CHANGE_STUDENT_AGE:
                changeStudentAge(ip_addr, port)
            if option == Option.DELETE_STUDENT:
                deleteStudent(ip_addr, port)
            if option == Option.EXIT:
                print("Exiting the program...")
                break
            
    except PortNumException as e:
        print(e)
    except IPAddrException as e:
        print(e)
    except OptionException as e:
        print(e)
    except InvalidInput as e:
        print(e)  
    