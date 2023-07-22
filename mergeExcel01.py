"""
두개 엑셀 파일 합치기
"""
import pandas as pd

# 첫 번째 엑셀 파일 읽기
df1 = pd.read_excel('./temp/WantedInfo.000021~036181.xlsx')

# 두 번째 엑셀 파일 읽기
df2 = pd.read_excel('./temp/WantedInfo.036182~060407.xlsx')

# 두 데이터프레임을 합치기
merged_df = pd.concat([df1, df2], ignore_index=True)

# 합쳐진 데이터프레임을 새로운 엑셀 파일로 저장
merged_df.to_excel('./temp/WantedInfo.xlsx', index=False)
