import requests
import json
from config import API_KEY
a=True

kong=[]
with open("notes.txt","r",encoding="utf-8") as f:
    lines =f.readlines()
for line in lines:
    prompt='请把下面的内容给做成{"事情": " ", "时间": " ", "地点": " "}的格式'+line
    line=line.strip()
    if not line:
        continue
    headers={"Authorization":"Bearer "+API_KEY}
    data={"model":"glm-4-flash","messages":[{"content":prompt,"role":"user"}]}
    try:
        r=requests.post(headers=headers,json=data,url="https://open.bigmodel.cn/api/paas/v4/chat/completions",timeout=60)
    except Exception as e:
        print("请求出错:",e)
        a=False
        continue
    if a==False:
        print("请求出错，程序终止")
        break
    if r.status_code!=200:
        print("请求失败，状态码:",r.status_code)
        break
    d=r.json()
    if "error" in d:
        print("请求失败，错误信息:",d["error"])
        break
    line=d["choices"][0]["message"]["content"]
    line=json.loads(line[line.find("{"):line.rfind("}")+1])
    kong.append(line)
with open("batch.json","w",encoding="utf-8") as f:
    json.dump(kong,f,ensure_ascii=False,indent=2)