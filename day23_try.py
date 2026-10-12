import requests
def get_hitokoto():
    try:
        r=requests.get("https://v1.hitokoto.cn/",timeout=5)#timeout就是最多等五秒 久了就放弃
        if(r.status_code == 200):
            data=r.json()
            return data["hitokoto"],data["from"]
    except Exception as e:
        print("出错了：",e)#except = "如果 try 里出了错，就执行我这一块"Exception = 所有常规错误的"总类"​。ValueError、KeyError、超时、域名找不到……全都是它的子孙as= e给这次抓到的错误起个名字叫 e，方便下面用它
    return "获取失败","无"
sentence,source=get_hitokoto()
print(f"{sentence},{source}")
with open("hitokoto.txt","a",encoding="utf-8") as f:
    f.write(f"{sentence}——来自{source}\n")