def showmenu():
    print("==每日天气小程序==")
    print("1.看天气")
    print("2.查历史")
    print("3.退出")
    return input("你的选择是？")

def search(city):
    import requests
    r=requests.get(f"https://wttr.in/{city}?format=j1", timeout=10)
    if(r.status_code==200):
        d=r.json()
        cc=d["current_condition"][0]
        print(cc["temp_C"])
        print(cc["humidity"])
        print(cc["weatherDesc"][0]["value"])
        print(d["nearest_area"][0]["areaName"][0]["value"])
    else:
        print("查不到城市")
def record():
    pass
def history():
    pass

def main():
    
    while True:
        choice=showmenu()
        if(choice=="1"):
            city=input("选择你要查询的城市")
            search(city)
        elif(choice=="2"):
            history()
        elif(choice=="3"):
            print("好的，现在就退出")
            break
        else:
            print("看不懂")
if __name__ == "__main__":        # 入口保护
    main()