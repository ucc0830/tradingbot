import requests
import keyring
import json
import mykeyring
import datetime


# OAuth
# REAL_APP_KEY = keyring.get_password('real_app_key','ucc0830')
# REAL_APP_SECRET = keyring.get_password('real_app_secret','ucc0830')
TEST_APP_KEY = keyring.get_password('test_app_key','ucc0830')
TEST_APP_SECRET = keyring.get_password('test_app_secret','ucc0830')

# Service Domain
# REAL_URL = "https://openapi.koreainvestment.com:9443"
TEST_URL = "https://openapivts.koreainvestment.com:29443"

def get_access_token():
	headers = {"content-type":"application/json"}
	body = {"grant_type":"client_credentials",
			"appkey":TEST_APP_KEY,
			"appsecret":TEST_APP_SECRET}
	PATH = "oauth2/tokenP"
	URL = f"{TEST_URL}/{PATH}"
	res = requests.post(URL, headers=headers, data=json.dumps(body))
	rescode = res.status_code
	if rescode == 200:
		print('[SUCCESS] 인증 토큰 발급 성공')
		ACCESS_TOKEN = res.json()["access_token"]
	else:
		print('[FAIL] 인증 토큰 발급 실패')
	global last_auth_time
	last_auth_time = datetime.datetime.now()
	print(last_auth_time)
	return ACCESS_TOKEN

# REAL_ACCESS_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6IjIyNTc4MTkyLWViOGUtNDZkZC1hOTc2LTVjNTU0MTg0NTAwZiIsImlzcyI6InVub2d3IiwiZXhwIjoxNzAwMzc3NDc0LCJpYXQiOjE3MDAyOTEwNzQsImp0aSI6IlBTQ3JHNGt5b0Q0ZHZRQUlsdHZQTjFpNW9FWEpPQWxncG1IRCJ9.Xz4_gU2Q6BnYBHJMkAIYdqaoqBb-S6QYyTwXUmDQ6UJ_l_PlGNerJGGvYfGmcaQox2WgmTqcAffYaSHwVZof0Q'
# TEST_ACCESS_TOKEN = get_access_token()


def hashkey(datas):
	PATH = "uapi/hashkey"
	URL = f"{TEST_URL}/{PATH}"
	headers = {
	'content-Type' : 'application/json',
	'appKey' : TEST_APP_KEY,
	'appSecret' : TEST_APP_SECRET,
	}
	res = requests.post(URL, headers=headers, data=json.dumps(datas))
	hashkey = res.json()["HASH"]
	return hashkey

# 국내주식현재가 조회
def select_stck_prpr():
	path = 'uapi/domestic-stock/v1/quotations/inquire-price'
	url = f"{TEST_URL}/{path}"
	headers = {"Content-Type":"application/json",
			"authorization": f"Bearer {TEST_ACCESS_TOKEN}",
			"appKey":TEST_APP_KEY,
			"appSecret":TEST_APP_SECRET,
			"tr_id":"FHKST01010100"}
	body = {
	    "fid_cond_mrkt_div_code":"J",
	    "fid_input_iscd":"005930"
	}
	res = requests.get(url, headers=headers, body=body)
	return res.json()['output']

# 해외주식 잔고 조회
def select_overseas_balance():
	path = 'uapi/overseas-stock/v1/trading/inquire-balance'
	url = f"{TEST_URL}/{path}"
	body = {
    # "CANO":"68149836",
	"CANO":"50099291",
    "ACNT_PRDT_CD":"01",
    "OVRS_EXCG_CD":"NASD",
    "TR_CRCY_CD":"USD",
    "CTX_AREA_FK200":"",
    "CTX_AREA_NK200":""
	}
	headers = {"Content-Type":"application/json; charset=utf-8",
			"authorization": f"Bearer {TEST_ACCESS_TOKEN}",
			"appKey":TEST_APP_KEY,
			"appSecret":TEST_APP_SECRET,
			"personalseckey":"",
			"tr_id":"VTTS3012R",
			"tr_cont":"",
			"custtype":"P",
			"seq_no":"",
			"mac_address":"04-7C-16-43-EE-68",
			"phone_number":"01026167721",
			"ip_addr":"",
			"hashkey":"",
			"gt_uid":""
	}
	res = requests.get(url, headers=headers, body=body)
	return res.json()

# 국내주식 잔고 조회
def select_domestic_balance():
	path = 'uapi/domestic-stock/v1/trading/inquire-balance'
	url = f"{TEST_URL}/{path}"
	body = {
    	"CANO":"50099291",
		# "CANO":"68149836",
    	"ACNT_PRDT_CD":"01",
    	"AFHR_FLPR_YN":"N",
    	"OFL_YN":"",
    	"INQR_DVSN":"02",
    	"UNPR_DVSN":"01",
    	"FUND_STTL_ICLD_YN":"N",
    	"FNCG_AMT_AUTO_RDPT_YN":"N",
    	"PRCS_DVSN":"00",
    	"CTX_AREA_FK100":"",
    	"CTX_AREA_NK100":""
	}
	headers = {"Content-Type":"application/json; charset=utf-8",
			"authorization": f"Bearer {TEST_ACCESS_TOKEN}",
			"appKey":TEST_APP_KEY,
			"appSecret":TEST_APP_SECRET,
			"personalseckey":"",
			"tr_id":"VTTC8434R",
			"tr_cont":"",
			"custtype":"P",
			"seq_no":"",
			"mac_address":"04-7C-16-43-EE-68",
			"phone_number":"01026167721",
			"ip_addr":"",
			"hashkey":hashkey(body),
			"gt_uid":""
	}
	res = requests.get(url, headers=headers, body=body)
	return res.json()


print((datetime.now() - datetime.now()).seconds)