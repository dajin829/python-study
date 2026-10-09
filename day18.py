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
with open("todo.txt","r",encoding="utf-8") as f:
    content=f.read()
print(content)#① todo 是列表（你叫数组，Python 里叫 list，第 10 天学的）​它真的装了 3 个独立的格子，每格一件完整的东西。todo[0] 取出 "吃饭"，todo[2] 取出 "健身"。件数是 3。② content 只装了 1 个字符串，不是"很多东西"​f.read() 把整个文件读成一整条文本。len(content)=9 说明它是 9 个字符（吃、饭、\n、买、菜、\n、健、身、\n）。所以它不是装了 3 件，是装了 1 条长绳子。content[0] 只能拿到 "吃" 这一个字，拿不到 "吃饭" 这一项。③ 那为什么打印出来也是三行？因为那条绳子里面藏了 \n（看"真面目"那行，\n 就明明白白在里面）。print 一碰到 \n 就换行，所以显示成三行——这是视觉上的错觉，不是真的分成了三件。
