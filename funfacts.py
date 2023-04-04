import config
import requests

def getAccessToken():
	url = "https://accounts.spotify.com/api/token"
	headers = {
		"Content-Type": "application/x-www-form-urlencoded"
	}
	data = {
		"grant_type": "client_credentials",
		"client_id": config.clientID,
		"client_secret": config.clientSecret
	}
	response = requests.request("POST", url, headers=headers, data=data)
	print(response.json())


getAccessToken()