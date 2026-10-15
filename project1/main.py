import requests


def showmenu():
    """打印菜单，返回用户输入的选择。"""
    print("==每日天气小程序==")
    print("1.看天气")
    print("2.查历史")
    print("3.退出")
    return input("你的选择是？")


def search(city):
    """查一次天气：打印出来，并把结果整理成一段文字 return 出去；查不到返回 None。"""
    try:
        r = requests.get(f"https://wttr.in/{city}?format=j1", timeout=10)
    except Exception as e:
        print("网络出错了：", e)
        return None

    if r.status_code != 200:
        print("查不到城市")
        return None

    d = r.json()
    cc = d["current_condition"][0]
    info = (f"{city} 今日天气：\n"
            f"  温度 {cc['temp_C']}℃   湿度 {cc['humidity']}%\n"
            f"  天气 {cc['weatherDesc'][0]['value']}\n"
            f"  地点 {d['nearest_area'][0]['areaName'][0]['value']}\n")
    print(info)
    return info


def record(info):
    """把一段天气文字追加写进 weather.txt。只负责写文件，不再联网。"""
    with open("weather.txt", "a", encoding="utf-8") as f:
        f.write(info)
        f.write("\n")


def history():
    """打印 weather.txt 里存过的全部记录。文件不存在或内容为空时给出提示。"""
    try:
        with open("weather.txt", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("还没有任何记录，先去查一次天气吧")
        return

    if content.strip() == "":
        print("还没有任何记录")
        return

    print(content)


def main():
    while True:
        choice = showmenu()
        if choice == "1":
            city = input("选择你要查询的城市：")
            info = search(city)
            if info:            # 查到了才存；没查到（None）就不写
                record(info)
        elif choice == "2":
            history()
        elif choice == "3":
            print("好的，现在就退出")
            break
        else:
            print("看不懂")


if __name__ == "__main__":
    main()
