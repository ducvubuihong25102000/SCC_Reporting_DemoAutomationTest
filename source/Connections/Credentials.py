import pandas as pd

EXCEL_PATH = r'D:\\DemoPowerBI\\PythonDataQualityChecker.xlsx'

excel_credentials = pd.read_excel(EXCEL_PATH, sheet_name= "Credentials")
excel_quality = pd.read_excel(EXCEL_PATH, sheet_name= "Quality Check")


APP_ID = excel_credentials['PBI_ClientID'][0] #client ID
DIR_ID = 'af9a7c3e-95a0-47a1-9094-0b53e29b012b' #tenant ID
OBJ_ID = '82ccab92-5228-4de0-a788-d4b290ebfcc1'
USER_NAME = excel_credentials['PBI_Username'][0]
USER_PASSWORD = excel_credentials['PBI_Password'][0]

AUTH_MICROSOFT_URL =  'https://login.microsoftonline.com/'
SCOPE = ['https://analysis.windows.net/powerbi/api/.default']

AUTHEN_URL = AUTH_MICROSOFT_URL + DIR_ID