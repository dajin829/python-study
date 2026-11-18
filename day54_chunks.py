"""RAG 第 1 块：把 PPT 拆成一段一段，存成文件。

跑完会生成 chunks.json，里面是一个列表，每一项长这样：
    {"页": 3, "文字": "图结构的应用 ..."}

为什么要拆？三个原因：
  1. 整本 PPT 塞不进 prompt（202 页，几十万字，模型一次只吃几千字）
  2. 就算塞得进，也太贵——每问一句都要按全部内容算钱
  3. 更重要的是"找不准"：把一整章发给模型，它回答时容易抓错地方

拆成小段之后，问问题时只用"最像的那几段"，又快又准又便宜。
"""

from pptx import Presentation
import json

p = Presentation("第6章 图.pptx")

chunks = []
for i, slide in enumerate(p.slides, start=1):
    texts = []
    for shape in slide.shapes:
        if shape.has_text_frame:
            t = shape.text_frame.text.strip()
            if t:
                texts.append(t)
    page_text = "\n".join(texts).strip()
    if page_text:
        chunks.append({"页": i, "文字": page_text})

print("共", len(chunks), "段")
print("最长一段", max(len(c["文字"]) for c in chunks), "字")
print("最短一段", min(len(c["文字"]) for c in chunks), "字")

with open("chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)

print("存好了，看 chunks.json")
