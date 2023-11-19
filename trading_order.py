import connect

# OAuth
REAL_APP_KEY = keyring.get_password('real_app_key','ucc0830')
REAL_APP_SECRET = keyring.get_password('real_app_secret','ucc0830')
TEST_APP_KEY = keyring.get_password('test_app_key','ucc0830')
TEST_APP_SECRET = keyring.get_password('test_app_secret','ucc0830')

# Service Domain
REAL_URL = "https://openapi.koreainvestment.com:9443"
TEST_URL = "https://openapivts.koreainvestment.com:29443"

# 국내주식주문
def select_stck_prpr():
	path = 'uapi/domestic-stock/v1/quotations/inquire-price'
	url = f"{TEST_URL}/{path}"
	headers = {"Content-Type":"application/json",
			"authorization": f"Bearer {TEST_ACCESS_TOKEN}",
			"appKey":TEST_APP_KEY,
			"appSecret":TEST_APP_SECRET,
			"tr_id":"FHKST01010100"}
	params = {
	    "fid_cond_mrkt_div_code":"J",
	    "fid_input_iscd":"005930"
	}
	res = requests.get(url, headers=headers, params=params)
	return res.json()['output']

# 해외주식주문
def select_stck_prpr():
	path = 'uapi/overseas-stock/v1/trading/order'
	url = f"{TEST_URL}/{path}"
	params = {
    	"CANO":"50099291",
		# "CANO":"68149836",
    	"ACNT_PRDT_CD":"01",
    	"OVRS_EXCG_CD":"NASD",
    	"PDNO":"TLT",
    	"ORD_QTY":"1",
    	"OVRS_ORD_UNPR":"0",
    	"CTAC_TLNO":"",
    	"MGCO_APTM_ODNO":"",
    	"SLL_TYPE":"",
    	"ORD_SVR_DVSN_CD":"0",
    	"ORD_DVSN":"00"
	}
	headers = {
		    "Content-Type":"application/json; charset=utf-8",
			"authorization": f"Bearer {TEST_ACCESS_TOKEN}",
			"appKey":TEST_APP_KEY,
			"appSecret":TEST_APP_SECRET,
			"personalseckey":"",
			"tr_id":"VTTT1002U",
			"tr_cont":"",
			"custtype":"P",
			"seq_no":"",
			"mac_address":"04-7C-16-43-EE-68",
			"phone_number":"01026167721",
			"ip_addr":"",
			"hashkey":hashkey(params),
			"gt_uid":""
    }
	
	res = requests.get(url, headers=headers, params=params)
	return res.json()['output']


