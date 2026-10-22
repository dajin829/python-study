"""第 34 天测试工具（老师写的，随便改）：测你自己的接口

用法：
  终端 1：先启动你的服务  →  python day34_my.py（卡住不动 = 在值班，正常）
  终端 2：跑这个文件      →  python day34_test.py
"""

import requests

BASE = "http://127.0.0.1:8000"      # 前半截：哪台电脑哪个门（端口改了这里跟着改）

# 后半截：要访问哪一页。往这个列表里加你想试的路径。
paths = [
    "/ping",                # 接口 1：应该 200 + {"status":"ok"}
    "/chat?text=你好",       # 接口 2：应该 200 + {"reply": 模型的回答}
    "/chat?text=",           # 空输入：应该 200 + {"error":"text不能为空"}
    "/",                     # 没登记过：应该 404（亲眼看看 404）
]

for path in paths:
    r = requests.get(BASE + path, timeout=10)
    print(f"{BASE + path}")
    print(f"   状态码 {r.status_code}   返回 {r.text[:100]}")
    print()
