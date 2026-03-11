from database.tasks_model import get_all_tasks,get_tasks_bystate,add_tasks,update_task_state,delete_task

def get_task(id):
    user_id=id
    print(id)
    data=get_all_tasks(user_id)
    return {"data":data}

def gettask_bystate(user_id,state):
    id=user_id
    state=state
    data=get_tasks_bystate(id,state)
    return {"data":data}

def addtask(id,data):
    user_id=id
    task=data.get("task")
    state=data.get("state")
    res=add_tasks(user_id,task,state)
    return {"Messsage":"Added Successfully"}

def update_task(userid,id,data):
    task_id=id
    state=data.get("state")
    user_id=userid
    res=update_task_state(user_id,task_id,state)
    return {"Message":"Updates Successfully"}

def delete__task(id,userid):
    task_id=id
    id=userid
    res=delete_task(id,task_id)