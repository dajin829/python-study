import requests
r=requests.get("https://wttr.in/厦门?format=j1", timeout=10)
print(r.status_code)
d=r.json()
cc=d["current_condition"][0]
print(cc["temp_C"])
print(cc["humidity"])
print(cc["weatherDesc"][0]["value"])         # 天气描述
print(d["nearest_area"][0]["areaName"][0]["value"])