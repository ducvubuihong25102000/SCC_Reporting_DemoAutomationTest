import msal
from source.Connections.Credentials import APP_ID, USER_NAME, USER_PASSWORD, SCOPE, AUTHEN_URL


# Get access token
app_instance = msal.PublicClientApplication(APP_ID, authority = AUTHEN_URL)
response =  app_instance.acquire_token_by_username_password(username= USER_NAME, password= USER_PASSWORD, scopes= SCOPE)
access_token = response['access_token']

headers = {
    'Authorization' : f'Bearer {access_token}'
}
