import pandas as pd

# قراءة ملف Excel
excel_path = r'../DOCS/shahania_forms_catalog.xlsx'
df = pd.read_excel(excel_path, sheet_name=None)

# طباعة أسماء الأوراق والحقول
for sheet_name, sheet_df in df.items():
    print(f'--- Sheet: {sheet_name} ---')
    print(sheet_df.head(10))
    print('\n')

