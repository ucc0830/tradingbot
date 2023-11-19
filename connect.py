import requests
import keyring
import json
import datetime
import time
from mykeyring import *

# TEST
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6IjQ4YjNmNGFiLTU1NTAtNDM5ZC04ZGQ5LTMzZWZmYzFkYWZmOCIsImlzcyI6InVub2d3IiwiZXhwIjoxNzAwNDUyMjQ3LCJpYXQiOjE3MDAzNjU4NDcsImp0aSI6IlBTcW1jd2JDTGxuMVRtR05LUWZxSVJaSDlBYVAxYWhEWkFGQyJ9.cpL2a14Tm1EVvnvX2OCByvQV1bGE4YLPErL4ExuR6cEX4S7H01gL5gI3MvFoGhgho1umg9pokgGSNQHSOvokvw

# OAuth
APP_KEY = keyring.get_password('app_key','ucc0830')
APP_SECRET = keyring.get_password('app_secret','ucc0830')

last_auth_time = datetime.datetime.now()
ACCESS_TOKEN = ""

# 엑세스토큰 발급
def auth():
	headers = {"content-type":"application/json"}
	body = {"grant_type":"client_credentials",
			"appkey":APP_KEY,
			"appsecret":APP_SECRET}
	PATH = "oauth2/tokenP"
	URL = f"{DOMAIN}/{PATH}"

	res = requests.post(URL, headers=headers, data=json.dumps(body))
	rescode = res.status_code
	if rescode == 200:
		global ACCESS_TOKEN
		ACCESS_TOKEN = res.json()["access_token"]
		print('[SUCCESS] 인증 토큰 발급 성공')
		global last_auth_time
		last_auth_time = datetime.datetime.now()
		return ACCESS_TOKEN
	else:
		print('[FAIL] 인증 토큰 발급 실패')

def hashkey(body):
	PATH = "uapi/hashkey"
	URL = f"{DOMAIN}/{PATH}"
	headers = {
	'content-Type' : 'application/json',
	'appKey' : APP_KEY,
	'appSecret' : APP_SECRET,
	}
	res = requests.post(URL, headers=headers, data=json.dumps(body))
	hashkey = res.json()["HASH"]
	return hashkey


