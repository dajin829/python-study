me = {"姓名": "大金", "年龄": 20,"专业":"人工智能","学校":"华侨大学"}#字典
print(me["专业"])
me["年龄"]=21
print(me["年龄"])
me["身高"]=186
print(me)
del me["年龄"]
print(me)
print(me.get("年龄","没记录年龄"))