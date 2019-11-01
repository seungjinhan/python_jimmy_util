from pytilhan.enums.base.top_enum import TopEnum
from pytilhan.exceptions.type_exception import TypeException
from pytilhan.exceptions.base.base_exception import TopException
from pytilhan.utils.enums_util import check_enum_type


class CustomException(TopException):

    def __init__(self, exception_enum, msg=None):
        # enum 타입을 확인
        if check_enum_type(exception_enum):
            self.__msg = msg
            self.__exception_enum = exception_enum

    @property
    def type(self):
        return self.__exception_enum

    @property
    def msg(self):
        return self.__msg

    def __str__(self):
        return "Exception :[{}]:[{}] -> message[{}]".format(self.__exception_enum, self.__exception_enum.value,
                                                            self.__msg)
