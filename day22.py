import requests
r = requests.get("https://v1.hitokoto.cn/")
print(r.status_code)
data=r.json()
print(data["hitokoto"])
print(data["from"])
with open("hitokoto.txt","w",encoding="utf-8") as f:
    f.write(data["hitokoto"]) 
    f.write("出处:"+ data["from"] + "\n")
print(type(r.text))
print(type(data))
print(data["id"])

