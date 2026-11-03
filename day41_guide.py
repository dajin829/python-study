# day41_guide.py —— 共写版：一句一句来，每行都讲为什么。
# 规矩：我讲一行 → 你打一行 → 攒够一块就跑一次。
# 今天不默写、不脱稿，允许全程看 day39_page.py。
#
# 分五段：
#   第 1 段  五行 import + app = FastAPI()
#   第 2 段  page() 外壳函数
#   第 3 段  第 1 页 home()：画表单
#   第 4 段  第 2 页 result()：查天气、问模型、画结果
#   第 5 段  三道关卡：空问题 / 查不到 / 模型没答
from weather_ai import advise,get_weather
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
def page(title,body):
    return f"""<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <style>
        body {{ font-family: sans-serif; max-width: 460px; margin: 60px auto; }}
        input {{ padding: 8px; margin-right: 6px; }}
        button {{ padding: 8px 22px; }}
        .card {{ border: 1px solid #bbb; border-radius: 10px; padding: 14px 18px;margin:14px 0; }}
        pre {{ white-space: pre-wrap; font-family: sans-serif; }}
    </style>
</head>
<body>
    {body}
</body>
</html>"""
app=FastAPI()
@app.get("/",response_class=HTMLResponse)
def home():
        return page("天气小助手","""
<h1>天气小助手</h1>
<p1>输入城市，我告诉你明天应该该注意什么</p1>
<form action="/result" method="get">
<input name="city" placeholder="比如，厦门">
<input name="question" placeholder="天气怎么样？">
<button>问</button>
</form>
""")
@app.get("/result",response_class=HTMLResponse)
def result(city:str,question:str=""):
    if not question:
        question="明天出门要注意什么"
    wt=get_weather(city)
    a=advise(wt,question)
    return page(city,f"""
    <h1>{city}.明天</h1>
    <div class ="card"><b>天气数据</b><pre>{wt}</pre></div>
    <p><a href="/">再问一个城市</a></p>
    <div class="card"><b>你问的：{question}</b><p>{a}</p></div>
""")
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
