from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = {}

MAX_TASK_ID = 0

@app.route("/tasks", methods=["GET"])
def getTasks():
    return jsonify(tasks), 200

@app.route("/tasks/<int:task_id>", methods=["GET"])
def getTask(task_id):
    if task_id in tasks:
        return jsonify(tasks[task_id]), 200
    return jsonify({"error": "Task not found"}), 404

@app.route("/tasks", methods=["POST"])
def addTask():
    global MAX_TASK_ID
    task_data = request.get_json()
    if not task_data or "title" not in task_data or "description" not in task_data:
        return jsonify({"error": "Bad Request: data must include 'title' and 'description' "}), 400
    MAX_TASK_ID += 1
    task_data["completed"] = False
    task_data["id"] = MAX_TASK_ID
    tasks[MAX_TASK_ID] = task_data
    return jsonify(tasks[MAX_TASK_ID]), 201

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def deletetTask(task_id):
    if task_id in tasks:
       del tasks[task_id]
    return jsonify({"message": "Student deleted"}), 200


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def updatetTask(task_id):
    if task_id in tasks:
        new_task_data = request.get_json()
        new_task_data["completed"] = False
        new_task_data["id"] = task_id
        tasks[task_id] = new_task_data
        return jsonify(tasks[task_id]), 200
    return jsonify({"error": "Student not found"}), 404   

@app.route("/tasks/<int:task_id>/complete", methods=["GET"])
def completeTask(task_id):
    if task_id in tasks:
        task = tasks[task_id]
        task["completed"] = True
        response = {"message": "Task marked as completed", "task": task}
        return jsonify(response), 200

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5050)