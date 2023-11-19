import requests
import keyring
from mykeyring import *
from connect import *

APP_KEY = keyring.get_password('app_key','ucc0830')
APP_SECRET = keyring.get_password('app_secret','ucc0830')

ACCESS_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6IjQ4YjNmNGFiLTU1NTAtNDM5ZC04ZGQ5LTMzZWZmYzFkYWZmOCIsImlzcyI6InVub2d3IiwiZXhwIjoxNzAwNDUyMjQ3LCJpYXQiOjE3MDAzNjU4NDcsImp0aSI6IlBTcW1jd2JDTGxuMVRtR05LUWZxSVJaSDlBYVAxYWhEWkFGQyJ9.cpL2a14Tm1EVvnvX2OCByvQV1bGE4YLPErL4ExuR6cEX4S7H01gL5gI3MvFoGhgho1umg9pokgGSNQHSOvokvw'

# 해외주식 잔고 조회
def select_overseas_balance():
	path = 'uapi/overseas-stock/v1/trading/inquire-balance'
	url = f"{DOMAIN}/{path}"
	body = {
	"CANO":MYACCT,
    "ACNT_PRDT_CD":"01",
    "OVRS_EXCG_CD":"NASD",
    "TR_CRCY_CD":"USD",
    "CTX_AREA_FK200":"",
    "CTX_AREA_NK200":""
	}
	headers = {"Content-Type":"application/json; charset=utf-8",
			"authorization": f"Bearer {ACCESS_TOKEN}",
			"appKey":APP_KEY,
			"appSecret":APP_SECRET,
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
	res = requests.get(url, headers=headers, params=body)
	return res.json()


# 국내주식 잔고 조회
def select_domestic_balance():
	path = 'uapi/domestic-stock/v1/trading/inquire-balance'
	url = f"{DOMAIN}/{path}"
	print(url)
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
			"authorization": f"Bearer {ACCESS_TOKEN}",
			"appKey":APP_KEY,
			"appSecret":APP_SECRET,
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
	res = requests.get(url, headers=headers, params=body)
	return res.json()



print("주식 잔고 조회")
# result = select_domestic_balance()
result = select_overseas_balance()
print(result)