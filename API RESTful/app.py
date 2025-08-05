from flask import Flask, jsonify, request, redirect
from flask_restx import Api, Resource, fields, Namespace

app = Flask(__name__)

# Redireccionamos la raiz a la página de la documentación
# antes de instanciar la Api con Flask-RESTX
@app.route("/", strict_slashes=False)
def home():
    return redirect("/docs")

# Instanciamos la Api
api = Api(app, version="1.1", title="API de Tareas", description="Una API RESTful para gestionar tareas", doc="/docs")

# Definimos un namespace con una descripción
ns_tasks = Namespace(
    'Tasks',
    description='Operaciones sobre tareas (crear, listar, actualizar, eliminar)'
)

# Modelo para tareas
task_model = ns_tasks.model('Task', {
    'id': fields.Integer(readonly=True, description='El identificador único de la tarea'),
    'title': fields.String(required=True, description='Título de la tarea'),
    'description': fields.String(description='Descripción de la tarea'),
    'done': fields.Boolean(description='Estado de la tarea', default=False)
})

# Modelo de datos (lista inicial de tareas)
tasks = [
    {"id": 1, "title": "Crear un servicio RESTful", "description": "Implementar documentación Swagger y testear endpoints", "done": False},
    {"id": 2, "title": "Hacer ejercicio", "description": "Ir al gimnasio", "done": True},
]

# Leer todas las tareas y crear una nueva tarea
@ns_tasks.route('/')
class TaskList(Resource):
    def get(self):
        """Leer todas las tareas"""
        return tasks

    @ns_tasks.expect(task_model, validate=True)
    def post(self):
        """Crear una nueva tarea"""
        data = ns_tasks.payload  # Accede al JSON enviado desde el cliente
        new_task = {
            "id": len(tasks) + 1,
            "title": data["title"],
            "description": data.get("description", ""),
            "done": data.get("done", False)
        }
        tasks.append(new_task)
        return new_task, 201


# Leer una tarea específica, actualizar una tarea y eliminar una tarea
@ns_tasks.route('/<int:task_id>')
@ns_tasks.response(404, 'Tarea no encontrada')
@ns_tasks.param('task_id', 'El ID de la tarea')
class Task(Resource):
    def get(self, task_id):
        """Leer una tarea por ID"""
        task = next((task for task in tasks if task["id"] == task_id), None)
        if task is None:
            ns_tasks.abort(404)
        return task

    @ns_tasks.expect(task_model, validate=True)
    def put(self, task_id):
        """Actualizar una tarea por ID"""
        task = next((task for task in tasks if task["id"] == task_id), None)
        if task is None:
            ns_tasks.abort(404)
        
        data = ns_tasks.payload
        task["title"] = data.get("title", task["title"])
        task["description"] = data.get("description", task["description"])
        task["done"] = data.get("done", task["done"])
        return task

    def delete(self, task_id):
        """Eliminar una tarea por ID"""
        global tasks
        task = next((task for task in tasks if task["id"] == task_id), None)
        if task is None:
            ns_tasks.abort(404)

        tasks = [task for task in tasks if task["id"] != task_id]
        return {'message': 'Tarea eliminada correctamente'}

# Registramos el namespace bajo la ruta /tasks
api.add_namespace(ns_tasks, path='/tasks')

if __name__ == "__main__":
    app.run(debug=True)