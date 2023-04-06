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

# INSERT ORDER TABLE
# for j in range (0,30):
#     for i in range(0, 30):
#         a = random.choice(list_product_id)
#         b = random.choice(list_customer_id)
#         c = str(datetime.date.today() - datetime.timedelta(days=j)).replace("-","")
#         d = random.randrange(1, 10) 
#         execution = insert_order.format(a = a, b = b, c=c, d=d)
#         print(execution)
#         cursor.execute(execution)
#         conn.commit()
#         pass
    
#CUSTOMER
# for i in range(0,10):
#     a = fakeObject.name()
#     b = fakeObject.phone_number()
#     execution = insert.format(a = a, b = b)
#     print(execution)
#     cursor.execute(execution)
#     conn.commit()


# [PRODUCT]
# for i in range(0,10):
#     a = fakeObject.ecommerce_name()
#     b = random.random()*1000
#     execution = insert2.format(a = a, b = b)
#     print(execution)
#     cursor.execute(execution)
#     conn.commit()

# result = cursor.execute(query2).fetchall()
# for row in result:
#     print(row)
    
