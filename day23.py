import requests
def get_hitokoto():
    r=requests.get("https://v1.hitokoto.cn/")
    data=r.json()
    return data["hitokoto"],data["from"]

sentence,source=get_hitokoto()
print(f"{sentence}——出自《{source}》")