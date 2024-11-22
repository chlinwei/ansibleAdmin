from src.auth.schemas import UserCreateSchema,UserDetailsSchema
from src.auth.models import UserModel
from sqlalchemy import Select
from src.auth.exceptions import UserErrorMapping
from src.exceptions import AnsibleException
from src.database import Session

class UserService:
    def getUserById(self,userId: int) -> UserDetailsSchema | None:
        stmt = (Select(UserModel).where(UserModel.id == userId))
        with Session() as session:
            results = session.execute(stmt).first()
            if results is None:
                return None
            return UserDetailsSchema.model_validate(results[0])

    

        
    
    def getUserByName(self,name: str) -> UserDetailsSchema | None:
        stmt = (Select(UserModel).where(UserModel.username == name))
        with Session() as session:
            results = session.execute(stmt).first()
            if results is None:
                return None
            return UserDetailsSchema.model_validate(results[0])
   
        
    def createUser(self,userdata: UserCreateSchema) -> UserDetailsSchema:
        result = self.getUserByName(userdata.username)
        with Session() as session:
            if result is not None:
                #用户存在
                raise AnsibleException(UserErrorMapping.UserExists)
            user_db = UserModel(**userdata.model_dump())
            session.add(user_db)
            session.commit()
            session.refresh(user_db)
            return UserDetailsSchema.model_validate(user_db)

        
        
        

        
        
            
    
        
    
            