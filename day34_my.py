from fastapi import FastAPI
import uvicorn
app=FastAPI()##@ 是固定语法，背下来就行。​ 它的意思是：“下面紧贴着的那个 def，归我管”
@app.get("/")
def home():
    return({"hitokoto":"慢慢来，比较快","from":"大金"})
if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)##你在 uvicorn.run(app, host="127.0.0.1", port=8000) 里写的 host 和 port 就是它。浏览器先按这一截找到“你这台电脑上、守着 8000 端口、正在值班的那个程序”——也就是你的 uvicorn。后半截 /ping —— 找到程序之后，问它要哪一页。这时才轮到 FastAPI