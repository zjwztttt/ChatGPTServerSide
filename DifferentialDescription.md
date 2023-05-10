## 在`v23.05.08.0007`(含)之前的版本中服务器依赖与`uvicorn`,
### 安装uvicorn
    pip3 install uvicorn
##### Uvicorn是一个基于Python的ASGI（异步服务器网关接口）Web服务器，此服务器代码简洁，性能好非常适合初学`python`伙伴们练手，有兴趣的可以看我写的[python中几个服务器的示例代码](https://github.com/zjwztttt/CompleteTutorial/blob/main/python%E7%9A%84%E5%87%A0%E7%A7%8D%E6%9C%8D%E5%8A%A1%E5%99%A8.md)
### 然后用此命令启动项目(http2服务端必须申请证书)
    hypercorn --keyfile key.pem --certfile cert.pem app_name:app --bind 0.0.0.0:8000 --workers 4 --access-logfile /var/log/hypercorn.log --error-logfile /var/log/hypercorn.log --daemon
