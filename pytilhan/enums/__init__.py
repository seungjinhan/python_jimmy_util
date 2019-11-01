import enum
from pytilhan.enums.network_exception_enum import NetworkExceptionEnum
from pytilhan.enums.base.top_enum import TopEnum, BaseEnum

if __name__ == '__main__':

    a = TopEnum
    b = NetworkExceptionEnum.CALL_FAIL
    c = BaseEnum
    print(isinstance(b, TopEnum))
    print(type(b))
    print(type(c))


