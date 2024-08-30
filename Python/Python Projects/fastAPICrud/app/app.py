from fastapi import FastAPI


app = FastAPI()

todos = [
    {
        "id": "1",
        "Activity": "Jogging"
    },
    {
        "id": "2",
        "Activity": "writing"
    }
]

# CRUD APP
@app.get("/", tags=['ROOT'])
def home():
    return {"Ping": "Pong"}


#  GET --> Read todo
@app.get('/todo', tags=['todos'])
def get_todo():
    return {'data':todos}

# Post -- Create Todo
@app.post("/todo", tags=['todos'])
def add_todo(todo:dict):
    todos.append(todo)
    return {
        "data": "A todo has been added !"
    }

@app.put("/todos/{id}")
def update_tod(id:int, body:dict):
    for todo in todos:
        if int(todo['id']) == id:
            todo['Activity']= body['Activity']
            return {
                'data': f"Todo with id {id} updated!"
            }
    return {
            'data': f"Todo with id {id} not found!"
        }


#  delete

@app.delete("/todo/{id}")
def delete_todo(id:int):
    for todo in todos:
        if int((todo['id'])) == id:
            todos.remove(todo)
            return {
                'data': f"{id} todo deleted!"
            }
    return{
        "data": "wrong id"
    }