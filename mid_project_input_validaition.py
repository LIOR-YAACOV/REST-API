import ipaddress
from mid_projet_exceptions import *
from mid_project_menu import Option 
MAX_PORT_NUMBER = 65535
MIN_PORT_NUMBER = 0

def mustBeNumberCheck(value, category):
    if value.isdigit() ==  False or int(value) < 0:
        raise InvalidInput(value, category)
    return int(value)

def getIPaddress():
    ip_addr_string = input("Enter the host address: ")
    try:
        _ = ipaddress.ip_address(ip_addr_string)
    except ValueError as _:
        raise InvalidInput(ip_addr_string, "IP Address")
    return ip_addr_string

def getPort():
    port_number = input("Enter the port: ")
    port_number = mustBeNumberCheck(port_number, "Port")
    if port_number < MIN_PORT_NUMBER or port_number > MAX_PORT_NUMBER:
        raise InvalidInput(port_number, "Port")
    return port_number

def CheckOptionValidity():
    option = input("Enter your choice: ")
    option = mustBeNumberCheck(option, "Option")
    if option < 0 or option > len(Option):
        raise InvalidInput(option, "Option")
    
    return Option(option)

def idCheck(student_id):
    student_id = mustBeNumberCheck(student_id, "Student ID")