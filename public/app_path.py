from starlette.responses import RedirectResponse
from fastapi import FastAPI

app = FastAPI()

from module.RequestModule.ReceiveGetRequest import get_roule
from module.RequestModule.ReceivePostRequest import chatgpt

# 将任意路径的请求定位到get路由中
@app.get('/{path:path}')
def all(path: str):
    url = app.url_path_for('get_roule')
    return RedirectResponse(url=url)

# 将任意路径的请求定位到post路由中
@app.post('/{path:path}')
def all(path: str):
    url = app.url_path_for('chatgpt')
    return RedirectResponse(url=url)