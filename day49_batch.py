import json
from day45_func import clean

# 第 1 块 · 读文件
#   用 with open 打开 notes.txt（模式 "r"，encoding="utf-8"）
#   用 .readlines() 拿到「每一行组成的列表」，存进变量 lines
with open("notes.txt","r",encoding="utf-8") as f:
    lines=f.readlines()


# 第 2 块 · 准备一个空列表，用来装每一行解析出来的字典
kong=[]

# 第 3 块 · 循环每一行（for line in lines:）
#   ① 先 line.strip() 去掉末尾那个换行
#   ② 空行跳过（用 continue）
#   ③ 调用 clean()，把返回的字典接住
for line in lines:
    line=line.strip()
    if not line:
        continue
    d=clean(line)

# 第 4 块 · 把接住的字典 append 进第 2 块那个列表
    kong.append(d)

# 第 5 块 · 把列表存成 batch.json
#   用 json.dump(列表, f, ensure_ascii=False, indent=2)
#   存完打一句 print，让自己知道成了
with open("batch.json","w",encoding="utf-8") as f:
    json.dump(kong,f,ensure_ascii=False,indent=2)
