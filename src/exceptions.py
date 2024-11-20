from enum import Enum
from src.utils import *
class BaseException(Enum):
    def __init__(self,code: int, message: str):
        self.code = code
        self.message = message

