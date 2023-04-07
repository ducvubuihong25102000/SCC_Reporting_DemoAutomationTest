import msal
import requests

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
request_point_group = 'https://api.powerbi.com/v1.0/myorg/groups'
headers = {
    'Authorization' : f'Bearer {access_id}'
}

response_request = requests.get(request_point_group, headers= headers)
print(response_request.status_code)
print(response_request.json())
print('--------------------------------------------------')



# Check permission
if response_request.status_code == 200:
    result = response_request.json()
    for item in result['value']:
        print(item)
else:
    print('Refresh User Permissions')
    requests.post('https://api.powerbi.com/v1.0/myorg/RefreshUserPermissions', headers= headers)
    new_response_request = requests.get(request_point_group, headers= headers)
    print(new_response_request.status_code) 
    new_result = response_request.json()
    for new_item in new_result['value']:
        print(new_item)





# result = response_request.json()
# print(result)

# print(type(response_request))





