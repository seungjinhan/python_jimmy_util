from pytilhan.enums.base.top_enum import BaseEnum


# 네트워크 예외 Enum값
class NetworkExceptionEnum(BaseEnum):
    CALL_FAIL = "네트워크 호출 응답 실패"
    CONNECT_FAIL = '접속실패'
