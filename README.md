## ChatGPTServerSide
##### ChatGPTServerSide：故名思意，一个基于ChatGPT API运行的后端程序，请注意：它仅只是一个服务端，它对外开放接口，不包含前端界面
#### 小提示：
##### 在生产环境部署中如果碰到如以下错误提示,均代表找不到对应的python依赖包
`ModuleNotFoundError: No module named '依赖包名'`
##### 大多数依赖包都可以使用以下命令安装
    pip3 install 包名 
## 准备工作：
#### 1.一台国际化的云服务器
#### 2.Finalshell远程链接工具（主要用来远程云服务器）
## 搭建环境(本教程基于Debian11系统，其他系统有些操作命令可能不受支持，请自行百度解决办法！)
### 更新系统
### 安装Python3
#### 安装python的方法有很多，咱这里只使用最简单的一种，有些云服务器不支持请自行百度另外的方法！
##### Debian
    apt install -y python3
### 安装pip3
##### Debian
    apt install -y python3-pip
### 安装uvicorn
    pip3 install uvicorn
##### Uvicorn是一个基于Python的ASGI（异步服务器网关接口）Web服务器
### 安装starlette(可选:在我本机编译器上没有提示安装此模块，但是在测试的时候部署在云服务器上时提示`ModuleNotFoundError: No module named 'starlette'`错误)
    pip3 install starlette
##### Starlette 是一个轻量级的 ASGI 框架，适用于构建高性能的异步 Web 应用程序。它是由编写过 Flask 和 Werkzeug 的同一组开发人员创建的，因此在设计上有很多相似之处。Starlette 具有简单易用的 API，支持 WebSocket、HTTP/2 和 GraphQL 等协议，可以与任何 ASGI 服务器一起使用
### 安装FastAPI
    pip3 install fastapi
### 安装openai
    pip3 install openai
### 启动项目
    nohup python3 -u app.py > nohup.log 2>&1 &
### 编辑计划任务
     crontab -e
### 黏贴以下命令
    0 5 * * * cd /root/ChatGPTServerSide && nohup python3 -u app.py > nohup.log 2>&1 &
##### 这表示每天凌晨5点启动服务
### 创建服务
    nano /etc/systemd/system/ChatGPTServerSide.service
### 黏贴以下命令
    [Unit]
    Description=ChatGPTServerSide
    After=network.target
    Wants=network.target

    [Service]
    ExecStart=nohup python3 -u /root/ChatGPTServerSide/app.py > nohup.log 2>&1 &
    Restart=always

    [Install]
    WantedBy=multi-user.target
### 使service文件生效
    systemctl daemon-reload
### 启动服务
    systemctl start ChatGPTServerSide.service
### 查看服务运行状态
    systemctl status ChatGPTServerSide.service
### 设置开机自动启动
    systemctl enable ChatGPTServerSide.service
