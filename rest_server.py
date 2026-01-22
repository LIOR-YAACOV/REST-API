from flask import Flask, request, jsonify

app = Flask(__name__)

students = [
        {
            "age": 21,
            "id": 1,
            "name": "John Doe"
        },
        {
            "age": 22,
            "id": 2,
            "name": "Jane Doe"
        }
    ]

@app.route("/students", methods=["GET"])
def getStudents():
    return jsonify({"students": students}), 200


@app.route("/students/<int:student_id>", methods=["GET"])
def getStudent(student_id):
    for student in students:
      if student_id == student["id"]:
         return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404


@app.route("/students", methods=["POST"])
def addStudent():
    data = request.get_json()
    if not data or "name" not in data or "age" not in data:
       return jsonify({"error": "Bad Request, data must include 'name' and 'age'"}), 400
    new_id = 0
    if len(students) > 0:
        new_id = students[-1]["id"] + 1
    new_student = {"name": data["name"], "age": data["age"], "id": new_id}
    students.append(new_student)
    return jsonify(new_student), 201


@app.route("/students/<int:student_id>", methods=["DELETE"])
def deleteStudent(student_id):
    global students
    new_students = []
    to_delete_found = False
    for student in students:
      if student_id != student["id"]:
         new_students.append(student)
      else:
        to_delete_found = True
    students = new_students
    if to_delete_found:
        return jsonify({"message": "Student deleted"}), 200
    return jsonify({"error": "Student not found"}), 404


@app.route("/students/<int:student_id>", methods=["PUT"])
def updateStudent(student_id):
    for student in students:
      if student_id == student["id"]:
        data = request.get_json()
        student["name"] = data["name"]
        student["age"] = data["age"]
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404   

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)