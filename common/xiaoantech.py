from data.ECUdata import imei

# 小安协议网址
url = "http://api.xiaoantech.com/v1/device"

# 关键字
C59 = {"imei": imei, "cmd": {"c": 59, "param": {}}}
