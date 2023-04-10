import requests
import json
from source.Connections.connPBIService import headers

# Get Rest API list of workspace
request_list_workspace = 'https://api.powerbi.com/v1.0/myorg/groups'

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