"""第 36 天 · 任务：凭记忆默写骨架

规则：不看 day35_weather_api.py，不看昨天的记忆卡。卡住了就喊老师，
只报告"我卡在第几块"，按提示阶梯来，不直接给答案。

要写的接口：
    /weather?city=厦门&question=要不要带伞
    - city    必填，空了要拦
    - question 可选，不传就用默认值"明天出门要注意什么？"

写完先自己跑，三个地址都测，再加一个不带 question 的：
    /weather?city=厦门
    /weather?city=
    /weather?city=asdasdzxc
    /weather?city=厦门&question=要不要带"""
from weather_ai import get_weather,advise
from fastapi import FastAPI
import uvicorn
app=FastAPI()
@app.get("/weather")
def weather(city:str,question:str="明天出门要注意什么？"):
    if city.strip()=="":
        return{"error":"没有输入要查询的城市"}
    a=get_weather(city)
    if not a:
        return {"error":"查不到此城市"}
    else:
        b=advise(a,question)
    if b:
        return b
    else:
        return {"error":"模型没答上来"}

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)