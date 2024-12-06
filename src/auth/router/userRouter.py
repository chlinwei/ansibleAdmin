from fastapi import APIRouter
from src.auth.schemas import UserCreateSchema,UserDetailsSchema,MenuDetailsSchema,MenuCreateSchema
from src.auth.dependencies import UserServiceDep
from src.utils import resp_200,ResponseModel,resp_pagination
from fastapi_pagination import Page,pagination_ctx
from fastapi import Depends
userRouter = APIRouter()



@userRouter.post("/users",tags=["users"],response_model=ResponseModel[UserDetailsSchema])
def createUser(user_schema: UserCreateSchema,userService: UserServiceDep):
    user = userService.createUser(user_schema)
    return resp_200(data=user)

@userRouter.get("/users/id/{user_id}",tags=["users"],response_model=ResponseModel[UserDetailsSchema])
def getUserById(user_id:int,userService: UserServiceDep):
    user = userService.getUserById(user_id)
    return resp_200(data=user)


@userRouter.get("/users/name/{name}",tags=["users"],response_model=ResponseModel[UserDetailsSchema])
def getUserByName(name:str,userService: UserServiceDep):
    user = userService.getUserByName(name)
    return resp_200(data=user)

@userRouter.get("/users/",tags=["users"], dependencies=[Depends(pagination_ctx(Page))],response_model=ResponseModel[Page[UserDetailsSchema]])
def getUserList(userService: UserServiceDep):
    results = userService.getUserList()
    return resp_pagination(data=results)