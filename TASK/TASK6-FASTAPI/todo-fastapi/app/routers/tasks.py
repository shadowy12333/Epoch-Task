from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from sqlalchemy.sql.functions import current_user

from app.database import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.dependencies import get_current_user
from app.models.user import User
from app.models.task import Task

router = APIRouter(prefix="/tasks",tags=["任务"])

@router.get("",response_model=List[TaskResponse])
def get_tasks(current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    tasks=db.query(Task).filter(Task.user_id==current_user.id).order_by(Task.id.desc()).all()
    return tasks

@router.post("",response_model=TaskResponse,status_code=201)
def create_task(task_data:TaskCreate,current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    new_task=Task(title=task_data.title,completed=False,user_id=current_user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.patch("/{task_id}",response_model=TaskResponse)
def update_task(task_id:int,task_data:TaskUpdate,current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    task=db.query(Task).filter(Task.id==task_id,Task.user_id==current_user.id).first()
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    update_data=task_data.model_dump(exclude_unset=True)
    for key,value in update_data.items():
        setattr(task,key,value)
        db.commit()
        db.refresh(task)
        return task
@router.delete("/{task_id}")
def task_delete(task_id:int,current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    task=db.query(Task).filter(Task.id==task_id,Task.user_id==current_user.id).first()
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message":"Task deleted"}










