from fastapi import APIRouter,HTTPException,Depends,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate,UserResponse,Token
from app.schemas.task import TaskCreate
from app.services import auth as auth_service
from app.dependencies import get_current_user
from app.models.user import User

router =APIRouter(prefix="/auth",tags=["用户"])
user_router=APIRouter(prefix="/users",tags=["用户"])

@router.post("/register",response_model=UserResponse,status_code=201)
def register(user_data: UserCreate,db: Session = Depends(get_db)):
    existing_user=db.query(User).filter(User.username==user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="User with that username already exists")
    user=auth_service.create_user(db,user_data.username,user_data.password)
    return user

@router.post("/login",response_model=Token)
def login(from_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    user=auth_service.authenticate_user(db,from_data.username,from_data.password)
    if not user:
        raise HTTPException(status_code=401,detail="Incorrect username or password")
    token=auth_service.create_access_token(data={"sub":user.username})
    return {"access_token":token,"token_type":"bearer"}
@router.get("/me",response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user










