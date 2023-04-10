import pandas as pd

EXCEL_PATH = r'D:\\DemoPowerBI\\demo_powerbi\\source\\PythonDataQualityChecker.xlsx'

excel_credentials = pd.read_excel(EXCEL_PATH, sheet_name= "Credentials")

excel_data = pd.read_excel(EXCEL_PATH, sheet_name= "Quality Check")