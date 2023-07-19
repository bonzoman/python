import sys

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import pandas as pd
from datetime import datetime
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE


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
                   '국가': country,
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
    # data_sheet2 = {'skill_tags': list(set(skill_tags_all_list))}  # 중복제거

    # DataFrame 객체 생성
    df1 = pd.DataFrame(data_sheet1)
    # df2 = pd.DataFrame(data_sheet2)

    # Excel 파일로 저장
    with pd.ExcelWriter('WantedInfo' + str(idx) + '.xlsx') as writer:
        df1.to_excel(writer, sheet_name='시트1', index=False)
        # df2.to_excel(writer, sheet_name='시트2', index=False)


# START #########################################################################################################
# START #########################################################################################################
# START #########################################################################################################
# START #########################################################################################################
API_URL = 'https://www.wanted.co.kr/api/v4/jobs/'
SITE_URL = 'https://www.wanted.co.kr/wd/'

# startNo, endNo, interval = 170001, 170012, 1000
startNo, endNo, interval = 59271, 1000000, 1000

page, company, industry_name, due_time, position, skill_tags, country, location, hidden, status, address, \
    detail_requirements, detail_main_tasks, detail_intro, detail_benefits, detail_preferred_points, \
    category_tags = initialize_variables()
i, idx = 0, 0
for idx in range(startNo, endNo):

    response = requests.get(API_URL + str(idx))
    if not response.ok:
        continue

    responseJson = response.json()

    # if responseJson.__contains__('job') and responseJson['job'].get('status') == 'active':
    if responseJson.__contains__('job'):
        i += 1
        print(i, SITE_URL + str(idx), responseJson)

        jobObj = responseJson['job']
        jobKeys = jobObj.keys()

        page.append(SITE_URL + str(idx))

        # key 없는 경우 미리 초기화 처리... array length 맞춰야 함
        company.append('') if 'company' not in jobObj else None
        industry_name.append('') if 'company' not in jobObj else None
        due_time.append('') if 'due_time' not in jobObj else None
        position.append('') if 'position' not in jobObj else None
        skill_tags.append('') if 'skill_tags' not in jobObj else None
        category_tags.append('') if 'category_tags' not in jobObj else None
        country.append('') if 'address' not in jobObj else None
        location.append('') if 'address' not in jobObj else None
        address.append('') if 'address' not in jobObj else None
        hidden.append('') if 'hidden' not in jobObj else None
        status.append('') if 'status' not in jobObj else None
        detail_requirements.append('') if 'detail' not in jobObj else None
        detail_main_tasks.append('') if 'detail' not in jobObj else None
        detail_intro.append('') if 'detail' not in jobObj else None
        detail_benefits.append('') if 'detail' not in jobObj else None
        detail_preferred_points.append('') if 'detail' not in jobObj else None

        for key in jobKeys:
            if key == 'company':
                company.append(jobObj[key]['name'] if 'name' in jobObj[key] else '')
                industry_name.append(jobObj[key]['industry_name'] if 'industry_name' in jobObj[key] else '')

            if key == 'due_time':
                due_time.append(jobObj.get(key) if not jobObj[key] is None else '상시')

            if key == 'position':
                position.append(jobObj.get(key))

            if key == 'skill_tags':
                aaa = []
                for n2 in jobObj[key]:
                    aaa.append(n2['title'] if 'title' in n2 else None)
                    # skill_tags_all_list.append(n2['title'])  # 전체 담기
                skill_tags.append(','.join(aaa))

            if key == 'category_tags':
                bbb = []
                for n3 in jobObj[key]:
                    bbb.append(str(n3['parent_id']) + '.' + str(n3['id']))
                category_tags.append(','.join(bbb))
            if key == 'address':
                country.append(jobObj[key]['country'] if 'country' in jobObj[key] else '')
                location.append(jobObj[key]['location'] if 'location' in jobObj[key] else '')
                address.append(jobObj[key]['full_location'] if 'full_location' in jobObj[key] else '')
            if key == 'hidden':
                hidden.append(jobObj.get(key))
            if key == 'status':
                status.append(jobObj.get(key))
            if key == 'detail':
                if jobObj[key] is None:
                    detail_requirements.append('')
                    detail_main_tasks.append('')
                    detail_intro.append('')
                    detail_benefits.append('')
                    detail_preferred_points.append('')
                else:
                    # IllegalCharacterError 나서 ILLEGAL_CHARACTERS_RE 특수문자 제거
                    detail_requirements.append(
                        ILLEGAL_CHARACTERS_RE.sub(r'', jobObj[key]['requirements'])
                        if 'requirements' in jobObj[key] else '')
                    detail_main_tasks.append(
                        ILLEGAL_CHARACTERS_RE.sub(r'', jobObj[key]['main_tasks'])
                        if 'main_tasks' in jobObj[key] else '')
                    detail_intro.append(
                        ILLEGAL_CHARACTERS_RE.sub(r'', jobObj[key]['intro'])
                        if 'intro' in jobObj[key] else '')
                    detail_benefits.append(
                        ILLEGAL_CHARACTERS_RE.sub(r'', jobObj[key]['benefits'])
                        if 'benefits' in jobObj[key] else '')
                    detail_preferred_points.append(
                        ILLEGAL_CHARACTERS_RE.sub(r'', jobObj[key]['preferred_points'])
                        if 'preferred_points' in jobObj[key] else '')
        # for end

        listLens = [len(page), len(company), len(industry_name), len(due_time), len(position),
                    len(skill_tags), len(country), len(location), len(hidden), len(status), len(address),
                    len(detail_requirements), len(detail_main_tasks), len(detail_intro), len(detail_benefits),
                    len(detail_preferred_points), len(category_tags)  # , len(skill_tags_all_list)
                    ]
        if not len(set(listLens)) == 1:  # 길이가 다르면
            print("오류")
            sys.exit()

    # if end

    if len(page) >= interval:
        save_data_to_excel(idx)
        page, company, industry_name, due_time, position, skill_tags, country, location, hidden, status, address, \
            detail_requirements, detail_main_tasks, detail_intro, detail_benefits, detail_preferred_points, \
            category_tags = initialize_variables()

# 마지막에 남은거 한 번 더 실행하는 코드
if len(page) > 0:  # interval 배수인지 확인
    save_data_to_excel(idx)

print("end : ", datetime.now())
