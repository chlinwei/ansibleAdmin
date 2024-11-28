from enum import Enum
#所有错误都在这里进行定义
class ErrorMapping(Enum):
    def __init__(self,code: int, message: str):
        self.code = code
        self.message = message
    def __str__(self):
        return f"error code:{self.code},message:{self.message}"
    def __repr__(self):
        return f"error code:{self.code},message:{self.message}"





    