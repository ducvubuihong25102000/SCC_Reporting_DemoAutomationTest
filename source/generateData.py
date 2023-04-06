from faker import Faker
import faker_commerce
import random
import datetime
import connection #file
 
 
cursor = connection.returnCursor
fakeObject = Faker()
fakeObject.add_provider(faker_commerce.Provider)


query_cust = 'SELECT Id_Cust FROM dbo.Customer'
query_pro = 'SELECT Id_Pro FROM dbo.Product'


insert_cust = "INSERT INTO dbo.Customer(CustName, CustPhone) VALUES ( \'{a}\', \'{b}\' )"
insert_pro = 'INSERT INTO dbo.Product (ProName, InStock, Price) VALUES (\'{a}\', 1000, {b:.2f})'
insert_order = "INSERT INTO [dbo].[Order] (Id_Pro, Id_Cust, DateKey, Quantity) VALUES (\'{a}\', \'{b}\', \'{c}\', {d})"

    
#CUSTOMER
for i in range(0,10):
    a = fakeObject.name()
    b = fakeObject.phone_number()
    execution = insert_cust.format(a = a, b = b)
    print(execution)
    cursor[0].execute(execution)
    cursor[1].commit()


# [PRODUCT]
for i in range(0,10):
    a = fakeObject.ecommerce_name()
    b = random.random()*1000
    execution = insert_pro.format(a = a, b = b)
    print(execution)
    cursor[0].execute(execution)
    cursor[1].commit()


# INSERT ORDER TABLE
for j in range (0,30):
    for i in range(0, 30):
        a = random.choice([i[0] for i in cursor[0].execute(query_pro).fetchall()])
        b = random.choice([i[0] for i in cursor[0].execute(query_cust).fetchall()])
        c = str(datetime.date.today() - datetime.timedelta(days=j)).replace("-","")
        d = random.randrange(1, 10) 
        execution = insert_order.format(a = a, b = b, c=c, d=d)
        print(execution)
        cursor[0].execute(execution)
        cursor[1].commit()
        pass