# day39_page.py —— 完整能跑的天气网页（教材版）。
# 今天你的任务不是写它，是【改】它：改标题、改提示语、改颜色，
# 每改一处就 Ctrl+C 停掉重跑，浏览器里看到自己的改动，就算学会一处。

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from weather_ai import get_weather, advise
import uvicorn

app = FastAPI()


# 公共函数：每一页的"外壳"。标题 + 内容拼在一起，包上 HTML 的固定结构。
def page(title, body):
    return f"""<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <style>
        body {{ font-family: sans-serif; max-width: 460px; margin: 60px auto;color:blue; }}
        input {{ padding: 8px; margin-right: 6px; }}
        button {{ padding: 8px 22px; }}
        .card {{ border: 1px solid #bbb; border-radius: 10px;
                 padding: 14px 18px; margin: 14px 0; }}
        pre {{ white-space: pre-wrap; font-family: sans-serif; }}
    </style>
</head>
<body>
    {body}
</body>
</html>"""


# 第 1 页：表单
@app.get("/", response_class=HTMLResponse)
def home():
    return page("天气小助手", """
    <h1>天气小助手</h1>
    <p>输入城市，我告诉你明天该注意什么。</p>
    <form action="/result" method="get">
        <input name="city" placeholder="比如：珠海">
        <input name="question" placeholder="天气怎么样？">
        <button>问！</button>
    </form>
    """)


# 第 2 页：查天气 + 问模型，把结果画成网页
@app.get("/result", response_class=HTMLResponse)
def result(city: str, question: str = ""):
    if not question:
        question = "明天出门要注意什么？"

    wt = get_weather(city)
    if not wt:
        return page("查不到", f"""
        <h1>查不到「{city}」</h1>
        <p>这个城市名可能写错了，<a href="/">回去换个试试</a>。</p>
        """)

    a = advise(wt, question)
    if not a:
        return page("出错了", """
        <h1>模型没答上来</h1>
        <p><a href="/">回去再试一次</a>。</p>
        """)

    return page(city, f"""
    <h1>{city} · 明天</h1>
    <div class="card"><b>天气数据</b><pre>{wt}</pre></div>
    <div class="card"><b>你问的：{question}</b><p>{a}</p></div>
    <p><a href="/">再问一个城市</a></p>
    <b>你问的：{question}</b>
    """)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
