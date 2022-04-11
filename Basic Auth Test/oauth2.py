from http import client
from oauthlib.oauth2 import WebApplicationClient
from config.credentials import user

client = WebApplicationClient(user.client_id)

authorization_url = 'https://api.1up.health/user-management/v1/user/auth-code'

url = client.prepare_request_uri(
    authorization_url
    # app_user_id = 'my_first_user',
    # client_id = user.client_id,
    # client_secret = user.client_secret
)

print(url)

data = client.prepare_refresh_body(
    app_user_id = 'my_first_user',
    client_id = user.client_id,
    client_secret = user.client_secret
)

print(data)