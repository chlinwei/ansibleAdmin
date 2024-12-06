from src.models import BaseModel
from sqlalchemy import Column,Integer,String,ForeignKey,Table
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped,mapped_column
from typing import List


class UserModel(BaseModel):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String(20),comment="用户名",nullable=False,unique=True)
    password: Mapped[str] = mapped_column(String(20),comment="密码",nullable=False)
    email: Mapped[str] = mapped_column(String(50),comment="邮箱",default=None,nullable=True)



class MenuModel(BaseModel):
    __tablename__ = "menus"
    parent_id: Mapped[int] = mapped_column(Integer,nullable=False,comment="parent id")
    menu_name: Mapped[str] = mapped_column(String(20),nullable=False,comment="菜单名")
    path: Mapped[str] = mapped_column(String(30),nullable=False,comment="访问路径")
    sort: Mapped[str] = mapped_column(String(30),default=None,comment="排序")
    menu_type: Mapped[int] = mapped_column(Integer,nullable=False,comment="0=目录,1=菜单,2=按钮")
    icon: Mapped[str] = mapped_column(String(30),default=None,comment="图标")

    roles: Mapped[List["RoleModel"]] = relationship(
        secondary="role_menu",back_populates="menus"
    )


class RoleModel(BaseModel):
    __tablename__ = "roles"
    sort: Mapped[str] = mapped_column(String(30),default=None,comment="排序")
    role_name: Mapped[str] = mapped_column(String(30),nullable=False,comment="角色名")
    status: Mapped[int] = mapped_column(Integer,default=0,comment="0=正常,1=禁止")

    menus: Mapped[List[MenuModel]] = relationship(
        secondary="role_menu",back_populates="roles"
    )



class  RoleMenuModel(BaseModel):
    #1对多
    __tablename__ = "role_menu"
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id'),primary_key=True)
    menu_id: Mapped[int] = mapped_column(ForeignKey('menus.id'),primary_key=True)


# class UserRoleModel(BaseModel):
#     #多对多
#     __tablename__ = "user_role"
#     user_id = Column(Integer,nullable=False,comment="用户id")
#     role_id = Column(Integer,nullable=False,comment="角色 id")