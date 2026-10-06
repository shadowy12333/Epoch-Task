from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
import jwt
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.services.auth import SECRET_KEY,ALGORITHM

oauth2_schema=OAuth2PasswordBearer(tokenUrl="/auth/login")
# OAuth2 Bearer Token 认证 的安全方案声明：
def get_current_user(token:str=Depends(oauth2_schema),db:Session=Depends(get_db)):
    credentials_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=payload.get("sub")
        if username is None:
            raise credentials_exception

    except jwt.PyJWTError:
        raise credentials_exception
    user=db.query(User).filter(User.username==username).first()
    if user is None:
        raise credentials_exception#凭证异常
    return user











