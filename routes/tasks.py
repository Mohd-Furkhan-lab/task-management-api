from fastapi import APIRouter,Request
from controller.task_controller import get_alltask_controller,gettaskbystate_controller,addtask_controller,updatetask_controller,deletetask_contoller
tasks=APIRouter(prefix="/tasks",tags=["Tasks"])

@tasks.get('/')
async def gettasks(request:Request,state:str|None=None,user_id:int|None=None):
    data=await request.json()
    if state:
        return await gettaskbystate_controller(data,state)
    return await get_alltask_controller(data)

@tasks.post('/')
async def addtaks(request:Request):
    data=await request.json()
    return await addtask_controller(data)

@tasks.put('/{id}')
async def update(id:int,request:Request):
    data=await request.json()
    return await updatetask_controller(id,data)


@tasks.delete('/{id}')
async def homeapi(id:int,request:Request):
    data=await request.json()
    return await deletetask_contoller(id,data)