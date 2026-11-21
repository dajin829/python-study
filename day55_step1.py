# 第 55 天 · 第 1 步
from pptx import Presentation
p=Presentation("第6章 图.pptx")
print(len(p.slides))
s=p.slides[20]
print(len(s.shapes))
for sh in s.shapes:
    print(sh.has_text_frame)##判断是否有文字
text=[]
for sh in s.shapes:
    if sh.has_text_frame:
        text.append(sh.text_frame.text)##把那行文字添加进来
for t in text:
    print(repr(t))
ok=[]
for t in text:
    if t.strip():
        ok.append(t)
print("\n".join(ok))##join(ok)把列表里的黏起来一起输出