# 使用官方的 Nginx 映像檔作為基底映像檔
FROM nginx:alpine

# 設定工作目錄
WORKDIR /usr/share/nginx/html

# 複製 CSIT2017 目錄到容器中
COPY CSIT2017 /usr/share/nginx/html/CSIT2017

# 暴露 Nginx 的預設端口
EXPOSE 80

# 啟動 Nginx 伺服器
CMD ["nginx", "-g", "daemon off;"]
