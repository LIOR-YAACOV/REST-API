import requests
from mid_project_utils import printStudent
from mid_project_input_validaition import mustBeNumberCheck
STUDENT_API = "students"

def getServerURL(ip_address, port):
    return "http://" + ip_address + ":" +  str(port)
    
def getAllStudent(ip_address, port):
    all_students_url = getServerURL(ip_address, port) + "/" + STUDENT_API
    response = requests.get(all_students_url)
    if response.status_code == 200:
        students = response.json()["students"]
        print("-- Students List --")
        for student in students:
            printStudent(student)
    else:
        print("Response error")

def getSpecificStudent(ip_address, port):
    all_students_url = getServerURL(ip_address, port) + "/" + STUDENT_API
    student_id = input("Enter the student ID: ")
    specific_student_url = all_students_url + "/" + str(student_id)
    response = requests.get(specific_student_url)
    if response.status_code == 200:
        student = response.json()
        print("-- Students Information --")
        printStudent(student)
    else:
        print("Error: Student not found")

def addStudent(ip_address, port):
    student_name = input("Enter student name: ")
    student_age = input("Enter student age: ")
    student_age = mustBeNumberCheck(student_age, "age")
    student_data = {
        "name": student_name,
        "age": student_age
    }
    all_students_url = getServerURL(ip_address, port) + "/" + STUDENT_API
    response = requests.post(all_students_url, json=student_data)
    if response.status_code == 201:
        print("Student created Successfully:")
        printStudent(response.json())
    else:
        print("Error: Student was not created successfully")

def changesStudentName(ip_address, port):
    student_id = input("Enter the student ID: ")
    all_students_url = getServerURL(ip_address, port) + "/" + STUDENT_API
    specific_student_url = all_students_url + "/" + student_id
    
    new_name = input("Enter new student name: ")
    
    response = requests.get(specific_student_url)
    if response.status_code != 200:
        print("Error: student does not exist")
        return
    
    student = response.json()
    updated_student_data = {"name": new_name, "age": student["age"]}
    change_student_response = requests.put(specific_student_url, json=updated_student_data)
    if change_student_response.status_code == 200:
        print("Student name updated succsesfully")
    else:
        print("Error: student name was not updated succsesfully")
    

def changeStudentAge(ip_address, port):
    student_id = input("Enter the student ID: ")
    all_students_url = getServerURL(ip_address, port) + "/" + STUDENT_API
    specific_student_url = all_students_url + "/" + student_id
    
    new_age = input("Enter new student age: ")
    new_age = mustBeNumberCheck(new_age, "Age")
    
    response = requests.get(specific_student_url)
    if response.status_code != 200:
        print("Error: student does not exist")
        return
    
    student = response.json()
    updated_student_data = {"name": student["name"], "age": new_age}
    change_student_response = requests.put(specific_student_url, json=updated_student_data)
    if change_student_response.status_code == 200:
        print("Student age updated succsesfully")
    else:
        print("Error: student age was not updated succsesfully")

def deleteStudent(ip_address, port):
    all_students_url = getServerURL(ip_address, port) + "/" + STUDENT_API
    student_id = input("Enter the student ID: ")
    specific_student_url = all_students_url + "/" + str(student_id)
    
    response = requests.delete(specific_student_url)
    if response.status_code == 200:
        print("Student seleted Successfully")
    else:
        print("Error: student delete failed")
