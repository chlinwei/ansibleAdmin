from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from datetime import datetime
class A(BaseModel):
    id: int
    name: str
    create_time: datetime

class B(BaseModel):
    age: int
    a: A


a = A(id=1,name='A',create_time=datetime.now())
b = B(age=10,a=a)
print(jsonable_encoder(a))
print(jsonable_encoder(b))