from fastapi import FastAPI
from app.database import Base,engine
from app.routers import auth,tasks

Base.metadata.create_all(bind=engine)
app=FastAPI(title="TASK6 雷霆todoAPI")
app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(auth.user_router)

@app.get("/hello_epoch")
def hello_epoch():
    return{"status":"Hello"}