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
                {"time": "09:45~10:45", "description": ["【專題演講I】演講者：過敏意教授/上海交通大學  【專題演講II】演講者：施國琛教授/中央大學"], "colspan": 4, "type": "1"},
                {"time": "10:45~11:00", "description": ["休息/交流時間"], "colspan": 4, "type": "1"},
                {"time": "11:00~12:00", "description": ["【專題演講III】演講者：王帥教授/東南大學  【專題演講IV】演講者：胡誌麟教授/中央大學"], "colspan": 4, "type": "1"},
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

    return render_template('agenda.html', schedule=schedule)

@app.route('/organization')
def organization():
    return render_template('organization.html')

@app.route('/program')
def program():
    return render_template('program.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, port=3333)