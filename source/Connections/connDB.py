import pyodbc
import pandas as pd
from Credentials import excel_credentials

CONN_DRIVER = "SQL Server"

sqlserver = excel_credentials['SQL_Server'][0]
sqluser = excel_credentials['SQL_User'][0] #RUN IN SQL SERVER 'SELECT SUPER_NAME()'
sqlpassword = excel_credentials['SQL_Password'][0]
sqldb = excel_credentials['SQL_Database'][0]

baseConnString = "Driver={{{Driver}}};Server={Server};Database={Database};Trusted_Connection=yes;"
connString = baseConnString.format(Driver = CONN_DRIVER, Server = sqlserver, Database = sqldb)

def cursor(connString):
    conn = pyodbc.connect(connString) #https://stackoverflow.com/questions/46045834/pyodbc-data-source-name-not-found-and-no-default-driver-specified #second solution
    cursor = conn.cursor()
    return cursor, conn

returnCursor = cursor(connString)
