import pandas as pd

EXCEL_PATH = r'D:\\DemoPowerBI\\demo_powerbi\\source\\PythonDataQualityChecker.xlsx'

excel_credentials = pd.read_excel(EXCEL_PATH, sheet_name= "Credentials")
excel_data = pd.read_excel(EXCEL_PATH, sheet_name= "Quality Check")


APP_ID = '1ca92ebd-3d3b-40f8-b193-bc65b37a3a17' #client ID
DIR_ID = 'af9a7c3e-95a0-47a1-9094-0b53e29b012b' #tenant ID
OBJ_ID = '82ccab92-5228-4de0-a788-d4b290ebfcc1'
USER_NAME = '030134180244@st.buh.edu.vn'
USER_PASSWORD = 'Hongduc25102000'

AUTH_MICROSOFT_URL =  'https://login.microsoftonline.com/'
SCOPE = ['https://analysis.windows.net/powerbi/api/.default']

AUTHEN_URL = AUTH_MICROSOFT_URL + DIR_ID