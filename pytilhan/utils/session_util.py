from pytilhan.enums.base import BaseEnum
from pytilhan.exceptions.custom_exception import CustomException
from pytilhan.enums.session_exception_enum import SessionExceptionEnum


# 세션 KEY LIST
class SessionKeyEnum(BaseEnum):
    USER_SESSION = "USER_SESSION"


# 사용자 세션 생성
def set_user_session(req, user):
    req.session[SessionKeyEnum.USER_SESSION.value] = user


# 사용자 세션 조회
def get_user_session(req):
    return req.session[SessionKeyEnum.USER_SESSION.value]


# 사용자 세션 존재 유무 확인
def exist_user_session(req):
    return SessionKeyEnum.USER_SESSION.value in req.session


# 사용자 세션 삭제
def remove_user_session(req):
    if exist_user_session(req):
        del req.session[SessionKeyEnum.USER_SESSION.value]


# 세션에 값 저장
def set_session(req, key, value):
    req.session[key] = value


# 세션에 값 조회
def get_session(req, key):
    return req.session[key]


# 세션에 값 삭제
def remove_session(req, key):
    try:
        del req.session[key]
    except KeyError:
        pass


# 세션에 키값 존재 유무 확인
def contain_key(req, key):
    return key in req.session


# 사용자 세션 체크 데코레이션    
def deco_exist_user_session(func):
    def inner(*args, **kwargs):
        req = args[0]

        if exist_user_session(req):
            return func(*args, **kwargs)
        else:
            raise CustomException(SessionExceptionEnum.NOT_EXIST)

    return inner
