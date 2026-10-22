"""第 33 天：给对话一个身份 + 别让它越聊越贵

基于 day32_chat.py，只加两样东西：

  1. system 提示词 —— 给模型设定身份和规矩。一次设定，后面每一轮都生效。
  2. 上下文裁剪 —— history 越聊越长（token 就越花越多），超过上限就砍掉最老的。

ask() 直接从 day32_chat.py 抄过来，一个字都不用改。
"""

import requests
from config import API_KEY

URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

# ── 第 1 步：写你的 system 提示词 ──────────────────────────
# 想让它扮演谁、用什么语气、有什么规矩，都写这里。
# 下面这段只是示例，换成你自己想要的（比如"你是我的 Python 助教"）。
SYSTEM_PROMPT = "你是小金，你是我的助手，你回答要尽可能简短"

MAX_TURNS = 20      # history 最多留多少条


def ask(history):
    """把整段对话交给模型，return 它这一轮的回答。（照抄 day32，不用改）"""
    headers = {"Authorization": "Bearer " + API_KEY}
    data = {"model": "glm-4-flash", "messages": history}
    try:
        r = requests.post(URL, headers=headers, json=data, timeout=60)
    except Exception as e:
        print(f"出现了错误{e}\n")
        return None
    if r.status_code != 200:
        print(r.text, r.status_code)
        return None
    d = r.json()
    if "error" in d:
        print(r.text, r.status_code)
        return None
    return d["choices"][0]["message"]["content"]


def trim(history):
    """history 太长就砍掉最老的几条，但第 0 条（system）必须保住。"""
    # 判断：len(history) 有没有超过 MAX_TURNS
    #   没超过 → 原样 return history
    #   超过了 → 保留第 0 条 + 最后 (MAX_TURNS - 1) 条
    #
    # 提示：拼两个列表用 + 就行
    #     [history[0]] + history[-(MAX_TURNS - 1):]
    #
    # ⚠ 不能直接写 history[-MAX_TURNS:]，那样第 0 条 system 会被切掉
    if len(history)<=   MAX_TURNS:
        return history
    else:
        return [history[0]]+history[-(MAX_TURNS-1):]
        


def main():
    # TODO 1：history 不再是空列表，第一项必须是 system（照 SYSTEM_PROMPT 造一个字典）
    history = []
    history.append({"content":SYSTEM_PROMPT,"role":"system"})

    while True:
        question = input("你：")
        if question.strip() == "":
            continue
        if question.lower() == "q":
            break
        history.append({"role": "user", "content": question})
        history=trim(history)

        # TODO 2：发请求之前，先让 trim 裁一次，把结果接回 history
        a = ask(history)
        if a:
            print("AI：", a)
            history.append({"role": "assistant", "content": a})

        # TODO 3：每轮打印一下 history 有几条，亲眼看它长、看它被裁
        print(f"[history {len(history)} 条]")


if __name__ == "__main__":
    main()
