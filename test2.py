import requests
from bs4 import BeautifulSoup
# from openpyxl import Workbook
import pandas as pd
from datetime import datetime
from time import time

API_URL = 'https://www.wanted.co.kr/api/v4/jobs/'
SITE_URL = 'https://www.wanted.co.kr/wd/'
IDX_LIST = []
URL_LIST = []


'''
def makeurl():
    for idx in range(170500, 170900): # 170787
        # url = "https://www.wanted.co.kr/wd/" + str(idx)
        url = API_URL + str(idx)
        IDX_LIST.append(str(idx));
        URL_LIST.append(url)


# M A I N
makeurl()
'''

# print("현재 : ", datetime.now())


# write_wb = Workbook()
# write_ws = write_wb.active

page = []
company = []
due_time = []
position = []
skill_tags = []
skill_tags_all_list = []
for idx in range(170000, 175000):

    # time.sleep(1)

    response = requests.get(API_URL+str(idx))
    responseJson = response.json()
    print(SITE_URL+str(idx), responseJson)

    if not responseJson.__contains__('job'):
        continue

    # soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    # soup = str(soup)

    jobObj = responseJson['job']
    jobKeys = responseJson['job'].keys()
    # print(jobObj)

    page.append('https://www.wanted.co.kr/wd/'+str(idx))

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

'''
df = pd.DataFrame()
df['page'] = page
df['company'] = company
df['due_time'] = due_time
df['position'] = position
df['skill_tags'] = skill_tags

df.to_excel('./WantedInfo.xlsx', sheet_name='Sheet1')
'''

print("현재 : ", datetime.now())

print("end")

'''
    jikmoo = soup[soup.find('"position":""') + 12: soup.find('"reward":') - 2]
    # print("직무:",jikmoo)
    yusa_jikmoo = soup[soup.find('"sub_categories":') + 18: soup.find('"position":""') - 2]
    # print("유사직무:", yusa_jikmoo)
    job_naeyong = soup[soup.find('"jd":') + 5: soup.find('"company_name":') - 2]
    # print("채용내용:", job_naeyong)
    company_name = soup[soup.find('"company_name":""') + 16: soup.find('"lang":""') - 2]
    # print("회사이름 7:  ", company_name)

    write_ws.append([
        company_name,
        jikmoo,
        yusa_jikmoo,
        job_naeyong
    ])

write_wb.save("Wanted.csv")  # save csv
'''