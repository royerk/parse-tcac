import os
import urllib.request
import pandas as pd
import openpyxl

PROJECT_DIR = "parse_tcac"


def download_xlsx(dir_path):
    """
    Download all applications, to get the URL go to the application page and copy link from an application.
    :param dir_path: relative path to applications storage
    """
    # 2021 round 1: https://www.treasurer.ca.gov/ctcac/2021/applications/20210204/
    # 2021 round 2: https://www.treasurer.ca.gov/ctcac/2021/secondround/applications/
    url_format = "https://www.treasurer.ca.gov/ctcac/2021/secondround/applications/"

    year_last_2_digits = 21

    existing_files = os.listdir(dir_path)

    for counter in range(0, 1000):  # because sometimes some numbers are skipped
        file_name = f"{year_last_2_digits}-{counter}.xlsx"

        if counter < 100:  # formatting with leading 0 is annoying, this works
            a = str(counter)
            while len(a) < 3:
                a = "0" + a
            file_name = f"{year_last_2_digits}-{counter}.xlsx"

        if file_name in existing_files:
            print(f"{file_name} already downloaded, skipping.")
            continue

        url = url_format + file_name
        print(f"Attempting to download: {url}")

        try:
            urllib.request.urlretrieve(url, os.path.join(dir_path, file_name))
        except urllib.error.HTTPError:
            print(f"Warning, file {file_name} is not present, skipping.")


def read_xlsx(dir_path):
    """
    For each downloaded application read some cells.
    :param dir_path: relative path to applications storage
    """
    sheet_name = "Application"
    column = "AG"
    line = 977

    data = []
    existing_files = sorted(os.listdir(dir_path))
    for i, file_name in enumerate(existing_files):
        path = os.path.join(dir_path, file_name)
        print(f"Processing, {i+1}/{len(existing_files)}: {path}")

        work_book = openpyxl.load_workbook(path, data_only=True)
        sheet = work_book[sheet_name]
        value = sheet[f"{column}{line}"].value

        print(file_name, value)

        data.append({"id": file_name.split(".")[0], "pw": value})

    df = pd.DataFrame(data=data)

    return df


def main():
    destination = "toto"
    dir_path = os.path.join(PROJECT_DIR, destination)

    if not destination in os.listdir(PROJECT_DIR):
        print(f"Creating destination directory: {dir_path}")
        os.mkdir(dir_path)

    download_xlsx(dir_path)

    result = read_xlsx(dir_path)

    output_path = os.path.join(PROJECT_DIR, "toto.csv")
    result.to_csv(output_path, index=False)


if __name__ == "__main__":
    main()
