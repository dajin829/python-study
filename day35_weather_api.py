"""第 35 天：把天气接进接口 —— 这个接口真的"知道现在"

昨天 /chat 只会说话：问它厦门明天热不热，它只能答"请查看天气预报"，因为
那条接口里根本没有天气数据。

今天把第 31 天写好的两个函数接进来，链路变成：
    浏览器 ?city=厦门 → wttr.in 查真数据 → 模型根据数据给建议 → JSON 回去

做好之后，访问 http://127.0.0.1:8000/weather?city=厦门 会看到这种结构：
{
  "city": "厦门",
  "weather": "城市：厦门\\n日期：2026-10-24\\n最高温：28度\\n...",
  "advice": "明天最高温 28 度、紫外线较强，出门记得防晒。"
}

今天没有新语法。全是旧知识：import、if 判空、调函数、return 字典。
"""

from fastapi import FastAPI
import uvicorn

from weather_ai import get_weather, advise    # 第 31 天写好的两个函数，直接借

app = FastAPI()


@app.get("/weather")
def weather(city: str):
    # TODO 1：city 为空（strip 之后）→ return {"error": "city 不能为空"}
    if city.strip()=="":
        return {"error": "city不能为空"}
    # TODO 2：wt = get_weather(city) 查天气
    #         查不到（返回 None）→ return {"error": "查不到这个城市的天气，换个城市试试"}
    wt=get_weather(city)
    if not wt:
        return{"error":"查不到这个城市的天气"}
    # TODO 3：a = advise(wt, "明天出门要注意什么？") 让模型根据天气数据给建议
    #         拿不到（返回 None）→ return {"error": "模型没答上来"}
    a=advise(wt,"明天出门应该穿什么？")
    if a:
        print(a)
    else:
        return{"error":"模型没答上来"}

    # TODO 4：都拿到了 → return {"city": city, "weather": wt, "advice": a}
    return {"city":city,"weather":wt,"advice":a}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
