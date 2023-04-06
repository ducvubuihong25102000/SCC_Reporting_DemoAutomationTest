import pyodbc
import pandas as pd


CONN_DRIVER = "SQL Server"
EXCEL_PATH = r'D:\\DemoPowerBI\\demo_powerbi\\source\\PythonDataQualityChecker.xlsx'



excelLoad = pd.read_excel(EXCEL_PATH,sheet_name=0)

sqlserver = excelLoad['SQL_Server'][0]
sqluser = excelLoad['SQL_User'][0] #RUN IN SQL SERVER 'SELECT SUPER_NAME()'
sqlpassword = ['SQL_Password'][0]
sqldb = excelLoad['SQL_Database'][0]

baseConnString = "Driver={{{Driver}}};Server={Server};Database={Database};Trusted_Connection=yes;"
connString = baseConnString.format(Driver = CONN_DRIVER, Server = sqlserver, Database = sqldb)

def cursor(connString):
    conn = pyodbc.connect(connString) #https://stackoverflow.com/questions/46045834/pyodbc-data-source-name-not-found-and-no-default-driver-specified #second solution
    cursor = conn.cursor()
    return cursor, conn

returnCursor = cursor(connString)
