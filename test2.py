import requests
from bs4 import BeautifulSoup
# from openpyxl import Workbook
import pandas as pd
from datetime import datetime

API_URL = 'https://www.wanted.co.kr/api/v4/jobs/'
SITE_URL = 'https://www.wanted.co.kr/wd/'

page = []
company = []
due_time = []
position = []
skill_tags = []
skill_tags_all_list = []
for idx in range(170000, 175000):

    response = requests.get(API_URL+str(idx))
    responseJson = response.json()
    print(SITE_URL+str(idx), responseJson)

    if not responseJson.__contains__('job'):
        continue

    jobObj = responseJson['job']
    jobKeys = responseJson['job'].keys()
    # print(jobObj)

    page.append(SITE_URL+str(idx))

    for n in jobKeys:
        if n == 'company':
            company.append(jobObj[n]['name'])
        elif n == 'due_time':
            due_time.append(jobObj.get(n))
        elif n == 'position':
            position.append(jobObj.get(n))
        elif n == 'skill_tags':
            skillTitles = []
            for n2 in jobObj[n]:
                skillTitles.append(n2['title'])
                skill_tags_all_list.append(n2['title'])  # 전체 담기
            skill_tags.append(','.join(skillTitles))


# 첫 번째 시트 데이터
data_sheet1 = {'page': page,
               'company': company,
               'due_time': due_time,
               'position': position,
               'skill_tags': skill_tags}

# 두 번째 시트 데이터
data_sheet2 = {'skill_tags': list(set(skill_tags_all_list))}  # 중복제거

# DataFrame 객체 생성
df1 = pd.DataFrame(data_sheet1)
df2 = pd.DataFrame(data_sheet2)

# Excel 파일로 저장
with pd.ExcelWriter('WantedInfo.xlsx') as writer:
    df1.to_excel(writer, sheet_name='시트1', index=False)
    df2.to_excel(writer, sheet_name='시트2', index=False)

print("end : ", datetime.now())
