from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agenda')
def agenda():
    schedule = [
        # {
        #     "date": "1月6日(星期一)",
        #     "divname": "day1",
        #     "events": [
        #         {"time": "17:00", "description": ["抵達桃園國際機場"], "colspan": 1, "type": "1"},
        #         {"time": "18:30", "description": ["註冊/接待晚宴/安排住宿"], "colspan": 1, "type": "1"}
        #     ]
        # },
        {
            "date": "1月7日(星期二)",
            "divname": "day2",
            "events": [
                {"time": "09:00~09:30", "description": ["教研大樓 TR A203  開幕式  貴賓介紹及貴賓致詞"], "colspan": 4, "type": "0"},
                {"time": "09:30~09:45", "description": ["貴賓合影"], "colspan": 4, "type": "0"},
                {"time": "09:45~10:45", "description": ["【專題演講I】演講者：卢苇教授/北京交通大學  【專題演講II】演講者：施國琛教授/中央大學"], "colspan": 4, "type": "1"},
                {"time": "10:45~11:00", "description": ["休息/交流時間"], "colspan": 4, "type": "1"},
                {"time": "11:00~12:00", "description": ["【專題演講III】演講者：方鹏飞副教授/東南大學  【專題演講IV】演講者：陳正一教授/中央大學"], "colspan": 4, "type": "1"},
                {"time": "12:00~14:00", "description": ["午餐"], "colspan": 4, "type": "0"},
                {"time": "14:00~15:30", "description": ["【分組論壇一】  網路計算與電子分論壇  (Network Computing and Electronics)(I)  電機 E1-233 會議室", "【分組論壇二】  人工智能分論壇  (Artificial Intelligence) (I)  電機 E1-225 會議室", "【分組論壇三】  永續應用分論壇  (Sustainable Applications)  (I)  通訊 E1-211 會議室"], "colspan": 1, "type": "1"},
                {"time": "15:30~16:00", "description": ["休息/交流時間"], "colspan": 4, "type": "0"},
                {"time": "16:00~17:30", "description": ["【分組論壇一】  網路計算與電子分論壇  (Network Computing and Electronics)(II)  電機 E1-233 會議室", "【分組論壇二】  人工智能分論壇  (Artificial Intelligence) (II)  電機 E1-225 會議室", "【分組論壇三】  永續應用分論壇  (Sustainable Applications)  (II)  通訊 E1-211 會議室"], "colspan": 1, "type": "1"},
                {"time": "18:00", "description": ["晚宴"], "colspan": 4, "type": "0"}
            ]
        },
        {
            "date": "1月8日(星期三)",
            "divname": "day3",
            "events": [
                {"time": "1/8", "description": ["海峽兩岸資訊技術研討會技術會議 跨校討論  國立清華大學、國立陽明交通大學"], "colspan": 1, "type": "2"}
            ]
        },
        {
            "date": "1月9日(星期四)",
            "divname": "day4",
            "events": [
                {"time": "1/9", "description": ["海峽兩岸資訊技術研討會技術會議 跨校討論  國立中興大學"], "colspan": 1, "type": "2"}
            ]
        }
    ]
    for day in range(len(schedule)):
        for event in range(len(schedule[day]['events'])):
            if schedule[day]['events'][event]['type'] == "0":
                schedule[day]['events'][event]['titlecolor'] = '#ffcccc'
                schedule[day]['events'][event]['bgcolor'] = '#ffcccc'
            elif schedule[day]['events'][event]['type'] == "1":
                schedule[day]['events'][event]['titlecolor'] = '#ffffff'
                schedule[day]['events'][event]['bgcolor'] = '#ffffff'
            elif schedule[day]['events'][event]['type'] == "2":
                schedule[day]['events'][event]['titlecolor'] = '#ffcccc'
                schedule[day]['events'][event]['bgcolor'] = '#ffffff'
            else: pass
        
        # traverse all descriptions, split by "  "
        for event in range(len(schedule[day]['events'])):
            descriptions = schedule[day]['events'][event]['description']
            for i in range(len(descriptions)):
                tmp_list = descriptions[i].split("  ")
                schedule[day]['events'][event]['description'][i] = tmp_list

    forums = [
        {
            "title": "【分組論壇一】",
            "subtitle": "網路計算與電子分論壇 (Network Computing and Electronics) (I)",
            "hosts": "燕鋒教授、鄭國興教授",
            "time": "14:00-15:30",
            "location": "電機 E1-233 會議室",
            "titlecolor": "8eaadb",
            "papers": [
                {"id": "NCE01", "title": "應用前饋式等化器補償之接收端電路", "author": "鄭國興"},
                {"id": "NCE02", "title": "基於深度學習之二維材料原子缺陷檢測框架", "author": "林家瑜"},
                {"id": "NCE03", "title": "密集無線網路中 AP 輔助的自適應視頻流傳輸機制", "author": "吳文甲"},
                {"id": "NCE04", "title": "群感感知環境下基於社群網路的協作式多用戶任務分配方法", "author": "胡誌麟"},
                {"id": "NCE05", "title": "強烈電磁脈衝影響下多用戶 MIMO 異質網路的覆蓋機率和區域頻譜效率", "author": "燕鋒"}]
        }, {
            "title": "【分組論壇二】",
            "subtitle": "人工智能分論壇 (Artificial Intelligence) (I)",
            "hosts": "吳小俊教授、孫敏德教授",
            "time": "14:00-15:30",
            "location": "電機 E1-225 會議室",
            "titlecolor": "8eaadb",
            "papers": [
                {"id": "AI02", "title": "帳單類別郵件之郵遞區號辨識", "author": "王文俊"},
                {"id": "AI03", "title": "輸出可信的深度聚類網路", "author": "賈育衡"},
                {"id": "AI04", "title": "AI 驅動的博物館文物識別：反光消除、影像處理與分類技術的集成應用", "author": "林家瑜"},
                {"id": "AI06", "title": "CA-Wav2Lip: 基於坐標注意力的野外語音到唇部合成", "author": "孫敏德"},
                {"id": "AI07", "title": "基於深度學習的多模態視覺融合方法", "author": "吳小俊"},
                ]
        },{
            "title": "【分組論壇三】",
            "subtitle": "永續應用分論壇 (Sustainable Applications) (I)",
            "hosts": "賀龍兵教授、陳正一教授",
            "time": "14:00-15:30",
            "location": "通訊 E1-211 會議室",
            "titlecolor": "8eaadb",
            "papers": [
                {"id": "SA01", "title": "基於層次分析法與熵值法之改良式粒子群優化策略於多目標最佳化能源管理系統", "author": "陳正一"},
                {"id": "SA02", "title": "基於模糊派翠類神經網路的太陽能平滑化控制", "author": "陳正一"},
                {"id": "SA03", "title": "適配於原位 TEM 應用的電、熱學分析型芯片研製", "author": "賀龍兵"},
                {"id": "SA04", "title": "以向日葵 8 號氣象衛星預測台灣區域雨量", "author": "陳映濃"},
                {"id": "SA05", "title": "具有零電流開關和倍壓單元的高升壓直流-直流轉換器", "author": "徐國鎧"}]
        },{
            "title": "【分組論壇一】(每篇發表時間為 10 分鐘)",
            "subtitle": "網路計算與電子分論壇 (Network Computing and Electronics) (II)",
            "hosts": "吳文甲教授、陳永芳教授",
            "time": "16:00~17:30",
            "location": "電機 E1-233 會議室",
            "titlecolor": "ffe599",
            "papers": [
                {"id": "NCE06", "title": "矽量子點和光熱半導體奈米材料於綠能與生醫領域的應用", "author": "杜長慶"},
                {"id": "NCE08", "title": "RFI 對基於 FIR 的自適應均衡器影響的研究", "author": "薛木添"},
                {"id": "NCE09", "title": "基於 Zadoff-Chu 序列之多輸入多輸出低軌道衛星通訊系統迭代載波頻率偏移與通道估測演算法設計", "author": "陳永芳"},
                {"id": "NCE11", "title": "運用高效能圖形處理器與 AI 技術於無人機之實時影像偵測與追蹤", "author": "張大中"}]
        }, {
            "title": "【分組論壇二】",
            "subtitle": "人工智能分論壇 (Artificial Intelligence) (II)",
            "hosts": "吳小俊教授、孫敏德教授",
            "time": "16:00~17:30",
            "location": "電機 E1-225 會議室",
            "titlecolor": "ffe599",
            "papers": [
                {"id": "AI08", "title": "雙曲表徵的龐加萊核", "author": "方鵬飛"},
                {"id": "AI09", "title": "模組化虛擬助教與生成式 AI 學習平台之實證研究：以 Python 課程為例", "author": "張家凱"},
                {"id": "AI10", "title": "考量老化的 AI 加速器設計", "author": "陳聿廣"},
                {"id": "SA11", "title": "A Speech and Lip Reading System with Generating Text to Assist Hearing-Impaired People", "author": "蔡宗漢"}
                ]
        },{
            "title": "【分組論壇三】",
            "subtitle": "永續應用分論壇 (Sustainable Applications) (II)",
            "hosts": "丁玎教授、葉士青教授",
            "time": "16:00~17:30",
            "location": "通訊 E1-211 會議室",
            "titlecolor": "ffe599",
            "papers": [
                {"id": "SA06", "title": "流浪足跡：基於沉浸式虛擬現實的第一人稱流浪動物生活體驗系統", "author": "丁玎"},
                {"id": "SA07", "title": "重複性經顱磁刺激同步虛擬實境與生理監測用於失語症創新治療與評估", "author": "葉士青"},
                {"id": "SA08", "title": "基於姿態辨識與壓力感測的智能瑜伽指導應用", "author": "蘇木春"},
                {"id": "SA09", "title": "運用「數位魔鏡」情境學習模式提升職業教育學習成效與參與度：以餐旅管理系學生為例", "author": "陳國棟"},
                {"id": "SA10", "title": "區塊鏈整合 V2X 網路之多連接管理效能評估", "author": "黃志煒"},
                ]
        }
    ]

    return render_template('agenda.html', schedule=schedule, forums=forums)


