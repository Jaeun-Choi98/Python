import os

def find_file(file_name, search_path='.'):
    file_name = file_name + ".xlsx"
    for root, dirs, files in os.walk(search_path):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

# 파일명 입력 받기
file_name = input("검색할 파일명을 입력하세요: ")

# 파일 찾기
file_path = find_file(file_name)

if file_path:
    print(f"{file_name}의 위치는 {file_path}입니다.")
else:
    print(f"{file_name}을(를) 찾을 수 없습니다.")
