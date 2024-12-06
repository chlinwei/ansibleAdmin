from src.errorMapping import ErrorMapping
class UserErrorMapping(ErrorMapping):
    UserNotExists = (2100,'用户不存在')
    UserExists = (2101,'用户已存在')



class MenuErrorMapping(ErrorMapping):
    MenuNotExists = (2200,'menu不存在')
    MenuExists = (2201,'menu已存在')