"""第 37 天 · 先教：POST 是什么（最小示例，8 行有效代码）

访问方式跟 GET 完全不同——不能在浏览器地址栏输，
要用"寄包裹"的方式（requests.post），见 day37_test.py。

注意：这个文件是"教材"，别在这里改代码——你的作业写在 day37_weather_api.py。
"""
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/echo")
def echo(payload: dict):
    # payload: dict 的意思是——把寄来的 JSON 包裹整个递给我，当字典用
    return {"你寄来的包裹": payload}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
