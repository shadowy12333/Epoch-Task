from sqlalchemy import Column,Integer,String,Boolean,ForeignKey#为什么这里要声明boolean？因为这里是数据库，告诉数据库这里是bool类型的数据
from sqlalchemy.orm import relationship#ORM 模块就是 Object-Relational Mapping，对象关系映射模块。
from app.database import Base
class Task(Base):
    __tablename__="tasks"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False)
    completed = Column(Boolean,default=False)
    user_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    owner=relationship("User",back_populates="tasks")
