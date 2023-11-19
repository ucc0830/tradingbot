from connect import *

print("해외주식 잔고 조회")
result = select_overseas_balance()
print(result)

print(last_auth_time)