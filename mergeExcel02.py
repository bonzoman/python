import pandas as pd


def merge_excel_files(file_path, files):
    merged_df = pd.DataFrame()
    for file in files:
        df = pd.read_excel(file_path + file)
        temp_df = pd.DataFrame(df)
        # 합치기
        merged_df = pd.concat([merged_df, temp_df], ignore_index=True)

    # 합쳐진 데이터프레임을 새로운 엑셀 파일로 저장
    merged_df.to_excel('./WantedInfo_All.xlsx', index=False)


if __name__ == "__main__":
    merge_excel_files(file_path="./", files=["WantedInfo13027.xlsx",
                                             'WantedInfo24454.xlsx',
                                             'WantedInfo36181.xlsx'])

