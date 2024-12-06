from fastapi import Depends
from typing import Annotated
from src.auth.service.menuService import MenuService
from src.auth.service.userService import UserService
from src.auth.dao.menuDao import MenuDao
from src.auth.dao.userDao import UserDao
def getUserService():
    dao = UserDao()
    return UserService(dao)
def getMenuService():
    dao = MenuDao()
    return MenuService(dao)
UserServiceDep = Annotated[UserService,Depends(getUserService)]

MenuServiceDep = Annotated[MenuService,Depends(getMenuService)]