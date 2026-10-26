"""第 37 天 · 第 2 步用：亲手寄一个包裹给 /echo，看它原样吐回来"""
import requests

r = requests.post("http://127.0.0.1:8000/echo", json={"name": "大金", "msg": "你好"})
print("状态码：", r.status_code)
print("它吐回来的：", r.text)
