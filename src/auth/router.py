from fastapi import APIRouter
from src.auth.schemas import UserCreateSchema,UserDetailsSchema
from src.auth.dependencies import UserServiceDep
from src.utils import resp_200,ResponseModel
from typing import Generic
userRouter = APIRouter()



@userRouter.post("/users",tags=["users"],response_model=ResponseModel[UserDetailsSchema])
def createUser(user_schema: UserCreateSchema,userService: UserServiceDep):
    user = userService.createUser(user_schema)
    return resp_200(data=user)

@userRouter.get("/users/{user_id}",tags=["users"],response_model=ResponseModel[UserDetailsSchema])
def getUserById(user_id:int,userService: UserServiceDep):
    user = userService.getUserById(user_id)
    return resp_200(data=user)


@userRouter.get("/users/",tags=["users"],response_model=ResponseModel[UserDetailsSchema])
def getUserByName(name:str,userService: UserServiceDep):
    user = userService.getUserByName(name)
    return resp_200(data=user)


