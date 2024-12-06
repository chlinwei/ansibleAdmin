from pydantic import BaseModel,ConfigDict
from datetime import datetime

class UserBaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str
    email: str
    

class UserCreateSchema(UserBaseSchema):
    password: str


class UserDetailsSchema(UserBaseSchema):
    id:int
    create_time:datetime
    update_time:datetime
    #0 正常,1 已删除
    is_delete:int
    create_user:int




class MenuBaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    parent_id: int = 0
    menu_name: str
    path: str
    sort: str 
    menu_type: int
    icon: str


class MenuCreateSchema(MenuBaseSchema):
    pass



class MenuDetailsSchema(MenuBaseSchema):
    pass

