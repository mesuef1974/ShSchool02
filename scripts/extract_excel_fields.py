import openpyxl
wb = openpyxl.load_workbook(r'/DOCS/shahania_forms_catalog.xlsx')
for ws in wb.worksheets:
    print(f'--- Sheet: {ws.title} ---')
    for i, row in enumerate(ws.iter_rows(values_only=True)):
        print(row)
        if i > 10:
            break

