import requests
import json
from config import API_KEY
s='{我今天早上从珠海送小金去东莞的大学体测，开回家已经中午了，下午休息一会，去做了个很喜欢的美甲，然后去打球，今晚上赢了，我觉得我打的不错，晚上又去打麻将，打完又去吃宵夜，回家已经2点多了}'
prompt=("你是我的助手，负责把我的句子信息给梳理成 '{'事件':  ,'地点':   }'\n"
        f"句子:{s}")
headers={"Authorization":"Bearer "+ API_KEY}
data={"model":"glm-4-flash","messages":[{"content":prompt,"role":"user"}]}

try:
    r=requests.post(headers=headers,json=data,url="https://open.bigmodel.cn/api/paas/v4/chat/completions"
)
    d=r.json()

except Exception as e:
    print(f"出现错误{e}")
if("error" in d):
    print(r.text)
if r.status_code==200:
    raw=d["choices"][0]["message"]["content"]
    print(type(raw))
    l=json.loads(raw.replace("'",'"'))##字符串变成了字典
    print(type(l))
    print(raw)
    print(l)
    