from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    topics0 = ["電腦網路與資訊處理技術", "分散式系統與雲端計算", "資料庫與大數據科學", "人工智慧與機器學習", "多媒體影音處理", "數位學習與學習科技", "生物資訊與醫學工程"]
    topics1 = ["射頻元件與積體電路設計",  "無線通訊與訊號處理", "無線、感測、行動網路與物聯網", "虛擬擴增實境與人機介面設計", "社群網路服務與大數據分析", "網路安全與區塊鏈技術", "軟體工程"]
    return render_template('index.html', topics0=topics0, topics1=topics1)

@app.route('/agenda')
def agenda():
    return render_template('agenda.html')

@app.route('/organization')
def organization():
    return render_template('organization.html')

@app.route('/traffic')
def traffic():
    return render_template('traffic.html')

@app.route('/program')
def program():
    return render_template('program.html')

if __name__ == '__main__':
   # app.run(host="0.0.0.0", debug=True)
   app.run(host="0.0.0.0", debug=False, port=3333)