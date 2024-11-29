from fastapi import Depends
from typing import Annotated
from src.auth.service import UserService
from src.auth.dao import UserDao
def getUserService():
    userDao = UserDao()
    return UserService(userDao)
UserServiceDep = Annotated[UserService,Depends(getUserService)]

