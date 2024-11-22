from pydantic import BaseModel,ConfigDict
from datetime import datetime

class UserBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str
    email: str
    

class UserCreateSchema(UserBaseModel):
    password: str


class UserDetailsSchema(UserBaseModel):
    id:int
    create_time:datetime
    update_time:datetime
    #0 正常,1 已删除
    is_delete:int
    create_user:int