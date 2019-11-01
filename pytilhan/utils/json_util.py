import json


# 스트링을 json으로 바꾸기
def string_to_json(data):
    result = json.loads(data)
    return result


# 파일을 읽어서 json으로 바꾸기
def file_to_json(path):

    result = '';
    with open(path, 'r', encoding='UTF-8-sig') as file:
        result = file.read()

    return string_to_json(result)


# json을 string으로 변환
def json_to_string(json_data):
    return json.dumps(json_data, ensure_ascii=False)


# json데이터를 file에 저장
def json_to_file(json_data, path):
    data = json_data

    if type(json_data) == dict:
        data = json_to_string(json_data)

    with open(path, 'w', encoding='UTF-8-sig') as file:
        file.write(data)


if __name__ == '__main__':
    d = '{"mail": { "id": "아이디", "password": "22" }}'
    da = string_to_json(d)

    json_to_file(da, '../../global.json')

    data = file_to_json('../../global.json')
    print(data)
