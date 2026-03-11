from services.task_services import get_task, gettask_bystate, addtask, update_task, delete__task
from fastapi import Request

async def get_alltask_controller(request: Request):
    id=request.state.user_id
    if not id:
        return {"Message":"Request Body Not Found"}
    return get_task(id)


async def gettaskbystate_controller(request:Request,state):
    id=request.state.user_id
    return gettask_bystate(id,state)


async def addtask_controller(request:Request,data):
    data=data=await data.json()
    user_id=request.state.user_id
    return addtask(user_id,data)


async def updatetask_controller(request:Request,id: int, data):
    data=await data.json()
    user_id=request.state.user_id
    return update_task(user_id,id, data)


async def deletetask_contoller(request:Request,id: int):
    user_id=request.state.user_id
    return delete__task(id,user_id)