from flask import Flask,render_template,request
import mysql.connector as sql

app = Flask('anil')

my_connection = sql.connect(
    host="localhost",
    user="public",
    password="Password#123",
    database="flask_test"
)

my_cursor = my_connection.cursor()

my_connection.close()

@app.route("/",methods=['GET'])
def welcome():
    return {"response":"Hey user, welcome to anil_flask app"}

@app.route("/book-event",methods=['GET'])
def book_event():
    return {"response":"You are in book events page"}

@app.route("/cancel-event",methods=['GET'])
def cancel_event():
    return {"response":"You are in cancel events page"}

@app.route("/user-data",methods=['GET'])
def user_data():
    return render_template("user_data.html")

@app.route("/get-user-data",methods=['POST'])
def get_user_data():
    _id = request.form['id']
    user_name = request.form['username']
    user_age = request.form['user_age']
    query = """
        INSERT INTO anil(id, user_name, user_age)
        values(%s, %s, %s)
    """
    values = (_id, user_name, user_age)
    my_cursor.execute(query,values)
    my_connection.commit()
    print(_id, user_name,user_age)
    return {'response':'data received successfully'}
    