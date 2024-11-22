from sqlalchemy import Column,Integer,DATETIME
from datetime import datetime
from src.database import Base


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer,primary_key=True)
    create_user = Column(Integer, default=0, comment="创建人")
    create_time = Column(DATETIME, default=datetime.now, comment="创建时间")
    update_user = Column(Integer, default=0, comment="更新人")
    update_time = Column(DATETIME, default=datetime.now, comment="更新时间")
    is_delete = Column(Integer, default=0, comment="删除标识:0-正常 1-已删除")