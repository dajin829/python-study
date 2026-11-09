import json

data = {"事件": ["看书", "打球"], "地点": ["图书馆", "球场"]}

with open("test.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("写完了")
