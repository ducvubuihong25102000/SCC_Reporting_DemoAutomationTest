import pyodbc
import random
import datetime
import os #dynamic take excel path
import pandas as pd
from faker import Faker
import faker_commerce as f


excelPath = r'D:\\DemoPowerBI\\demo_powerbi\\source\\PythonDataQualityChecker.xlsx'

excelLoad = pd.read_excel(excelPath,sheet_name=0)


sqlserver = excelLoad['SQL_Server'][0]
sqluser = excelLoad['SQL_User'][0] #RUN IN SQL SERVER 'SELECT SUPER_NAME()'
sqlpassword = ['SQL_Password'][0]
sqldb = excelLoad['SQL_Database'][0]
connDriver = "SQL Server"

baseConnString = "Driver={{{Driver}}};Server={Server};Database={Database};Trusted_Connection=yes;"
connString = baseConnString.format(Driver = connDriver, Server = sqlserver, Database = sqldb)

fakeObject = Faker()
fakeObject.add_provider(f.Provider)



query_cust = 'SELECT Id_Cust FROM dbo.Customer'
query_pro = 'SELECT Id_Pro FROM dbo.Product'
insert = "INSERT INTO dbo.Customer(CustName, CustPhone) VALUES ( \'{a}\', \'{b}\' )"
insert2 = 'INSERT INTO dbo.Product (ProName, InStock, Price) VALUES (\'{a}\', 1000, {b:.2f})'
insert_order = "INSERT INTO [dbo].[Order] (Id_Pro, Id_Cust, DateKey, Quantity) VALUES (\'{a}\', \'{b}\', \'{c}\', {d})"

 
# cnxn_str = (r"Driver={SQL Server};Server=DESKTOP-I5JKLU2\SQLEXPRESS;Database=DEMO;Trusted_Connection=yes;") 
conn = pyodbc.connect(connString) #https://stackoverflow.com/questions/46045834/pyodbc-data-source-name-not-found-and-no-default-driver-specified #second solution
cursor = conn.cursor()

list_product_id = [i[0] for i in cursor.execute(query_pro).fetchall()]
list_customer_id = [i[0] for i in cursor.execute(query_cust).fetchall()]
print(list_customer_id)

    
