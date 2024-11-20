from pydantic import BaseModel

class UserBaseModel(BaseModel):
    username: str
    password: str
    email: str

class UserCreateSchema(UserBaseModel):
    pass


class UserDetailsSchema(UserBaseModel):
    pass    