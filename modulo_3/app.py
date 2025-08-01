from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(
        id=task_id_control, 
        title=data['title'], 
        description=data.get("description", "")
    )
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso."})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
        "tasks": task_list,
        "total_task": len(task_list)
    }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for activity in tasks:
        if activity.id == id:
            return jsonify(activity.to_dict())
        
    return jsonify({"message": "Não foi possível encontrar a atividade."}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for activity in tasks:
        if activity.id == id:
            task = activity
            break

    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade."}), 404

    data = request.get_json()
    activity.title = data['title']
    activity.description = data['description']
    activity.completed = data['completed']
    return jsonify({"message": "Tarefa atualizada com sucesso."})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for activity in tasks:
        if activity.id == id:
            task = activity
            break
    
    if not task:
        return jsonify({"message": "Não foi possível encontrar a atividade."}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso."})
    

if __name__ == "__main__":
    app.run(debug=True)