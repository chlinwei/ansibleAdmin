from src.exceptions import AnsibleException
from src.auth.exceptions import UserErrorMapping

def test_raise_exception():
    raise AnsibleException(UserErrorMapping.UserExists)