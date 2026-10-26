# day38_demo.py —— 教材，不是作业。
# 先跑起来，在浏览器里点一遍；读懂了，再自己写 day38_page.py。
# 一共 2 个接口、1 个新东西（HTMLResponse），其余全是你会的。

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()


# 第 1 页：一张有输入框的表单
@app.get("/", response_class=HTMLResponse)
def home():
    return """<!doctype html>
<html>
<head><meta charset="utf-8"><title>打招呼</title></head>
<body>
    <h1>打个招呼</h1>
    <form action="/hi" method="get">
        <input name="name" placeholder="你的名字">
        <button>发送</button>
    </form>
</body>
</html>"""


# 第 2 页：把收到的名字写进网页里
@app.get("/hi", response_class=HTMLResponse)
def hi(name: str):
    return f"""<!doctype html>
<html>
<head><meta charset="utf-8"><title>你好</title></head>
<body>
    <h1>你好，{name}</h1>
    <p>你刚才在输入框里打的东西，跑到这里来了。</p>
    <a href="/">再来一次</a>
</body>
</html>"""


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
