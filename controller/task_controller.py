from services.task_services import get_task, gettask_bystate, addtask, update_task, delete__task


async def get_alltask_controller(data):
    return get_task(data)


async def gettaskbystate_controller(data,state):
    return gettask_bystate(data,state)


async def addtask_controller(data):
    return addtask(data)


async def updatetask_controller(id: int, data):
    return update_task(id, data)


async def deletetask_contoller(id: int, data):
    return delete__task(id, data)