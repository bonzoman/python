import requests
from bs4 import BeautifulSoup
# from openpyxl import Workbook
import pandas as pd
from datetime import datetime


def initialize_variables():
    return [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []


def save_data_to_excel(index):
    # 첫 번째 시트 데이터
    data_sheet1 = {'page': page,
                   '회사명': company,
                   '분류': industry_name,
                   '마감기간': due_time,
                   'position': position,
                   'skill_tags': skill_tags,
                   '지역': location,
                   'hidden': hidden,
                   'status': status,
                   'address': address,
                   'category_tags': category_tags,
                   'detail_requirements': detail_requirements,
                   'detail_main_tasks': detail_main_tasks,
                   'detail_intro': detail_intro,
                   'detail_benefits': detail_benefits,
                   'detail_preferred_points': detail_preferred_points
                   }

    # 두 번째 시트 데이터
    data_sheet2 = {'skill_tags': list(set(skill_tags_all_list))}  # 중복제거

    # DataFrame 객체 생성
    df1 = pd.DataFrame(data_sheet1)
    df2 = pd.DataFrame(data_sheet2)

    # Excel 파일로 저장
    with pd.ExcelWriter('WantedInfo' + str(idx) + '.xlsx') as writer:
        df1.to_excel(writer, sheet_name='시트1', index=False)
        df2.to_excel(writer, sheet_name='시트2', index=False)


# START #########################################################################################################
# START #########################################################################################################
# START #########################################################################################################
# START #########################################################################################################
API_URL = 'https://www.wanted.co.kr/api/v4/jobs/'
SITE_URL = 'https://www.wanted.co.kr/wd/'

# startNo, endNo, interval = 170001, 170012, 1000
startNo, endNo, interval = 102, 100001, 1000

page, company, industry_name, due_time, position, skill_tags, location, hidden, status, address, \
    detail_requirements, detail_main_tasks, detail_intro, detail_benefits, detail_preferred_points, \
    category_tags, skill_tags_all_list = initialize_variables()

for idx in range(startNo, endNo):

    response = requests.get(API_URL+str(idx))
    responseJson = response.json()
    print(SITE_URL+str(idx), responseJson)

    if responseJson.__contains__('job'):

        jobObj = responseJson['job']
        jobKeys = jobObj.keys()
        # print(jobObj)

        page.append(SITE_URL+str(idx))

        for n in jobKeys:
            if n == 'company':
                company.append(jobObj[n]['name'])
                industry_name.append(jobObj[n]['industry_name'])
            elif n == 'due_time':
                due_time.append(jobObj.get(n))
            elif n == 'position':
                position.append(jobObj.get(n))
            elif n == 'skill_tags':
                aaa = []
                for n2 in jobObj[n]:
                    aaa.append(n2['title'])
                    skill_tags_all_list.append(n2['title'])  # 전체 담기
                skill_tags.append(','.join(aaa))
            elif n == 'category_tags':
                bbb = []
                for n3 in jobObj[n]:
                    bbb.append(str(n3['parent_id']) + '.' + str(n3['id']))
                category_tags.append(','.join(bbb))
            elif n == 'address':
                location.append(jobObj[n]['location'])
                address.append(jobObj[n]['full_location'])
            elif n == 'hidden':
                hidden.append(jobObj.get(n))
            elif n == 'status':
                status.append(jobObj.get(n))
            elif n == 'detail':
                detail_requirements.append(jobObj[n]['requirements'])
                detail_main_tasks.append(jobObj[n]['main_tasks'])
                detail_intro.append(jobObj[n]['intro'])
                detail_benefits.append(jobObj[n]['benefits'])
                detail_preferred_points.append(jobObj[n]['preferred_points'])

    if idx % interval == 0 and len(page) > 0:  # interval 배수인지 확인
        save_data_to_excel(idx)
        page, company, industry_name, due_time, position, skill_tags, location, hidden, status, address, \
            detail_requirements, detail_main_tasks, detail_intro, detail_benefits, detail_preferred_points, \
            category_tags, skill_tags_all_list = initialize_variables()

# 마지막에 남은거 한 번 더 실행하는 코드
if not idx % interval == 0 and len(page) > 0:   # interval 배수인지 확인
    save_data_to_excel(idx)

print("end : ", datetime.now())
