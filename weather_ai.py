import requests
from config import API_KEY

# 项目二：天气 + 大模型 = 出行建议助手
# 你说「明天要不要带伞」，它自己去查真天气，再让大模型给建议。
#
# 三个函数的规矩（今天最重要的一条）：
#   get_weather  → 只查数据、只 return，一行 print 都不许有
#   advise       → 只负责调模型，不知道天气
#   main         → 只负责串起来和显示


def get_weather(city, day=1):
    """查某城市某一天的天气，整理成一小段中文 return 出去。查不到 / 网络错都 return None。

    day：0 = 今天，1 = 明天，2 = 后天（对应 d["weather"] 这个列表的下标）
    """
    # 第 1 步：照 project1/main.py 里 search() 的结构抄一遍
    #         requests.get(f"https://wttr.in/{city}?format=j1", timeout=10)
    #         整段包在 try/except，出错 return None
    #         状态码不是 200 → return None（注意：这里不许 print）
    # 第 2 步：w = d["weather"][day]      ← 只要这一天，别把整份 JSON 往下传
    # 第 3 步：从 w 里取这 5 样（字段名见任务卡）：
    #         date / maxtempC / mintempC / hourly[4]["chanceofrain"] / uvIndex
    # 第 4 步：拼成多行 f-string（括号只在最后一行闭合），return 出去
    try:
        r=requests.get(f"https://wttr.in/{city}?format=j1",timeout=10)
    except Exception as e:
        print(f"出现了问题{e}")
        return None
    if(r.status_code==200):
        d=r.json()
        w=d["weather"][day]
        weather_text=(f"城市：{city}\n"
                      f"日期：{w['date']}\n"
                      f"最高温：{w['maxtempC']}度\n"
                      f"最低温：{w['mintempC']}度\n"
                      f"中午降雨概率：{w['hourly'][4]['chanceofrain']}%\n"
                      f"紫外线指数：{w['uvIndex']}\n")
        return weather_text
    else:
        return None

def advise(weather_text, question):
    """把天气数据 + 用户的问题一起交给大模型，return 它的建议。失败 return None。"""
    # 第 1 步：拼 prompt（模板见任务卡，重点是那句「只根据数据回答」）
    # 第 2 步：照 day29.py 的 ask() 抄 —— headers / json / post / timeout
    # 第 3 步：r.json() 之后先查 if "error" in d
    # 第 4 步：return d["choices"][0]["message"]["content"]
    headers={"Authorization":"Bearer "+ API_KEY}
    prompt=("你是一个天气助手\n"
            "请根据我给你的天气情况来回答我给你的问题\n"
            "不要自己编造回答,不会就说不知道，根据我给你的数据来回答\n"
            f"天气数据：{weather_text}\n"
            f"问题：{question}\n"
            "请用两句以内的中文回答\n")# 只需改一个词：把 content 的值从 question 换成 prompt。​ 所有天气数据还有问题都装在这个 prompt 里。
    data={"model":"glm-4-flash","messages":[{"content":prompt,"role":"user"}]}
    try:
        r=requests.post(headers=headers,json=data,url="https://open.bigmodel.cn/api/paas/v4/chat/completions",timeout=60)
    except Exception as e:
        print(f"出现了问题{e}\n")
        return None
    d=r.json()
    if "error" in d:
        print(r.text)
        print("有错误\n")

        return None
    if(r.status_code==200):
        advise=d["choices"][0]["message"]["content"]
        return advise




def main():
    # 第 1 步：问城市、问问题（两个 input）
    # 第 2 步：wt = get_weather(city)
    #          if not wt: 打印一句提示，然后 return
    # 第 3 步：print(wt)      ← 显示归 main 管，让用户看到喂给模型的到底是什么
    # 第 4 步：a = advise(wt, question)
    #          if a: print(a)   ← 这个 if 别忘了，第 27/29 天都栽过
    city=input("请输入你要查询的城市")
    wt=get_weather(city)
    if not wt:
        print("查询不到这个城市的天气")
        return
    print(wt)
    question=input("请提出你想问的问题")
    if question.lower() == "no":
        return None
    a=advise(wt,question)
    if a:
        print(a)

if __name__ == "__main__":
    main()
