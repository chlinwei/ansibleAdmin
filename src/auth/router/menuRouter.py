from fastapi import APIRouter
from src.auth.schemas import UserCreateSchema,UserDetailsSchema,MenuDetailsSchema,MenuCreateSchema
from src.auth.dependencies import UserServiceDep,MenuServiceDep
from src.utils import resp_200,ResponseModel,resp_pagination
from fastapi_pagination import Page,pagination_ctx
from fastapi import Depends
menuRouter = APIRouter()

@menuRouter.post("/menus",tags=["menus"],response_model=ResponseModel[MenuDetailsSchema])
def createMenu(menu_schema: MenuCreateSchema,menuService: MenuServiceDep):
    data = menuService.createMenu(menu_schema)
    return resp_200(data=data)

@menuRouter.get("/menus/id/{menu_id}",tags=["menus"],response_model=ResponseModel[MenuDetailsSchema])
def getMenuById(menu_id:int,menuService: MenuServiceDep):
    data = menuService.getMenuById(menu_id)
    return resp_200(data=data)


@menuRouter.get("/menus/name/{name}",tags=["menus"],response_model=ResponseModel[MenuDetailsSchema])
def getMenuByName(name:str,menuService: MenuServiceDep):
    data = menuService.getMenuByName(name)
    return resp_200(data=data)

@menuRouter.get("/menus/",tags=["menus"], dependencies=[Depends(pagination_ctx(Page))],response_model=ResponseModel[Page[MenuDetailsSchema]])
def getMenuList(menuService: MenuServiceDep):
    results = menuService.getUserList()
    return resp_pagination(data=results)
