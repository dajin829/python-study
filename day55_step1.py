# 第 55 天 · 第 1 步
from pptx import Presentation
p=Presentation("第6章 图.pptx")
print(len(p.slides))
s=p.slides[20]
print(len(s.shapes))
for sh in s.shapes:
    print(sh.has_text_frame)