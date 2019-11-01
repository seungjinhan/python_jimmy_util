from pytilhan.exceptions.type_exception import TypeException
from pytilhan.enums.base.top_enum import TopEnum


def check_enum_type(enum_obj):

    # enum 타입을 확인
    if isinstance(enum_obj, TopEnum):
        return True
    else:
        raise TypeException(enum_obj, TopEnum, 'wrong type')
