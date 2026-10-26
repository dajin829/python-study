"""第 37 天 · 测试工具：给你的 POST 接口寄包裹

用法：先启动你的服务（python day37_weather_api.py），再在第二个终端跑：
    python day37_test.py
"""
import requests

BASE = "http://127.0.0.1:8000"

cases = [
    ("正常：city + question", {"city": "厦门", "question": "要不要带伞"}),
    ("只有 city（question 用默认）", {"city": "厦门"}),
    ("空 city", {"city": ""}),
    ("乱码城市", {"city": "asdasdzxc"}),
    ("空包裹", {}),
]

for name, payload in cases:
    r = requests.post(BASE + "/weather", json=payload, timeout=120)
    print(f"{name}   状态码 {r.status_code}")
    print(f"   {r.text[:200]}")
    print()
