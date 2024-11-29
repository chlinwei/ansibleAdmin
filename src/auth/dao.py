from src.auth.models import UserModel
from sqlalchemy import select,Select
from src.database import Session
from fastapi_pagination.ext.sqlalchemy import paginate

class UserDao:
    def getUserById(self,userId: int):
        stmt = (Select(UserModel).where(UserModel.id == userId))
        with Session() as session:
            result = session.execute(stmt).scalar()
            return result
    

        

    def getUserByName(self,name: str):
        stmt = (Select(UserModel).where(UserModel.username == name))
        with Session() as session:
            result = session.execute(stmt).scalar()
            return result
   

    def createUser(self,user_db: UserModel) -> UserModel:
        with Session() as session:
            session.add(user_db)
            session.commit()
            session.refresh(user_db)
            return user_db
        
    def getUserList(self):
        stmt = (select(UserModel))
        with Session() as session:
            return paginate(session,stmt)
            
        
        
        

        
        
            
    
        
    
            