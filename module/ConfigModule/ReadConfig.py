import openai
import toml
import os

config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Config', 'Server.toml'))
config = toml.load(config_path)
# 读取配置文件
#with open("../../Config/Server.toml", "r", encoding='utf-8') as f:
#    config = toml.load(f)

web_host = config['servers']['web_host']
web_port = config['servers']['web_port']
chatgpt_user = config['servers']['chatgpt_user']
text_model = config['servers']['text_model']
code_model = config['servers']['code_model']
Api_key = config['servers']['Api_key']
Authentication_Status = config['servers']['Authentication_Status']