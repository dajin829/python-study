while True:
    try:
        s=int(input("输入多少秒:"))
    except ValueError:
        print("请输入整数")
        continue
    if s<0:
        print("请输入正整数")
        continue
    else:
        break
print(f"{s//3600}小时{(s%3600)//60}分钟{s%60}秒")
