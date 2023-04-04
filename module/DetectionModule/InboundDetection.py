import re

# 对用户输入的消息进行过滤和校验
def validate_input(message_text):
    # 使用正则表达式过滤非法字符
    pattern = re.compile(r"[^\w\s]")
    filtered_text = re.sub(pattern, "", message_text)
    if len(filtered_text) < 1:
        raise ValueError("输入的消息不能为空！")
    elif len(filtered_text) > 1024:
        raise ValueError("输入的消息过长，请输入不超过1024个字符的消息！")
    return filtered_text

