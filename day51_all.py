import requests
import json
from config import API_KEY
with open("dajin.txt","r",encoding="utf-8") as f:
    text=f.read()
def get_json_from_api(text:str):

    try:
        r=requests.post(headers={"Authorization":"Bearer "+API_KEY},json={"model":"glm-4-flash","messages":[{"content":'请把下面的内容给做成[{"事情": " ", "时间": " ", "地点": " "}]的数组格式，并且每一个数组只能有一个事件以及其对应的时间的地带你'+text,"role":"user"}],},url="https://open.bigmodel.cn/api/paas/v4/chat/completions",timeout=60)
    except Exception as e:
        return(f"出现了问题{e},现在重新尝试")
    if r.status_code!=200:
        return "请求失败，状态码:",r.status_code
    if r.status_code==200:
        d=r.json()
    if "error" in d:
        return ("请求失败，错误信息:",d["error"])
    line=d["choices"][0]["message"]["content"]
    line=json.loads(line[line.find("["):line.rfind("]")+1])
    with open("new_all.json","w",encoding="utf-8") as f:
        json.dump(line,f,ensure_ascii=False,indent=2)
    return line
def main():
    result=get_json_from_api(text)
    if result:
        print("成功获取到数据并保存到new_all.json")

if __name__ == "__main__":
    main()
