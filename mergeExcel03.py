import os

import pandas as pd
import glob


def merge_excel_files(file_path, file_format, save_path, save_format, columns=None):
    merge_df = pd.DataFrame()

    # 한줄 짜리
    # file_list = [f"{file_path}/{file}" for file in os.listdir(file_path) if file_format in file]

    # 여러줄 짜리
    file_list = []
    for file in os.listdir(file_path):
        if file_format in file:
            file_list.append(f"{file_path}/{file}")

    for file in file_list:
        if file_format == ".xlsx":
            file_df = pd.read_excel(file)
        else:
            file_df = pd.read_csv(file)

        if columns is None:
            columns = file_df.columns

        temp_df = pd.DataFrame(file_df, columns=columns)

        merge_df = pd.concat([merge_df, temp_df], ignore_index=True)

    if save_format == ".xlsx":
        merge_df.to_excel(save_path, index=False)
    else:
        merge_df.to_csv(save_path, index=False)


if __name__ == "__main__":
    merge_excel_files(file_path="./DataFiles",
                      file_format=".xlsx",
                      save_path="./DataFiles/sample_All.xlsx",
                      save_format=".xlsx")
