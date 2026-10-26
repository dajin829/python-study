from fastapi import FastAPI
from day32_chat import URL
from config import API_KEY
import requests
from weather_ai import get_weather
import uvicorn
app=FastAPI()
@app.post("/weather")
def weather(playord:dict):
    city=playord.get("city")
    if not city:
        return {"error":"city为空"}
    weather=get_weather(city)
    if not weather:
        return {"error":"查不到这个城市的天气数据"}
    question=playord.get("question")
    if not question:
        question="明天出门需要注意什么"
    headers={"Authorization":"Bearer "+API_KEY}
    prompt=("你是一个天气助手\n"
        "请根据我给你的天气情况来回答我给你的问题\n"
        "不要自己编造回答,不会就说不知道，根据我给你的数据来回答\n"
        f"天气数据：{weather}\n"
        f"问题：{question}\n")
    data={"model":"glm-4-flash","messages":[{"content":prompt,"role":"user"}]}
    r=requests.post(headers=headers,json=data,url=URL)
    d=r.json()
    if "error" in d:
        return {"error":r.text}
    if r.status_code==200:
        return d["choices"][0]["message"]["content"]
if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
    ##@app.get	@app.post谁能调	浏览器地址栏直接输就行	必须用 requests.post(url, json={...}) 寄包裹（你今天写不了浏览器那一半，所以我给了 day37_test.py）数据在哪	网址尾巴 ?city=厦门	包裹 body 里，网址上看不见函数怎么收	参数名对号，一个参数收一个值	一个 dict 参数收下整个包裹数据量	网址一行，塞不下多少	随便装，传文档、传图片都行你的哪天	第 34–36 天（day36）	今天（day37）