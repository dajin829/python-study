contacts = [
    {"姓名": "张三", "电话": "13800000001"},
    {"姓名": "李四", "电话": "13800000002"},
    {"姓名": "王五", "电话": "13800000003"},
]
for c in contacts:
    print(c["姓名"],c["电话"])
name=input("请输入名字:")
found=False
for c in contacts:
    if c["姓名"]==name:
        print(f"{name}的电话是{c['电话']}")
        found=True
if found==False:
    print(f"没有找到{name}的电话")
