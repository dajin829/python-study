import requests
from config import  API_KEY
def ask(question):
    headers = {"Authorization": "Bearer " + API_KEY}#headers —— 你是谁的证明 Authorization 的意思是“授权”——谁在请求。Bearer 读作“持有者”，意思是“我手里有票”，后面跟你的 key。
    data = {"model":"glm-4-flash","messages":[{"content":question,"role":"user"}]}
    r=requests.post(headers = headers,json = data ,url ="https://open.bigmodel.cn/api/paas/v4/chat/completions",timeout=60 )
    print(r.status_code)
    d=r.json()
    if "error" in d:
        print(r.text)
        return None

    print(d["choices"][0].keys())
    return d["choices"][0]["message"]["content"]
def main():
    question=input("请输入你的问题")
    print(ask(question))

if __name__=="__main__":
    main()