from src.utils import *
from src.exceptions import BaseException
class UserException(BaseException,Exception):
    def __init__(self,code: int, message: str):
        self.code = code
        self.message = message
    
    UserNotExists = (1000,"用户不存在")
    UserExists = (1001,"用户已存在")