# @app.route('/organization')
# def organization():
#     return render_template('organization.html')
@app.route("/organization")
def organization():
    honor_chair = [
        "周景揚 中央大學校長", 
        "黃　如 东南大学校長"
    ]
    conference_chair = [
        "綦振瀛 中央大學副校長", 
        "金　石 东南大学副校長"
    ]
    session_chair_0 = [
        "蘇木春 中央大學資訊電機學院", 
        "张敏灵 东南大学计算机科学与工程学院"
    ]
    session_chair_1 = [
        "王文俊 中央大學電機工程學系教授", 
        "李柏磊 中央大學資訊電機學院"
    ]
    committee_members_0 = [
        "鄭國興 中央大學電機工程學系教授", 
        "徐國鎧 中央大學電機工程學系教授", 
        "蔡宗漢 中央大學電機工程學系教授", 
        "陳正一 中央大學資訊工程學系教授", 
        "薛木添 中央大學電機工程學系副教授", 
        "陳聿廣 中央大學電機工程學系副教授", 
        "杜長慶 中央大學電機工程學系副教授", 
        "孫敏德 中央大學資訊工程學系教授", 
        "陳國棟 中央大學資訊工程學系教授", 
        "林家瑜 中央大學資訊工程學系助理教授", 
        "陳永芳 中央大學通訊工程學系教授", 
        "張大中 中央大學通訊工程學系教授", 
        "黃志煒 中央大學通訊工程學系教授", 
        "范國清 中央大學資訊工程學系教授", 
        "陳映濃 中央大學太空及遙測研究中心專案助理教授", 
        "葉士青 中央大學資訊工程學系教授", 
        "吳曉光 中央大學資訊工程學系教授", 
        "胡誌麟 中央大學通訊工程學系教授", 
    ]
    committee_members_1 = [
        "張家凱 中央大學通識教育中心專任助理教授", 
        "周承復 台灣大學資訊工程學系教授", 
        "惠　霖 淡江大學資訊工程學系教授", 
        "刘　静 东南大学港澳台办科长", 
        "楊冠羽 东南大学计算机科学与工程学院副院長", 
        "王　帅 东南大学计算机科学与工程学院教授",
        "丁　玎 东南大学计算机科学与工程学院副教授",
        "贾育衡 东南大学计算机科学与工程学院副教授",
        "方鹏飞 东南大学计算机科学与工程学院副教授",
        "吴文甲 东南大学计算机科学与工程学院副教授",
        "贺龙兵 东南大学集成电路学院教授、副院长",
        "蔡　浩 东南大学集成电路学院副教授、院长助理",
        "燕　锋 东南大学信息科学与工程学院副教授、院长助理",
        "卢　苇 北京交通大学软件学院教授",
        "过敏意 上海交通大学电子信息与电气工程学院教授",
        "吴小俊 江南大学研究生院/科技部教授、院长",
        "梁吉业 山西大学计算机与信息技术学院教授",
        "曹付元 山西大学计算机与信息技术学院教授、院长",
    ]

    return render_template(
        "organization.html",
        honor_chair=honor_chair,
        conference_chair=conference_chair,
        session_chair_0=session_chair_0,
        session_chair_1=session_chair_1,
        committee_members_0=committee_members_0,
        committee_members_1=committee_members_1,
    )

@app.route('/program')
def program():
    return render_template('program.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=3333)