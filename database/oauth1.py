from yahoo_oauth import OAuth1
oauth = OAuth1(None, None, from_file='keys.json')

if not oauth.token_is_valid():
	oauth.refresh_access_token()