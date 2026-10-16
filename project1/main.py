import requests


def showmenu():
    print("1.查天气")
    print("2.查历史")
    print("3.退出")
    return input("你的选择是：")

    """打印菜单，返回用户输入的选择。"""
    # 第 1 步：打印 4 行（标题 + 1.看天气 / 2.查历史 / 3.退出）
    # 第 2 步：return input("你的选择是？")


def search(city):
    
    try:
        r=requests.get(f"https://wttr.in/{city}?format=j1",timeout=10)
    except Exception as e:
        print("网络连接有问题:",e)
        return None
    if(r.status_code==200):
        d=r.json()
        cc=d["current_condition"][0]
        weather_cn = {"113": "晴", "116": "多云", "119": "阴", "122": "阴天","143": "薄雾", "149": "烟霾", "248": "雾", "200": "雷阵雨",}
        print(f"{city}的当日天气状态\n"
              f"温度{cc['temp_C']}度\n" 
              f"湿度{cc['humidity']}%\n"
              f"{weather_cn.get(cc['weatherCode'],'未知')}\n"
              f"{d['nearest_area'][0]['areaName'][0]['value']}\n")
        info=(f"{city}的当日天气状态\n"
              f"温度{cc['temp_C']}度\n"
              f"湿度{cc['humidity']}%\n"
              f"{weather_cn.get(cc['weatherCode'],'未知')}\n"
              f"最近气象观测地{d['nearest_area'][0]['areaName'][0]['value']}\n")
        return(info)

    elif(r.status_code!=200):
        print("查询不到该城市的天气状态")
        return None
    
    """查一次天气：打印出来，并把结果整理成一段文字 return 出去；查不到返回 None。"""
    # 第 1 步：requests.get(f"https://wttr.in/{city}?format=j1", timeout=10)
    #         整段包在 try/except 里；出错就 print 提示 + return None
    #         （注意：f 前缀别丢，丢了就会静默查成别的城市）
    # 第 2 步：if r.status_code != 200: print("查不到城市"); return None
    # 第 3 步：d = r.json();  cc = d["current_condition"][0]
    # 第 4 步：拼多行 f-string 赋值给 info
    #         用到的字段：cc['temp_C']、cc['humidity']、
    #                     cc['weatherDesc'][0]['value']、
    #                     d['nearest_area'][0]['areaName'][0]['value']
    #         （括号只在最后一行闭合，中间几行不写 ) ）
    # 第 5 步：print(info)，然后 return info



def record(info):
    """把一段天气文字追加写进 weather.txt。只负责写文件，不联网。"""
    # 用 "a" 模式打开 weather.txt（encoding="utf-8"），
    # 写入 info，再写一个 "\n"
    with open("weather.txt","a",encoding="utf-8") as f:
        f.write(info)
        f.write("\n")


def history():
    """打印 weather.txt 里存过的全部记录。文件不存在或内容为空时给出提示。"""
    # 第 1 步：try 读文件；except FileNotFoundError → print 提示 + return
    # 第 2 步：如果内容是空白（content.strip() == ""）也要提示 + return
    # 第 3 步：print 出来
    try:
        with open("weather.txt","r",encoding="utf-8") as f:
            content=f.read()
    except FileNotFoundError:
        print("还没查过天气，去查一次吧")
        return
    if content.strip()=="":
        print("这是个空文件")
        return
    print(content)

def main():
    # 第 1 步：while True，用 showmenu() 拿 choice
    # 第 2 步：choice == "1" → input 要城市 → info = search(city)
    #          → if info: 才 record(info)   （None 说明没查到，不能存）
    # 第 3 步：choice == "2" → history()
    # 第 4 步：choice == "3" → 打印再见 + break
    # 第 5 步：else → print("看不懂")
    while True:
        choice=showmenu()
        if(choice=="1"):
            city=input("请输入你想查询的城市：")
            info=search(city)
            if(info):
                record(info)
        elif(choice=="2"):
            history()
        elif(choice=="3"):
            print("退出")
            break
        else:
            print("看不懂")
            


if __name__ == "__main__":
    main()
