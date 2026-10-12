import requests
def hitokoto():
    r=requests.get("https://v1.hitokoto.cn/",timeout=5)
    data=r.json()
    return data["hitokoto"],data["from"]
a=0
while True:
    answer = input("要不要继续？")
    if answer=="y":
        a=a+1
        sentence,source=hitokoto()
        with open("hitokoto.txt","a",encoding="utf-8") as f:
            f.write(sentence + "来自《" + source +"》\n")
    if answer=="n":
        print(f"今天存入了{a}句")
        break
with open("hitokoto.txt","r",encoding="utf-8") as f:
    content=f.read()
print(content)
