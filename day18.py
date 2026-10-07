import random
print(random.randint(1,6))
import math
print(math.sqrt(16))
print(random.choice(["石头","剪刀","布"]))

with open("note.txt","w",encoding="utf-8") as f:
    f.write("今天学完了第十八天\n")
    f.write("python能存文件了\n")
print("存完了")

with open("note.txt","r",encoding="utf-8")as f:
          content=f.read()
print(content)
todo=["吃饭","买菜","健身"]
with open("todo.txt","w",encoding="utf-8")as f:
       for i in range(len(todo)):
              f.write(todo[i]+"\n")