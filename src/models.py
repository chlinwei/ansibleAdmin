from sqlalchemy import Column,Integer,DATETIME
from datetime import datetime
from sqlalchemy.orm import Mapped,mapped_column
from src.database import Base
from sqlalchemy import String,DateTime,Integer


# class BaseModel(Base):
#     __abstract__ = True
#     id = Column(Integer,primary_key=True)
#     create_user = Column(Integer, default=0, comment="创建人")
#     create_time = Column(DATETIME, default=datetime.now, comment="创建时间")
#     update_user = Column(Integer, default=0, comment="更新人")
#     update_time = Column(DATETIME, default=datetime.now, comment="更新时间")
#     is_delete = Column(Integer, default=0, comment="删除标识:0-正常 1-已删除")



class BaseModel(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True,comment="id")
    create_user: Mapped[int] = mapped_column(Integer,comment="创建人",default=0)
    create_time: Mapped[datetime] = mapped_column(DateTime,comment="创建时间",default=datetime.now)
    update_user: Mapped[int] = mapped_column(Integer,comment="更新人",default=0)
    update_time: Mapped[datetime] = mapped_column(DateTime,comment="更新时间",default=datetime.now)
    is_delete: Mapped[int] = mapped_column(Integer,default=0,comment="0=正常,1=已删除")