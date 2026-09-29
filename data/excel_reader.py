import openpyxl
from pathlib import Path


def get_excel_data(file_name="test_data.xlsx", sheet_name="Sheet1"):
    file_path = Path(__file__).resolve().parent / file_name
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]

    rows = list(sheet.iter_rows(values_only=True))
    headers = rows[0]
    data = []

    for row in rows[1:]:
        if any(row):  # skip empty rows
            data.append(dict(zip(headers, row)))

    return data