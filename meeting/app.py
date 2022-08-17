from flask import Flask,render_template,request,redirect
from models import db,Meetings

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meetings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')

    if request.method == 'POST':

        topic = request.form['topic']
        date = request.form['date']
        s_Time = request.form['s_Time']
        e_Time = request.form['e_Time']
        users = request.form['users']
        meetings = Meetings(
            topic=topic,
            date=date,
            s_Time=s_Time,
            e_Time=e_Time,
            users=users
        )
        db.session.add(meetings)
        db.session.commit()
        return redirect('/')

@app.route('/list')
def list():
    meetings = Meetings.query.all()
    return render_template('list.html',meetings = meetings)

@app.route('/<int:id>/edit',methods = ['GET','POST'])
def update(id):
    meetings = Meetings.query.filter_by(id=id).first()

    if request.method == 'POST':
        if meetings:
            db.session.delete(meetings)
            db.session.commit()

        topic = request.form['topic']
        date = request.form['date']
        s_Time = request.form['s_Time']
        e_Time = request.form['e_Time']
        users = request.form['users']

        meetings = Meetings(
            topic=topic,
            date=date,
            s_Time=s_Time,
            e_Time=e_Time,
            users=users
        )
        db.session.add(meetings)
        db.session.commit()
        return redirect('/')

    return render_template('update.html', meetings = meetings)

@app.route('/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    meetings = Meetings.query.filter_by(id=id).first()
    if request.method == 'POST':
        if meetings:
            db.session.delete(meetings)
            db.session.commit()
            return redirect('/')
    return render_template('delete.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)