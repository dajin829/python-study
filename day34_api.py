"""第 34 天：把 ask() 变成网页接口（FastAPI 第一步）

之前：程序 = 终端里 input() 问、print() 答，只有你自己能用。
今天：程序 = 一个网址。浏览器、手机、别人的程序，都能发请求来拿回答。

分工：
  FastAPI 负责"把函数变成网址"——你写函数，它管收请求、发响应。
  你负责写两个函数：一个测活，一个聊天。

复用第 33 天的代码：ask() 和 SYSTEM_PROMPT 直接 import 过来，不重写。
（这就是"模块"的好处——day33_chat.py 里有 if __name__ == "__main__" 保护，
  所以 import 它不会顺带跑它的 main()。）
"""

from fastapi import FastAPI
import uvicorn

from day33_chat import ask, SYSTEM_PROMPT

app = FastAPI()


# ── 接口 1：/ping ——— 测试服务活着没有 ──────────────────────────
# 跑起来之后，浏览器访问 http://127.0.0.1:8000/ping
# 应该看到：{"status":"ok"}
#
# TODO 1：写函数体。return 一个字典 {"status": "ok"} 就行。
@app.get("/ping")
def ping():
    return{"status":"ok"}


# ── 接口 2：/chat?text=你想问的话 ——— 单轮问答 ────────────────────
# 浏览器访问 http://127.0.0.1:8000/chat?text=你好
# FastAPI 会自动把 ?text=你好 里的"你好"递给函数参数 text。
#
# TODO 2：先判断 text 是不是空字符串（strip 之后）
#         是空 → return {"error": "text 不能为空"}
# TODO 3：组装 messages：第 1 条 system（用 SYSTEM_PROMPT），第 2 条 user（用 text）
#         参照第 33 天 main() 里 history 的造法
# TODO 4：调 ask(messages)，把回答包进 {"reply": 回答} return 出去
#         ask 返回 None 时（请求失败），return {"error": "模型没答上来"}
@app.get("/chat")
def chat(text: str):
    if(text.strip()==""):
        return{"error":"text不能为空"}
    else:
        messages=[]
        messages.append({"content":SYSTEM_PROMPT,"role":"system"})
        messages.append({"content":text,"role":"user"})
        a=ask(messages)
        if(a):
            return {"reply":a}
        else:
            return{"error":"模型没答上来"}


if __name__ == "__main__":
    # uvicorn 是 FastAPI 自带的"服务器"，负责真正监听端口。
    # 三个参数照抄：哪个 app、监听哪台机器（本机）、哪个端口。
    uvicorn.run(app, host="127.0.0.1", port=8000)
