from fastapi import Depends
from typing import Annotated
from src.auth.service import UserService
UserServiceDep = Annotated[UserService,Depends(UserService)]