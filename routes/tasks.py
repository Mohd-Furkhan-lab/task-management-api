from fastapi import APIRouter,Request
from controller.task_controller import get_alltask_controller,gettaskbystate_controller,addtask_controller,updatetask_controller,deletetask_contoller
tasks=APIRouter(prefix="/tasks",tags=["Tasks"])
from middelware.jwt_decorator import jwt_required

@tasks.get('/')
@jwt_required
async def gettasks(request:Request,state:str|None=None,user_id:int|None=None):
    data=request
    if state:
        return await gettaskbystate_controller(data,state)
    return await get_alltask_controller(request)

@tasks.post('/')
@jwt_required
async def addtaks(request:Request):
    data=request
    return await addtask_controller(request,data)

@tasks.put('/{id}')
@jwt_required
async def update(request:Request,id:int):
    data=request
    return await updatetask_controller(request,id,data)


@tasks.delete('/{id}')
@jwt_required
async def homeapi(request:Request,id:int):
    data=request
    return await deletetask_contoller(request,id)