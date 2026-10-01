todo=[]
while True:
    items=input("请输入你的待办事项")
    if items=="done":
        break
    todo.append(items)
print("这是你的待办事项")
for i in range(len(todo)):
    print(i+1,todo[i])
    if(todo[0]=="done"):
        print("你没有待办事项")
    else:
        print(f"一共{len(todo)}件事")
