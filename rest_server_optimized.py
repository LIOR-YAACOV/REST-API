from flask import Flask, request, jsonify

app = Flask(__name__)

students = {1: {"age": 21, "name": "John Doe"}, 2: {"age": 22, "name": "Jane Doe"}}

MAX_ID = 2

@app.route("/students", methods=["GET"])
def getStudents():
    return jsonify(students), 200


@app.route("/students/<int:student_id>", methods=["GET"])
def getStudent(student_id):
    if student_id in students:
        return jsonify(students[student_id]), 200
    return jsonify({"error": "Student not found"}), 404


@app.route("/students", methods=["POST"])
def addStudent():
    global MAX_ID
    data = request.get_json()
    if not data or "name" not in data or "age" not in data:
       return jsonify({"error": "Bad Request, data must include 'name' and 'age'"}), 400
    MAX_ID += 1
    students[MAX_ID] = data
    return jsonify(students[MAX_ID]), 201


@app.route("/students/<int:student_id>", methods=["DELETE"])
def deleteStudent(student_id):
    if student_id in students:
       del students[student_id]
    return jsonify({"message": "Student deleted"}), 200


@app.route("/students/<int:student_id>", methods=["PUT"])
def updateStudent(student_id):
    if student_id in students:
        students[student_id] = request.get_json()
        return jsonify(students[student_id]), 200
    return jsonify({"error": "Student not found"}), 404   

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)