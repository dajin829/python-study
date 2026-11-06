import requests
import json
from config import API_KEY
def clean(s:str ):
    prompt=("你是我的助手，负责把我给你的句子中的信息整理JSON:{'事件':[],'地点':[]}"
    f"句子:{s}")
    headers={"Authorization":"Bearer "+API_KEY}
    data={"model":"glm-4-flash","messages":[{"content":prompt,"role":"user"}]}
   
    try:
         r=requests.post(headers=headers,json=data,url="https://open.bigmodel.cn/api/paas/v4/chat/completions")
         d=r.json()
    except Exception as e:
         print(f"出现了错误:{e}")
         return None
    if "error" in d:
         print(f"出现了错误:{d['error']}")
         return None
    if r.status_code==200:
         l=d["choices"][0]["message"]["content"] 
         i=l.find("{")
         m=l.rfind("}")## find("{") + rfind("}")就是拿位置
         
    try:
         return json.loads(l[i:m+1])
    except Exception as e:
         print(f"出现了错误:{e}")
         return None

l="我今天早上从珠海送小金去东莞的大学体测，开回家已经中午了，下午休息一会，去做了个很喜欢的美甲，然后去打球，今晚上赢了，我觉得我打的不错，晚上又去打麻将，打完又去吃宵夜，回家已经2点多了"
s="我今天早上十一点起床坐高铁回厦门，六点才到，然后去吃了个猪脚饭，拿了我的新鞋子，但是有一点点小"
print(clean(l))
print(clean(s))
print(clean(" "))