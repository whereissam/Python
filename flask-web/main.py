from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost:3306/test1"

db.init_app(app)


@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/conn')
def conn():
    sql = "select DATABASE()"
    result = db.engine.execute(sql)
    record = result.fetchone()
    print(record)
    return '資料庫已連線'


@app.route('/student')
def student():
    table = '''<thead><th>ID</th>
                <th>Name</th>
                <th>Sex</th>
                <th>Age</th>
                <th>Dept</th></thead>'''

    sql = "Select * from student"
    result = db.engine.execute(sql)
    record = result.fetchall()
    for i in record:
        table += '''<tr><td>''' + str(i[0]) + '''</td>
                        <td>''' + str(i[1]) + '''</td>
                        <td>''' + str(i[2]) + '''</td>
                        <td>''' + str(i[3]) + '''</td>
                        <td>''' + str(i[4]) + '''</td></tr> '''
    # print(table)
    return '<table border=1>' + table + '</table>'


@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method == 'POST':
        ID = request.form.get('ID')
        Name = request.form.get('Name')
        Sex = request.form.get('Sex')
        Age = request.form.get('Age')
        Dept = request.form.get('Dept')

        sql = 'INSERT INTO student (ID, Name, Sex, Age, Dept) VALUES (%s, %s, %s, %s, %s)'
        result = db.engine.execute(sql, (ID, Name, Sex, Age, Dept))

        db.session.commit() #call db say it's commited
        return '已新增 ' + request.form.get('ID')

    return render_template('submit.html')


if __name__ == "__main__":
    app.run()