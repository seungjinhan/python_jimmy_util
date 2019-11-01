import os
import shutil
import glob

# 폴더내 파일 이름 조회
def get_file_names_in_dir( directory):
    
    file_list = os.listdir(directory)
    return [f for f in file_list if os.path.isfile(directory+"/"+f)]

# 폴더내 파일경로 조회(full path)
def get_file_names_in_dir_with_fullpath( directory):
    
    file_list = glob.glob(directory+"/*")
    return [f for f in file_list if os.path.isfile(f)]

# 폴더내 폴더 이름 조회
def get_folder_Names_in_dir(directory):
    
    file_list = os.listdir(directory)
    return [f for f in file_list if os.path.isdir(directory+"/"+f)]

# 폴더내 폴더이름 조회(full path)
def get_folder_names_in_dir_with_fullpath( directory):
    
    file_list = glob.glob(directory+"/*")
    return [f for f in file_list if os.path.isdir(f)]

# 폴더 내 이름 폴더 조회
def get_folder_files_Names_in_dir(directory):
    
    file_list = os.listdir(directory)
    return [f for f in file_list]

# 폴더 내 이름/폴더 구분해서 반환
def get_folder_files_Names_in_dir2(directory):
    
    result = [ get_folder_files_Names_in_dir(directory), get_file_names_in_dir(directory)]
    return result

# 폴더 내 이름/폴더 구분해서 반활(full path)
def get_folder_files_Names_in_dir2_with_fullpath(directory):
    
    result = [ get_file_names_in_dir_with_fullpath(directory), get_folder_names_in_dir_with_fullpath(directory)]
    return result

# 파일 생성하기
def create_dir( directory):
    try:
        if not(os.path.isdir( directory)):
            os.makedirs(os.path.join( directory))
    except OSError as e:
            print("Failed to create directory! [",str(e),"]")
            raise

# 파일 이동하기
def move_files( files, src_dir, desc_dir):
    
    create_dir( desc_dir)
    
    for f in files:
        shutil.move(src_dir+"/"+f, desc_dir+"/"+f)


if __name__ == '__main__':
    
#     print( get_file_names_in_dir("c:/"))
    print( get_file_names_in_dir_with_fullpath("c:/"))
    print( get_folder_names_in_dir_with_fullpath("c:/"))
    print( get_folder_files_Names_in_dir2_with_fullpath("c:/"))
#     print( get_folder_Names_in_dir("c:/"))
#     print( get_folder_files_Names_in_dir("c:/"))
#     print( get_folder_files_Names_in_dir2("c:/"))
    #move_files(["log.log"], "F:/log/home/chunlab/appserver", "F:/log/home/chunlab/appserver/a")
    