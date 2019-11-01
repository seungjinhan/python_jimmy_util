from pytilhan.exceptions.base.base_exception import TopException


class TypeException(TopException):

    def __init__(self, instance, class_name, msg=None):
        self._msg = msg
        self._instance = instance
        self._class_name = class_name

    def __str__(self):
        return "[{}]'s type is {}. you need to use this type {}'s sub Enum . message[{}] ".format(self._instance,
                                                                                                  type(self._instance),
                                                                                                  self._class_name,
                                                                                                  self._msg)
