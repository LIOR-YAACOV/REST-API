# from mid_project_menu import Option

def printMenu():
    print("What do you want to do? ")
    print("1. Get students list ")
    print("2. Get a specific student information ")
    print("3. Save a new student ")
    print("4. Change student name ")
    print("5. Change student age")
    print("6. Delete student ")
    print("7. Exit ")

def printStudent(student):
    print(f"ID: {student["id"]}")
    print(f"Name: {student["name"]}")
    print(f"Age: {student["age"]}")
    print("---------------------")

if __name__ == "__main__":
    printMenu()