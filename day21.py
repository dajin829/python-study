import requests

r=requests.get("https://www.baidu.com")
print(r.status_code)
print(r.text)

m=requests.get("https://httpbin.org/get")
print(m.status_code)
print(m.text)