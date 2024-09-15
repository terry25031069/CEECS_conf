from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    topics0 = ["電腦網路與資訊處理技術", "分散式系統與雲端計算", "資料庫與大數據科學", "人工智慧與機器學習", "多媒體影音處理", "數位學習與學習科技", "生物資訊與醫學工程"]
    topics1 = ["射頻元件與積體電路設計",  "無線通訊與訊號處理", "無線、感測、行動網路與物聯網", "虛擬擴增實境與人機介面設計", "社群網路服務與大數據分析", "網路安全與區塊鏈技術", "軟體工程"]
    return render_template('index.html', topics0=topics0, topics1=topics1)

@app.route('/agenda')
def agenda():
    schedule = [
        {
            "date": "11月27日(星期一)",
            "events": [
                {"time": "17:00", "description": "抵達桃園國際機場"},
                {"time": "18:30", "description": "註冊/接待晚宴/安排住宿"}
            ]
        },
        {
            "date": "11月28日(星期二)",
            "events": [
                {"time": "09:00 ~ 09:30", "description": "開幕致詞"},
                {"time": "09:30 ~ 09:45", "description": "貴賓合影"},
                {"time": "09:45 ~ 10:30", "description": "【專題演講I】 演講者：中央大學資訊工程學系 張嘉惠 教授 講 題：From Information Extraction to Message Understanding - The Ultimate Challenge of AI 人工智慧的終極挑戰-自然語言理解 地 點：工程五館A207 主持人：國立中央大學資訊工程學系許富皓主任"},
                {"time": "10:30 ~ 10:40", "description": "茶敘"},
                {"time": "10:40 ~ 11:25", "description": "【專題演講II】 演講者：中央大學網路學習科技研究所 陳德懷 講座教授 講 題：明日閱讀與數位學習趨勢 地 點：工程五館A207 主持人：國立中央大學資電學院邱煥凱副院長"},
                {"time": "11:25 ~ 12:10", "description": "【專題演講III】 演講者：南京大學計算機科學與技術系 高陽 教授 講 題：多智能體強化學習中的博弈與均衡 地 點：工程五館A207 主持人：東南大學電腦科學與工程學院李偉副院長"},
                {"time": "12:10 ~ 13:30", "description": "午餐"},
                {"time": "13:30 ~ 15:00", "description": "【研討會 A1】 通訊工程/電路設計 工程五館 A203"},
                {"time": "13:30 ~ 15:00", "description": "【研討會 B1】 多媒體處理/資訊安全 工程五館 A301"},
                {"time": "13:30 ~ 15:00", "description": "【研討會 C1】 醫療工程/深度學習 工程五館 A302"},
                {"time": "15:00 ~ 15:30", "description": "茶敘"},
                {"time": "15:30 ~ 17:00", "description": "【研討會 A2】 資料處理工程 工程五館 A203"},
                {"time": "15:30 ~ 17:00", "description": "【研討會 B2】 資料傳輸工程 工程五館 A301"},
                {"time": "15:30 ~ 17:00", "description": "【研討會 C2】 資料庫工程/學習科技 工程五館 A302"},
                {"time": "18:30 ~ 21:00", "description": "晚宴"}
            ]
        },
        {
            "date": "11月29日(星期三)",
            "events": [
                {"time": "09:00 ~ 12:00", "description": "技術會議(分組討論) 地點:工程五館A301、A203、A205會議室"},
                {"time": "14:00 ~ 17:00", "description": "海報張貼 地點:工程五館一樓大廳"}
            ]
        },
        {
            "date": "11月30日(星期四)",
            "events": [
                {"time": "09:00 ~ 12:00", "description": "技術會議(分組討論) 地點:工程五館A301、A203、A205會議室"},
                {"time": "14:00 ~ 17:00", "description": "海報張貼 地點:工程五館一樓大廳"}
            ]
        }
    ]
    return render_template('agenda.html', schedule=schedule)

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