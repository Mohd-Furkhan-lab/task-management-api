from database.tasks_model import get_all_tasks,get_tasks_bystate,add_tasks,update_task_state,delete_task

def get_task(data):
    id=data.get("user_id")
    print(id)
    data=get_all_tasks(id)
    return {"data":data}

def gettask_bystate(data,state):
    id=data.get("user_id")
    state=state
    data=get_tasks_bystate(id,state)
    return {"data":data}

def addtask(data):
    user_id=data.get("user_id")
    task=data.get("task")
    state=data.get("state")
    res=add_tasks(user_id,task,state)
    return {"Messsage":"Added Successfully"}

def update_task(id,data):
    task_id=id
    state=data.get("state")
    id=data.get("user_id")
    res=update_task_state(id,task_id,state)
    return {"Message":"Updates Successfully"}

def delete__task(id,data):
    id=id
    task_id=data.get("task_id")
    res=delete_task(id,task_id)