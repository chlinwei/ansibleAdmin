from src.auth.schemas import UserCreateSchema,UserDetailsSchema
from src.auth.models import UserModel
from sqlalchemy import Select
from src.dependencies import SessionDep
from src.auth.exceptions import UserException
class UserService:
    def getUserById(userId: int, session: SessionDep) -> UserDetailsSchema:
        stmt = (Select(UserModel).where(UserModel.id == userId))
        result = session.execute(stmt).one()
        user_data = UserDetailsSchema(**result.__dict__)
        return user_data
    
    def getUserByName(name: str, session: SessionDep) -> UserDetailsSchema:
        stmt = (Select(UserModel).where(UserModel.username == name))
        result = session.execute(stmt).one()
        user_data = UserDetailsSchema(**result.__dict__)
        return user_data
   
        
    def createUser(userdata: UserCreateSchema, session: SessionDep) -> UserDetailsSchema:
        if UserService.getUserByName(userdata.username) is not None:
            #用户存在
            raise UserException.UserExists()
        
        
            
    
        
    
            