import msal
import requests
import json

APP_ID = '1ca92ebd-3d3b-40f8-b193-bc65b37a3a17' #client ID
DIR_ID = 'af9a7c3e-95a0-47a1-9094-0b53e29b012b' #tenant ID
OBJ_ID = '82ccab92-5228-4de0-a788-d4b290ebfcc1'
USER_NAME = '030134180244@st.buh.edu.vn'
USER_PASSWORD = 'Hongduc25102000'

AUTHO_MICROSOFT_URL =  'https://login.microsoftonline.com/'
SCOPE = ['https://analysis.windows.net/powerbi/api/.default']

authority_url = AUTHO_MICROSOFT_URL + DIR_ID

# Get access token
app_instance = msal.PublicClientApplication(APP_ID, authority = authority_url)
response =  app_instance.acquire_token_by_username_password(username= USER_NAME, password= USER_PASSWORD, scopes= SCOPE)
access_id = response['access_token']


# print(type(response))
# print(response.keys())
# print('-------------------------------------------------')
# print(response['access_token'])



# Get Rest API list of workspace
request_list_workspace = 'https://api.powerbi.com/v1.0/myorg/groups'
headers = {
    'Authorization' : f'Bearer {access_id}'
}

response_list_workspace = requests.get(request_list_workspace, headers= headers)
print(response_list_workspace.status_code)
print(response_list_workspace.json())
print('--------------------------------------------------')



# Check permission
if response_list_workspace.status_code == 200:
    result = response_list_workspace.json()
    for item in result['value']:
        # print(item)
        # Get list of dataset in each workspace
        request_list_datasets = f'https://api.powerbi.com/v1.0/myorg/groups/{item["id"]}/datasets'
        print(request_list_datasets)
        response_list_datasets = requests.get(request_list_datasets, headers= headers)
        print(item['name'])
        print(item['id'])
        print(response_list_datasets.status_code)
        for item in response_list_datasets.json()['value']:
            print(item['id']) 
        print('--------------------------------------------------')

        
else:
    print('Refresh User Permissions')
    requests.post('https://api.powerbi.com/v1.0/myorg/RefreshUserPermissions', headers= headers)
    new_response_request = requests.get(request_list_workspace, headers= headers)
    print(new_response_request.status_code) 
    new_result = new_response_request.json()
    for new_item in new_result['value']:
        print(new_item)






# DAX query request
DAX_query = {
    # 'query1': r'MEASURE \'Order\'[DemoSum] SUM(\'Order\'[Quantity]) FROM  GROUPBY(\'Order\'[Id_Cust])'
    'queries' : [
        {
            'query': r'EVALUATE VALUES(Customer)'
        }
    ],
    "serializerSettings": {
    "includeNulls": True
    } 
}
datasetId = '753c0d56-2e7e-42f0-a29c-3648a45c022d' # Get from above API
request_datasets_query = f'https://api.powerbi.com/v1.0/myorg/datasets/{datasetId}/executeQueries'
print(request_datasets_query)
response_datasets_query = requests.post(request_datasets_query, headers= headers, json= DAX_query)
print(response_datasets_query.status_code)
clean_response_datasets_query = json.dumps(response_datasets_query.json(), indent= 2)
print(clean_response_datasets_query)
print(type(clean_response_datasets_query))


## Check permission to action in Dataset
# groupId = '908218c2-5294-4680-8130-5286c77872ed'

# # temp = f'https://api.powerbi.com/v1.0/myorg/datasets/{datasetId}/tables'
# temp = f'https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets/{datasetId}'
# print(temp)
# temprun = requests.get(temp, headers = headers)
# print(temprun.status_code)
# print(temprun.json().keys())