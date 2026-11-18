import requests
import json
from config import API_KEY
with open("dajin.txt","r",encoding="utf-8") as f:
    text=f.read()
def get_json_from_api(text:str):
    if text.strip()=="":
        return None

    try:
        r=requests.post(headers={"Authorization":"Bearer "+API_KEY},json={"model":"glm-4-flash","messages":[{"content":'请把下面的内容给做成[{"事情": " ", "时间": " ", "地点": " "}]的数组格式，并且每一个数组只能有一个事件以及其对应的时间的地带你，没有具体事件就返回 []，不要编造'+text,"role":"user"}],},url="https://open.bigmodel.cn/api/paas/v4/chat/completions",timeout=60)
    except Exception as e:
        print(f"出现了问题,现在重新尝试{e}")
        return None
    if r.status_code!=200:
        print(f"请求失败，状态码:{r.status_code}")
        return None
    if r.status_code==200:
        d=r.json()
    if "error" in d:
        print(f"请求失败，错误信息:{d['error']}")
        return None
    line=d["choices"][0]["message"]["content"]
    line=json.loads(line[line.find("["):line.rfind("]")+1])
    ok=[]
    for x in line:
        if x["事情"].strip():
            ok.append(x)
    line=ok
    with open("new_all.json","w",encoding="utf-8") as f:
        json.dump(line,f,ensure_ascii=False,indent=2)
    return line
def main():
    if not text.strip():
        print("输入文本为空，未进行请求。")
    else:
        result=get_json_from_api(text)
        if result:
            print("成功获取到数据并保存到new_all.json")
        else:
            print("请求失败，未获取到数据。")
if __name__ == "__main__":
    main()
