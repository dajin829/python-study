"""第 34 天最小示例（老师写的）：世界上第一个只属于你的接口

第 22 天你是"客户"：requests.get 去别人家（hitokoto）拿一句话。
今天你当"店家"：自己开一个网址，把一句话说给来访问的人听。

只有 6 行有效代码，聊天里逐行讲。
"""

from fastapi import FastAPI
import uvicorn

app = FastAPI()                       # 1 造一个空的服务器程序


@app.get("/")                         # 2 登记：网址 / ↔ 下面的 home 函数
def home():                           # 3 来访问 / 时，执行这个函数
    return {"hitokoto": "慢慢来，比较快", "from": "大金"}   # 4 它收到的回复


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)   # 5-6 开门营业，守住 8000 端口
