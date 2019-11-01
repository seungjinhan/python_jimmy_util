from pytilhan.utils.json_util import file_to_json

def read_global_data( ):
    data = file_to_json('../../global.json')
    return data


if __name__ == '__main__':
    print( read_global_data())