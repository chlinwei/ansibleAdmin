from src.auth.models import MenuModel
from sqlalchemy import select,Select
from src.database import Session
from fastapi_pagination.ext.sqlalchemy import paginate
        

        
class MenuDao:
    def getMenuById(self,menuId: int):
        stmt = (Select(MenuModel).where(MenuModel.id == menuId))
        with Session() as session:
            result = session.execute(stmt).scalar()
            return result
    def getMenuByName(self,name: str):
        stmt = (Select(MenuModel).where(MenuModel.menu_name == name))
        with Session() as session:
            result = session.execute(stmt).scalar()
            return result

    def createMenu(self,menu_db: MenuModel):
        with Session() as session:
            session.add(menu_db)
            session.commit()
            session.refresh(menu_db)
            return menu_db
    def getMenuList(self):
        stmt = (select(MenuModel))
        with Session() as session:
            return paginate(session,stmt,sorted="")
    
        
    
            