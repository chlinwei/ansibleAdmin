from src.models import BaseModel
from sqlalchemy import Column,Integer,String

class UserModel(BaseModel):
    __tablename__ = "users"
    username = Column(String(20), nullable=False, unique=True, comment="用户姓名")
    password = Column(String(20), nullable=False, comment="密码")
    email = Column(String(50), nullable=True,  comment="电子邮箱")



    