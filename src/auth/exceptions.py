from src.errorMapping import ErrorMapping
class UserErrorMapping(ErrorMapping):
    UserNotExists = (2000,'用户不存在')
    UserExists = (2001,'用户已存在')

