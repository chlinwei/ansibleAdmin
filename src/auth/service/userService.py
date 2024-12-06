from src.auth.schemas import UserCreateSchema,UserDetailsSchema
from src.auth.schemas import MenuCreateSchema,MenuDetailsSchema
from src.auth.models import UserModel,MenuModel
from sqlalchemy import Select
from src.auth.exceptions import UserErrorMapping,MenuErrorMapping
from src.exceptions import AnsibleException
from src.database import Session
from loguru import logger
from src.auth.utils import Hasher
from src.auth.dao.userDao import UserDao

class UserService:
    def __init__(self,userDao: UserDao):
        self.userDao = userDao
    def getUserById(self,userId: int) -> UserDetailsSchema:
        result = self.userDao.getUserById(userId)
        if result is None:
                errorData = f"userId:{userId} not found"
                raise AnsibleException(UserErrorMapping.UserNotExists,errordata=errorData)
        return UserDetailsSchema.model_validate(result)


    def getUserByName(self,name: str) -> UserDetailsSchema:
        result = self.userDao.getUserByName(name)
        if result is None:
            raise AnsibleException(UserErrorMapping.UserNotExists,errordata=f"userName:{name} not found")
        return UserDetailsSchema.model_validate(result)
    
   

    def createUser(self,userdata: UserCreateSchema) -> UserDetailsSchema:
        result = self.userDao.getUserByName(userdata.username)
        if result is not None:
            #用户存在
            raise AnsibleException(UserErrorMapping.UserExists,errordata=f"userName:{userdata.username} already exists")
        user_db = UserModel(**userdata.model_dump())
        user_db.password = Hasher.get_password_hash(user_db.password)
        result = self.userDao.createUser(user_db)
        return UserDetailsSchema.model_validate(result)
    
    def getUserList(self):
         return self.userDao.getUserList()