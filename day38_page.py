from fastapi.responses import HTMLResponse
from fastapi import FastAPI
import uvicorn
app=FastAPI()
@app.get("/",response_class=HTMLResponse)##response_class=HTMLResponse告诉它这次return的是网页 不是数据
def home():
    return """<!doctype html>
<html><body>
        <form action="/result" method="get">
            <input name="city" placeholder="大金">
            <button>发送</button>
    </form>
</body></html>"""
@app.get("/result",response_class=HTMLResponse)
def result(city:str,question:str):
    return f"<h1>"
