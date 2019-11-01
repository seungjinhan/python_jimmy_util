from pytilhan.exceptions.custom_exception import CustomException
from pytilhan.enums.network_exception_enum import NetworkExceptionEnum
from pytilhan.exceptions.base.base_exception import TopException

if __name__ == '__main__':

    print('test')
    try:
        raise CustomException( NetworkExceptionEnum.CALL_FAIL)
    except TopException as e:
        print('>>',e)
    except Exception as e:
        print(e)