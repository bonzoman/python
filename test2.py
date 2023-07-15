import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

POSTING_NUM_LIST = []
JOB_DESC_LIST = []  # 공고내용(col-md-12)
TITLE_LIST = []  # 채용공고 제목(tm_mgt_title)
COMPANY_NAME_LIST = []  # 회사이름 (tm_h2_title_company_info)
CATEGORY_LIST = []  # 부문 (rc_categories_name)
URL_LIST = []


def makeurl():
    for idx in range(170491, 170492):
        url = "https://www.wanted.co.kr/wd/" + str(idx)
        URL_LIST.append(url)


# M A I N
makeurl()


ABC = ["A1", "B1", "C1", "D1"]
columns = ["회사이름", "직무", "유사직무", "채용내용"]

write_wb = Workbook()
write_ws = write_wb.active

# Head Columns 만들기
for i, URL in enumerate(URL_LIST):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    soup = str(soup)

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
