import pandas as pd
import os, sys
sys.path.append('../common')
import excel as ex

# 엑셀 파일 읽기
excel_data = pd.read_excel('파일명.xlsx')

# 데이터 확인
print(excel_data.head())

# 데이터 처리 등 여러 작업 수행 가능
# 예: 특정 열 선택하기
selected_data = excel_data['열 이름']

# 처리한 데이터를 새로운 엑셀 파일로 저장
selected_data.to_excel('새로운_파일명.xlsx', index=False)
