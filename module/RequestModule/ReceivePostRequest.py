from module.DetectionModule.InboundDetection import validate_input
from module.DetectionModule.MessageDetection import detect_code
from module.ConfigModule.ReadConfig import Authentication_Status
from module.ConfigModule.ReadConfig import chatgpt_user
from module.ConfigModule.ReadConfig import text_model
from module.ConfigModule.ReadConfig import code_model
from module.ConfigModule.ReadConfig import Api_key
from urllib.parse import urlparse
from public.app_path import app
from fastapi import Request
import logging
import openai
import json
import time

openai.api_key = Api_key

# post路由
@app.post('/POST/GPTAPI')
async def chatgpt(request: Request):  # put application's code here
    try:

        # 从请求体中获取JSON对象
        json_data = await request.json()

        # 从JSON对象中获客户名称
        customer_name = json_data.get('Customer_name', '')

        # 从JSON对象中获取认证码
        authentication_code = json_data.get('Authentication_Code', '')

        # 从JSON对象中获取请求类型
        tab_type = json_data.get('tab_type', '')

        # 从JSON对象中获取消息类型
        message_type = json_data.get('message_type', '')

        # 从JSON对象中获取消息
        message_text = json_data.get('message_text', '')

        # 对消息进行过滤和校验
        filtered_message = validate_input(message_text)

        # 从JSON对象中获取发送者
        sender = json_data.get('sender', '')

        # 配置 logging
        logging.basicConfig(filename='chatbot.log', encoding='utf-8', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

        # 添加日志记录
        logging.info(f"tab_type: {tab_type}")

        # 添加日志记录
        logging.info(f"User input: {filtered_message}")

        if Authentication_Status == "false":

            if tab_type == "text_tab":

                if message_type:

                    if message_text:

                        # 生成文字
                        completion = openai.ChatCompletion.create(
                            model=text_model,
                            messages=[
                                {"role": "system", "content": chatgpt_user},
                                {"role": "user", "content": filtered_message}
                            ],
                            temperature=0.9,
                            max_tokens=1024,
                            top_p=1.0,
                            n=1,
                            frequency_penalty=0.5,
                            presence_penalty=0.0,
                        )
                        output_text = completion.choices[0].message.content
                        print(output_text)

                        # 添加日志记录
                        logging.info(f"output_text: {output_text}")
                        return {'code': 200, 'type': 'Code', 'message': output_text}

                    else:
                        print("请传递文本消息")
                        return {'code': 504, 'type': 'error', 'message': "请传递文本消息"}

                else:
                    print("消息类型不能为空")
                    return {'code': 504, 'type': 'error', 'message': "消息类型不能为空"}


            elif tab_type == "code_tab":

                if message_type:

                    if message_text:

                        # 生成代码
                        completion = openai.ChatCompletion.create(
                            model=text_model,
                            messages=[
                                {"role": "system", "content": chatgpt_user},
                                {"role": "user", "content": filtered_message}
                            ],
                            temperature=0.9,
                            max_tokens=1024,
                            top_p=1.0,
                            n=1,
                            frequency_penalty=0.5,
                            presence_penalty=0.0,
                        )
                        # 获取代码
                        try:
                            output_code = completion.choices[0].message.content
                        except (KeyError, IndexError):
                            print("无法获取代码")
                            return {'code': 504, 'type': 'error', 'message': "无法获取代码"}

                        # 判断是否为代码
                        lang, code = detect_code(output_code)
                        if lang:

                            # 如果是代码，则返回代码类型和代码内容
                            time.sleep(1)  # 添加 1 秒的延迟
                            print(output_code)
                            # 添加日志记录
                            logging.info(f"output_code: {output_code}")
                            return {'code': 200, 'type': 'code', 'lang': lang, 'message': code}

                        else:

                            # 如果不是代码，则返回普通文本内容
                            time.sleep(1)  # 添加 1 秒的延迟
                            print(output_code)
                            # 添加日志记录
                            logging.info(f"output_code: {output_code}")
                            return {'code': 200, 'type': 'text', 'message': output_code}


                    else:
                        print("请传递文本消息")
                        return {'code': 504, 'type': 'error', 'message': "请传递文本消息"}

                else:
                    print("消息类型不能为空")
                    return {'code': 504, 'type': 'error', 'message': "消息类型不能为空"}


            elif tab_type == "image_tab":

                if message_type:

                    if message_text:

                        # 生成图像
                        response = openai.Image.create(
                            prompt=filtered_message,
                            n=1,
                            size="1024x1024"
                        )
                        # 获取图片 URL
                        try:
                            image_url = response['data'][0]['url'].strip()
                        except (KeyError, IndexError):
                            print("无法获取图片 URL")
                            return {'code': 504, 'type': 'error', 'message': "无法获取图片 URL"}

                        # 检查图片 URL 是否安全
                        parsed_url = urlparse(image_url)
                        if parsed_url.scheme != 'https' or parsed_url.hostname is None:

                            return {'code': 504, 'type': 'error', 'message': "无效的图片 URL"}

                        else:
                            time.sleep(1)  # 添加 1 秒的延迟
                            print(image_url)
                            # 下载图片
                            # image_content = requests.get(image_url).content
                            # 保存图像到文件
                            # with open('image.jpg', 'wb') as f:
                            # f.write(image_content)
                            # 将图片转换成Base64编码
                            # img_str = base64.b64encode(image_content).decode('utf-8')
                            # print("你将图片转换成的Base64编码是：",img_str)
                            # 添加日志记录
                            logging.info(f"image_url: {image_url}")
                            return {'code': 200, 'type': 'image', 'message': image_url}

                    else:
                        print("请传递文本消息")
                        return {'code': 504, 'type': 'error', 'message': "请传递文本消息"}

                else:
                    print("消息类型不能为空")
                    return {'code': 504, 'type': 'error', 'message': "消息类型不能为空"}


            elif tab_type == "video_tab":

                print("tab_type:" + tab_type)


            elif not tab_type:

                print("发起请求时请求类型不能为空！！！")
                return {'code': 504, 'type': 'error', 'message': "发起请求时请求类型不能为空！！！"}


            else:

                print("目前还不支持" + tab_type + "请求类型")
                return {'code': 504, 'type': 'error', 'message': "目前还不支持" + tab_type + "请求类型"}


        elif Authentication_Status == "True":

            if customer_name == customer_name and authentication_code == authentication_code:

                print("认证成功：" + customer_name)

            else:

                print("认证失败")
                return {'code': 504, 'type': 'error', 'message': "认证失败"}

        else:

            print("不支持的认证状态：" + Authentication_Status)



    except Exception as e:
        # 返回错误信息
        return {'error': "请携带参数请求"+str(e)}