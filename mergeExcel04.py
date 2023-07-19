"""
기존파일에 내용추가(서식유지)
"""
import pandas as pd
from openpyxl import load_workbook


def append_to_excel(p_existing_file, p_new_data, p_save_path):
    # 기존 엑셀 파일 읽기
    existing_df = pd.read_excel(p_existing_file)

    # 새로운 데이터를 데이터프레임으로 변환
    new_df = pd.DataFrame(p_new_data)

    # 기존 데이터프레임과 새로운 데이터프레임을 병합
    merged_df = pd.concat([existing_df, new_df], ignore_index=True)

    # 엑셀 파일에 서식 유지하여 데이터 추가
    book = load_workbook(p_existing_file)
    writer = pd.ExcelWriter(p_save_path, engine='openpyxl')
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    merged_df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()


if __name__ == "__main__":
    existing_file = "./DataFiles/sample1.xlsx"
    new_data = {
        "Column1": [100, 200, 300],
        "Column2": ["A", "B", "C"]
    }
    save_path = "./DataFiles/새로운파일.xlsx"

    append_to_excel(existing_file, new_data, save_path)
