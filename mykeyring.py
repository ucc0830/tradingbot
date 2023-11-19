import keyring

# 실전계좌
keyring.set_password('real_app_key'   , 'ucc0830', 'PSCrG4kyoD4dvQAIltvPN1i5oEXJOAlgpmHD')
keyring.set_password('real_app_secret', 'ucc0830', 'faMcSDN6t+kmFVngs6lV+PlkwPyj56ErNTNFVUhhUaCqW3ghf8TOvAfcQPbIww3IuzLisP4MA7wmPrw17cV2JLhGHXC7Klps07eQXaTcuMVl1VNRThTvD9AYh8/rdwBrwqxkSE80Dl79hrAUvaAUhPxfMkzw8EtgSi7DWeKXQTKNbPqDHOM=')
# 모의계좌
keyring.set_password('test_app_key'   , 'ucc0830', 'PSqmcwbCLln1TmGNKQfqIRZH9AaP1ahDZAFC')
keyring.set_password('test_app_secret', 'ucc0830', 'uVlXuEKLzy261USlc0cm1q21FbM1EvYsPzYfMqPvqEU8niGF9+tLsBAb7EfaDNvqGl2OZSH2REhf8mKznE/HruT3mbdxidCtdEVYUu0psVe6M9BoNlnwWyR6JhqSAwK3hhGWLeN5vmvZgGtl8lbJf0Tv37IW0JVh6YKUBsmNqR2fgV28BLc=')

# my_acct: "68149836"
global my_acct
my_acct = "50099291"
global my_phone
my_phone = "01026167721"

#domain info
#실전투자
global prod
prod = "https://openapi.koreainvestment.com:9443"
#웹소켓
global ops
ops = "ws://ops.koreainvestment.com:21000"
#모의투자서비스
global vts
vts = "https://openapivts.koreainvestment.com:29443" 