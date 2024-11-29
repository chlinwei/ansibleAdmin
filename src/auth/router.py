from fastapi import APIRouter
from src.auth.schemas import UserCreateSchema,UserDetailsSchema
from src.auth.dependencies import UserServiceDep
from src.utils import resp_200,ResponseModel
from fastapi_pagination import Page,pagination_ctx,paginate
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


@userRouter.get("/users/username/{name}",tags=["users"],response_model=ResponseModel[UserDetailsSchema])
def getUserByName(name:str,userService: UserServiceDep):
    user = userService.getUserByName(name)
    return resp_200(data=user)

# @userRouter.get("/users/",tags=["users"])
# def getUserList(userService: UserServiceDep) ->  Page[UserDetailsSchema]:
#     result = userService.getUserList()
# <class 'fastapi_pagination.default.Page[UserDetailsSchema]'>
#     print(type(result))
#     return result

# @userRouter.get("/users/",tags=["users"], dependencies=[Depends(pagination_ctx(Page))],response_model=ResponseModel[Page[UserDetailsSchema]])
# def getUserList(userService: UserServiceDep):
#     result = userService.getUserList()
#     model = ResponseModel(code=200,message="success",data=result)
#     return model

@userRouter.get("/users/",tags=["users"], dependencies=[Depends(pagination_ctx(Page))],response_model=ResponseModel[Page[UserDetailsSchema]])
def getUserList(userService: UserServiceDep):
    result = userService.getUserList()
    return resp_200(data=result)