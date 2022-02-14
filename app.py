from flask import Flask, jsonify
app = Flask(__name__)
tasks = [
    {
        'id': 0,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit',
        'done': False
    },
    {
        'id': 1,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]
@app.route('/')
def index():
    return "welcome to proton demo - updated!!"
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    return jsonify({'task': tasks[task_id]})
# curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/tasks
@app.route('/tasks',methods=['POST'])
def create():
    Create_task={
        'id': 2,
        'title': 'Buy food',
        'description': 'Need to find a good restaurant',
        'done': False
    }
    tasks.append(Create_task)
    return jsonify({'created':Create_task})
# curl -i -H "Content-Type: Application/json" -X PUT http://localhost:5000/tasks/2
@app.route('/tasks/<int:task_id>',methods=['PUT'])
def task_update(task_id):
    tasks[task_id]['done']="True"
    return jsonify({'task':tasks[task_id]})
# curl -i -H "Content-Type: Application/json" -X DELETE http://localhost:5000/tasks/2
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete(task_id):
    tasks.remove(tasks[task_id])
    return jsonify({'result':True})

if __name__ == "__main__":
   app.run(host='0.0.0.0',port=80)
