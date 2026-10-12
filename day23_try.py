import requests
def get_hitokoto():
    try:
        r=requests.get("https://v1.hitokoto.cn/",timeout=5)#timeout就是最多等五秒 久了就放弃
        if(r.status_code == 200):
            data=r.json()
            return data["hitokoto"],data["from"]
    except Exception as e:
        print("出错了：",e)
    return "获取失败","无"
sentence,source=get_hitokoto()
print(f"{sentence},{source}")
with open("hitokoto.txt","a",encoding="utf-8") as f:
    f.write(f"{sentence}——来自{source}\n")