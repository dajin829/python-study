# day42_demo.py —— 让模型吐出"程序能用的东西"
#
# 到今天为止：模型返回的都是一句话（"带伞，防晒。"），只能印给人看。
# 今天：让它返回 JSON，程序才能拿去判断、存表、做决定。
#
# 只用三个老东西：requests.post（第 29 天）、字典取值。
# 新东西只有两个：json.loads、response_format。
import json
import requests
from config import API_KEY

API = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

# 一段乱七八糟的通知（真实场景：群里发的消息）
NOTICE = "这周三下午两点在学院楼302开班会，记得带学生证和笔，别迟到。"

# prompt 的两件事：① 说清"只返回 JSON" ② 给它一个空模板照抄
PROMPT = (
    "从下面这段通知里提取信息，返回 JSON：\n"
    '{"时间": "", "地点": "", "要带的东西": []}\n'
    f"通知：{NOTICE}"
)


def ask(prompt, force_json=False):
    """把 prompt 扔给模型，原样返回它说的话（一个字符串）。

    force_json=True 时多带一个开关，逼它只回纯 JSON。
    """
    headers = {"Authorization": "Bearer " + API_KEY}
    data = {"model": "glm-4-flash",
            "messages": [{"role": "user", "content": prompt}]}
    if force_json:
        data["response_format"] = {"type": "json_object"}   # ← 今天的新东西 1
    r = requests.post(API, headers=headers, json=data, timeout=60)
    d = r.json()
    if "error" in d:
        print(r.text)
        return None
    return d["choices"][0]["message"]["content"]


# ========== 第一回合：不带开关，直接解析 ==========
print("========== 第一回合：不带开关 ==========")
raw = ask(PROMPT)
print("模型原话：")
print(raw)
print("类型：", type(raw))

try:
    d = json.loads(raw)          # ← 今天的新东西 2：字符串 → 字典
    print("解析成功：", d)
except json.JSONDecodeError as e:
    print("解析失败：", e)
    print("原因：它裹了一层 ```json 围栏。嘴上答应了，手上没照做。")


# ========== 第二回合：带开关，再解析 ==========
print()
print("========== 第二回合：带开关 ==========")
raw = ask(PROMPT, force_json=True)
print("模型原话：")
print(raw)

d = json.loads(raw)
print("类型：", type(d))
print("时间：", d["时间"])
print("地点：", d["地点"])
print("要带：", d["要带的东西"])
