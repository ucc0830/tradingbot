from connect import *
from mykeyring import *

APP_KEY = keyring.get_password('app_key','ucc0830')
APP_SECRET = keyring.get_password('app_secret','ucc0830')
ACCESS_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6IjQ4YjNmNGFiLTU1NTAtNDM5ZC04ZGQ5LTMzZWZmYzFkYWZmOCIsImlzcyI6InVub2d3IiwiZXhwIjoxNzAwNDUyMjQ3LCJpYXQiOjE3MDAzNjU4NDcsImp0aSI6IlBTcW1jd2JDTGxuMVRtR05LUWZxSVJaSDlBYVAxYWhEWkFGQyJ9.cpL2a14Tm1EVvnvX2OCByvQV1bGE4YLPErL4ExuR6cEX4S7H01gL5gI3MvFoGhgho1umg9pokgGSNQHSOvokvw'

# 국내주식현재가 조회
def select_stck_prpr():
	path = 'uapi/domestic-stock/v1/quotations/inquire-price'
	url = f"{DOMAIN}/{path}"
	headers = {"Content-Type":"application/json",
			"authorization": f"Bearer {ACCESS_TOKEN}",
			"appKey":APP_KEY,
			"appSecret":APP_SECRET,
			"tr_id":"FHKST01010100"}
	body = {
	    "fid_cond_mrkt_div_code":"J",
	    "fid_input_iscd":"005930"
	}
	res = requests.get(url, headers=headers, body=body)
	return res.json()['output']

print(ACCESS_TOKEN)
print(select_stck_prpr)
