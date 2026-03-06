from fastapi import APIRouter

tasks=APIRouter(prefix="/tasks",tags=["Tasks"])

@tasks.get('/')
def homeapi():
    return "Home Api"

@tasks.post('/')
def homeapi():
    return "post"

@tasks.put('/{id}')
def homeapi(id):
    return f"{id} updated successfully"

@tasks.delete('/{id}')
def homeapi(id):
    return f"{id} deleted successfully"
