class Task:   #开场白，为输入的东西贴上标签
    def __init__(self, id:int,title:str,completed:bool=False):
        self.id=id
        self.title=title
        self.completed=completed

    def to_dict(self):#把输入的东西转化为字典，为后续json读取铺垫
        return{"id":self.id,"title":self.title,"completed":self.completed}

def add_task(tasks,title):#创建id，使每个任务的id唯一，创建这个任务
    new_id=max([t.id for t in tasks],default=0)+1
    tasks.append(Task(id=new_id,title=title))
    return tasks

def find_task(tasks,task_id):#查找任务
    for task in tasks:
        if task.id==task_id:##
            return task
    return None#循环走完才应该退出

def delete_task(tasks,task_id):#查找删除任务
    task = find_task(tasks,task_id)
    if task:
        tasks.remove(task)
        return True
    return False


