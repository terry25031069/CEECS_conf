from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
    app.run(debug=True)