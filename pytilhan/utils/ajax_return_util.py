from pytilhan.utils.enums_util import check_enum_type


# Enum객체로 반환객체 생성
def make_error_return_enum(enum_obj, msg):
    if check_enum_type(enum_obj):
        data = {
            "success": False,
            "code": enum_obj.name,
            "desc": enum_obj.value,
            "data": msg
        }
        return str(data)
    else:
        return 'error'
    
def make_error_return( msg):
    data = {
        "success": False,
        "code": "",
        "desc": "",
        "data": msg
    }
    return str(data)


# Exception객체로 반환객체 생성
def make_error_return_exception(e):
    data = {
        "success": False,
        "code": None,
        "desc": None,
        "data": e
    }
    return str(data)


# CustomException 객체로 반환객체 생성
def make_error_return_custom_exception(e):
    data = {
        "success": False,
        "code": e.type.name,
        "desc": e.type.value,
        "data": e
    }
    return str(data)


# 성공일때 반환객체 생성
def make_success_return_json_data(json_data):
    data = {
        "success": True,
        "code": None,
        "desc": None,
        "data": json_data
    }
    return data
