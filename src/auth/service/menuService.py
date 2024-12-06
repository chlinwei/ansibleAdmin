from src.auth.schemas import UserCreateSchema,UserDetailsSchema
from src.auth.schemas import MenuCreateSchema,MenuDetailsSchema
from src.auth.models import UserModel,MenuModel
from sqlalchemy import Select
from src.auth.exceptions import UserErrorMapping,MenuErrorMapping
from src.exceptions import AnsibleException
from src.database import Session
from loguru import logger
from src.auth.utils import Hasher
from src.auth.dao.menuDao  import   MenuDao

class MenuService:
    def __init__(self,menuDao: MenuDao):
        self.menuDao = menuDao
    def getMenuById(self,menuId: int) -> MenuDetailsSchema:
        result = self.menuDao.getMenuById(menuId)
        if result is None:
                errorData = f"menuId:{menuId} not found"
                raise AnsibleException(MenuErrorMapping.MenuExists,errordata=errorData)
        return MenuDetailsSchema.model_validate(result)

    def getMenuByName(self,name: str) -> MenuDetailsSchema:
        result = self.menuDao.getMenuByName(name)
        if result is None:
            raise AnsibleException(MenuErrorMapping.MenuNotExists,errordata=f"Menu:{name} not found")
        return MenuDetailsSchema.model_validate(result)

    def createMenu(self,menu_data: MenuCreateSchema) -> MenuDetailsSchema:
        result = self.menuDao.getMenuByName(menu_data.menu_name)
        if result is not None:
            #存在
            raise AnsibleException(MenuErrorMapping.MenuExists,errordata=f"Menu:{menu_data.menu_name} already exists")
        menu_db = MenuModel(**menu_data.model_dump())
        result = self.menuDao.createMenu(menu_db)
        return MenuDetailsSchema.model_validate(result)
    
    def getUserList(self):
         return self.menuDao.getMenuList()