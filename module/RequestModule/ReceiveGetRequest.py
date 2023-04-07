from fastapi import Request
from public.app_path import app
import json

# get路由
@app.get('/GET')
async def get_roule(request: Request):  # put application's code here
    try:

        print('你好，世界！！！')
        return {'code': 200, 'type':"text", 'message': '请使用post发起请求'}

    except Exception as e:
        # 返回错误信息
        return {'error': '请携带请求数据发送请求'+str(e)}