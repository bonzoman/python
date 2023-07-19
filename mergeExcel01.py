import pandas as pd

# 첫 번째 엑셀 파일 읽기
df1 = pd.read_excel('./DataFiles/sample1.xlsx')

# 두 번째 엑셀 파일 읽기
df2 = pd.read_excel('./DataFiles/sample2.xlsx')

# 두 데이터프레임을 합치기
merged_df = pd.concat([df1, df2], ignore_index=True)

# 합쳐진 데이터프레임을 새로운 엑셀 파일로 저장
merged_df.to_excel('./DataFiles/sample_All.xlsx', index=False)
