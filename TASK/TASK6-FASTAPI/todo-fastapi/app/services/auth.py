import os
from dotenv import load_dotenv #dotenv的作用：1，防泄漏2，多环境隔离3，集中管理参数
from datetime import datetime,timedelta
import jwt
from pwdlib import PasswordHash
from sqlalchemy.orm import Session
from app.models.user import User

load_dotenv()
SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES",30))#它把“Token 过期时间”从代码里抽出来，变成可配置项，方便开发、测试、生产环境分别设置不同值。

password_hash=PasswordHash.recommended()#密码加密
def create_user(db: Session,username:str,password:str):
    hashed=password_hash.hash(password)
    user=User(username=username,password_hash=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, username: str, password: str):
    user=db.query(User).filter(User.username==username).first()
    if not user:
        return False
    return user

#用户登录成功 → 拿到用户信息
# 复制信息，加入过期时间
# 用 SECRET_KEY 签名生成 JWT
# 返回给客户端，客户端后续请求携带这个 Token
# 服务端用 jwt.decode() 验证签名和过期时间
def create_access_token(data:dict):
    to_encode=data.copy()#把data的值赋给encode
    expire=datetime.utcnow()+timedelta(minutes=EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encode_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt

