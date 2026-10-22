"""第 32 天：多轮对话 —— 让模型记住上文。

跟 day29.py 唯一的区别，就在函数的参数上：

    day29:  ask(question)   每次只发一句话  → 模型没有上文，每次从零开始
    今天:   ask(history)    每次发整段对话  → 模型能看到前面说过什么

其余部分（headers / post / json / error 检查 / 取值）一个字都不用改。
"""

import requests
from config import API_KEY

URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"


def ask(history):
    """把整段对话交给模型，return 它这一轮的回答。

    参数 history 是一个列表，里面每条都是这种字典：
        {"role": "user",      "content": "我说的话"}
        {"role": "assistant", "content": "它上次的回答"}
    """
    # 第 1 步：headers（照 day29 抄，注意 Bearer 后面的空格在引号里面）
    headers={"Authorization":"Bearer "+API_KEY}
    data={"model":"glm-4-flash","messages":history}
    try:
        r=requests.post(headers=headers,json=data,url="https://open.bigmodel.cn/api/paas/v4/chat/completions",timeout=60)
    except Exception as e:
        print(f"出现了错误{e}\n")
        return None
    if(r.status_code!=200):
        print(r.text,r.status_code)#r.text里有错误的原因，不能用and，会把最后一个值给吞掉
        return None
    d=r.json()
    if "error" in d:
        print(r.text,r.status_code)
        return None
    
    return d["choices"][0]["message"]["content"]


    # 第 2 步：data
    #   {"model": "glm-4-flash", "messages": history}
    #   ⚠ messages 的值就是 history 本身，不要再包一层 [] 或 {}
    

    # 第 3 步：requests.post(URL, headers=..., json=..., timeout=60)
    
    # 第 4 步：d = r.json()，然后 if "error" in d: print(r.text) + return None
    

    # 第 5 步：return d["choices"][0]["message"]["content"]
    

def main():
    history = []          # 空的对话列表，所有内容都往这里堆

    while True:
        # 第 1 步：问一句，提示语写"（输入 q 退出）"
        question=input("请输入你的问题")
        if(question.strip()==""):
            print("你没输入\n")
            continue
        if(question.lower()=="q"):
            print("退出程序\n")
            break
        else:
            history.append({"content":question,"role":"user"})
        a=ask(history)
        if a:
            print(a)
            history.append({"content":a,"role":"assistant"})#要把每一次回答也给放进history，不然大模型会忘；history 是列表，append 加进去的是一整个新的字典，不是键。键是字典里的事，跟列表没关系
        # 第 2 步：空输入 → continue；输入 q（不分大小写）→ break
        

        # 第 3 步：把这句话装成字典追加进 history
        #   history.append({"role": "user", "content": question})
        

        # 第 4 步：a = ask(history)
        

        # 第 5 步：if a: 打印出来，并把它的回答也追加进 history
        #   history.append({"role": "assistant", "content": a})
        #   ⚠ 这一条最容易漏。不存它的回答，下一轮它不知道"我上一句说了什么"
        


if __name__ == "__main__":
    main()
