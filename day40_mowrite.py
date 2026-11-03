# day40_mowrite.py —— 默写日。这个文件里没有一行代码，全部由你写。

# 任务：凭记忆写出两页的天气网页，功能跟 day39_page.py 一样。
# 规矩：
#   - 不打开 day39_page.py，不看昨天的记忆卡；
#   - 卡住了别问"怎么写"，说"我卡在第几块"，我按阶梯提示；
#   - HTML 标签想不起具体拼写可以问，但要先自己试着回忆。
#
# 要写的两页：
#   第 1 页  @app.get("/")          —— 表单：city + question 两个输入框，提交到 /result
#   第 2 页  @app.get("/result")    —— 查天气 + 问模型，结果画成网页
#
# 第 2 页内部的三道关卡（每道失败都要返回"看得懂的页面"，不能裸崩）：
#   1. question 空着 → 换成默认问题
#   2. get_weather 返回 None → "查不到这个城市"页
#   3. advise 返回 None → "模型没答上来"页
#
# 外壳：一个公共函数，收 title 和 body，包上 <!doctype html> ... <style> ... </style> 的固定结构。
# 验收（自己跑完挨个点）：
#   http://127.0.0.1:8000/
#   http://127.0.0.1:8000/result?city=厦门&question=要不要带伞
#   http://127.0.0.1:8000/result?city=asdasdzxc
#   http://127.0.0.1:8000/result?city=厦门          ← 不带 question，看默认值生效没
#
# 写完喊"检查"。
from fastapi import FastAPI
import uvicorn 
from weather_ai import advise,get_weather
from fastapi.responses import HTMLResponse
app=FastAPI()
@app.get("/",response_class=HTMLResponse)
def home():
   