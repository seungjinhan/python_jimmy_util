import requests
from pytilhan.exceptions.custom_exception import CustomException
from pytilhan.enums.network_exception_enum import NetworkExceptionEnum


# API 호출 : GET
def call_get(url, param):
    try:
        res = requests.get(url, params=param)
    except Exception as e: 
        raise CustomException(NetworkExceptionEnum.CONNECT_FAIL , "[" + str(e) + "] [GET] ["+ url + " - "+ str(param)+"]" )
    
    return check_res(res)


# API 호출 : POST
def call_post(url, param):
    try:
        res = requests.post(url, data=param)
    except Exception as e: 
        raise CustomException(NetworkExceptionEnum.CONNECT_FAIL, "[" + str(e) + "] [POST] ["+ url + " - "+ str(param)+"]" )
            
    return check_res(res)


# API 호출후  Response 값 체크 및 반환
def check_res(res):

    if res.ok:
        return res.content
    else:
        raise CustomException(NetworkExceptionEnum.CALL_FAIL, str(res))


if __name__ ==  '__main__':
    
    call_get("http://54.180.21.228:9003/push", {})
    