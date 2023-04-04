from fastapi import Request
from public.app_path import app

# get路由
@app.get('/GET')
async def get_roule(request: Request):  # put application's code here

    print('你好，世界！！！')
    return '你好，世界！！！'