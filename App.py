from flask import Flask , render_template ,request , redirect , url_for , flash
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
app = Flask(__name__)

app.secret_key = "Secret Key"


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Ruturaj8003#@localhost/MyDatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


mysql = SQLAlchemy(app)

class Data(mysql.Model):
    id = mysql.Column(mysql.Integer , primary_key = True)
    name = mysql.Column(mysql.String(100))
    email = mysql.Column(mysql.String(100))
    phone = mysql.Column(mysql.String(100))


    def __init__(self , name , email , phone):
        self.name = name
        self.email = email
        self.phone = phone







@app.route('/')
def Index():
    my_data = Data.query.all()
    return render_template('index.html' , employees = my_data)


@app.route('/insert' , methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        my_data = Data(name , email , phone)
        mysql.session.add(my_data)
        mysql.session.commit()
        flash("Employee Inserted Successfully.")
        return  redirect(url_for('Index'))

@app.route('/update' , methods = ['GET' , 'POST'])
def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
        mysql.session.commit()
        flash("Employee updated successfully!!")
        return redirect(url_for('Index'))


@app.route('/delete/<id>/' , methods = ['GET' , 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    mysql.session.delete(my_data)
    mysql.session.commit()
    flash("Employee deleted successfully!!")
    return redirect(url_for('Index'))





if __name__ == "__main__":
    app.run(debug=True)