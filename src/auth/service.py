from src.auth.schemas import UserCreateSchema,UserDetailsSchema
from src.auth.models import UserModel
from sqlalchemy import Select
from src.auth.exceptions import UserErrorMapping
from src.exceptions import AnsibleException
from src.database import Session
from loguru import logger

class UserService:
    @logger.catch
    def getUserById(self,userId: int) -> UserDetailsSchema:
        stmt = (Select(UserModel).where(UserModel.id == userId))
        with Session() as session:
            result = session.execute(stmt).scalar()
            if result is None:
                errorData = f"userId:{userId} not found"
                raise AnsibleException(UserErrorMapping.UserNotExists,errordata=errorData)
            return UserDetailsSchema.model_validate(result)

    

        
    @logger.catch
    def getUserByName(self,name: str) -> UserDetailsSchema:
        stmt = (Select(UserModel).where(UserModel.username == name))
        with Session() as session:
            result = session.execute(stmt).scalar()
            if result is None:
                raise AnsibleException(UserErrorMapping.UserNotExists,errordata=f"userName:{name} not found")
            return UserDetailsSchema.model_validate(result)
   
    @logger.catch
    def createUser(self,userdata: UserCreateSchema) -> UserDetailsSchema:
        result = self.getUserByName(userdata.username)
        with Session() as session:
            if result is not None:
                #用户存在
                raise AnsibleException(UserErrorMapping.UserExists,errordata=f"userName:{userdata.username} already exists")
            user_db = UserModel(**userdata.model_dump())
            session.add(user_db)
            session.commit()
            session.refresh(user_db)
            return UserDetailsSchema.model_validate(user_db)

        
        
        

        
        
            
    
        
    
            