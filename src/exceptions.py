from src.errorMapping import ErrorMapping
class AnsibleException(Exception):
    def __init__(self,errorMapping: ErrorMapping):
        msg = f"error code:{errorMapping.code},message:{errorMapping.message}"
        self.errorMapping = errorMapping
        super().__init__(msg)