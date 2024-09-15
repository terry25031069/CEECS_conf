# 使用官方的 Python 映像檔作為基底映像檔
FROM python:3.9-alpine

# 設定工作目錄
WORKDIR /app

# 複製 CSIT2017 目錄到容器中
COPY CSIT2017 /app

# 安裝 Flask
RUN pip install flask

# 暴露 Flask 的預設端口
EXPOSE 3333

# 啟動 Flask 應用程序
CMD ["python", "app.py"]

# docker build -t csit .
# docker run --name csit-container -p 80:3333 --memory 512m csit