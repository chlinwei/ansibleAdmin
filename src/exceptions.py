from src.errorMapping import ErrorMapping
from fastapi import Request
from src.utils import resp_400_exception
class AnsibleException(Exception):
    def __init__(self,errorMapping: ErrorMapping,errordata:str = None):
        msg = f"error code:{errorMapping.code},message:{errorMapping.message}"
        self.errorMapping = errorMapping
        self.errordata = errordata
        super().__init__(msg)


def AnsibleAdminExceptionHandler(request: Request, exception: AnsibleException):
    return resp_400_exception(errMapping=exception.errorMapping,data=exception.errordata)
    