# Solution add specific path by system path
# import sys
# sys.path.insert(0,'D:\\DemoPowerBI\\demo_powerbi\\source\\') #Add path for Connections package
# sys.path.insert(1, 'D:\\DemoPowerBI\\demo_powerbi\\source\\Connections\\') #Add path for Cendential package

from source.Connections import connDB as conn

query_cust = 'SELECT Id_Cust FROM dbo.Customer'
query_pro = 'SELECT Id_Pro FROM dbo.Product'

cursor = conn.returnConn[0]

list_product_id = [i[0] for i in cursor.execute(query_pro).fetchall()]
list_customer_id = [i[0] for i in cursor.execute(query_cust).fetchall()]
print(list_customer_id)
print(list_product_id)