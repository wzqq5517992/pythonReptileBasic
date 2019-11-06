# coding=utf-8
import requests
import json
import sys

headers = {
"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
post_data = {
    # "query":"你好",
    # "from":"zh",
    # "to":"en",
    "from": "en",
    "to": "zh",
    "query": "hola",
    "sign": "372549.85108",
    "token": "e262887a4d4b12815e2e27cf307036ca"
}

post_url = "http://fanyi.baidu.com/basetrans"

r = requests.post(post_url, data=post_data, headers=headers)
print(r.content.decode())
dict_ret = json.loads(r.content.decode())
ret = dict_ret["trans"][0]["dst"]
print("result is :", ret)
