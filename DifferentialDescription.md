## 在`v23.05.08.0007`(含)之前的版本中服务器依赖与`uvicorn`,
### 安装uvicorn(v23.05.08.0007(含)版本之前需要)
    pip3 install uvicorn
##### Uvicorn是一个基于Python的ASGI（异步服务器网关接口）Web服务器，此服务器代码简洁，性能好非常适合初学`python`伙伴们练手，有兴趣的可以看我的总结的[python中几个服务器]()
### 然后用此命令启动项目(http2服务端必须申请证书)
    hypercorn --keyfile key.pem --certfile cert.pem app_name:app --bind 0.0.0.0:8000 --workers 4 --access-logfile /var/log/hypercorn.log --error-logfile /var/log/hypercorn.log --daemon
