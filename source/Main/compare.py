
from time import time

start = time()

from source.Main.getDataDB import df
from source.Main.getDataPBIService import df_pbi

if (df.equals(df_pbi)):
    print("Data from Power BI Service and DB is matching !!!")
    print('Time after compare: ' + str(time() - start))
else:
    print("Data is not matching!!!")
    print('Time after compare: ' + str(time() - start))

