from flask import Flask,render_template, redirect, url_for, session, flash,request
from flask_wtf import FlaskForm
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import bcrypt
from flask_mysqldb import MySQL
import mysql.connector

app=Flask(__name__)
conn=mysql.connector.connect(host="localhost",user="root",password="jaynil",database="mydatabase")
cursor = conn.cursor()

#pages connection
@app.route('/')
def index():
    return render_template('landing page.html')

@app.route('/insights.html')
def insights():
    return render_template('insights.html')

@app.route('/Admin.html')
def Admin():
    return render_template('Admin.html')

@app.route('/analysis.html')
def analysis():
    return render_template('analysis.html')

@app.route('/analytics.html',methods=["GET","POST"])
def analytics():
    result=""
    if (request.method=="POST"):       
        cpi=request.form['cpi']
        projects=request.form['projects']
        hackathon=request.form['hackathon']
        skills=request.form['skills']
        branch=request.form['branch']
        gender=request.form['gender']
        

# Load the model from the .pkl file
        with open('svc.pkl', 'rb') as file:
            loaded_model = pickle.load(file)
        result=loaded_model.predict(np.array([[cpi,projects,hackathon,skills,branch,gender]]))
        return render_template('analytics.html',result=result)
    return render_template('analytics.html')

@app.route('/page.html')
def page():
    return render_template('page.html')

@app.route('/trends.html')
def trends():
    return render_template('trends.html')


#machine learning
@app.route('/predict')
def predict():
     pass 



#connection
@app.route('/login',methods=["GET","POST"])
def login():
    message=''
    if (request.method=='POST'):
        cursor = conn.cursor()
        email1=request.form['email']
        password1=request.form['password']
        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email1, password1, ))
        user = cursor.fetchone()
        # print(user)
        if user:
                
                message = 'Logged in successfully !'
                return render_template('Admin.html')
        else:
                message = 'Please enter correct email / password !'

    return render_template('login.html',message=message)

@app.route('/signup',methods=["GET","POST"])
def signup():
   
    if (request.method=="POST"):
        
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
       
      
    # store data into database  
        cursor.execute("INSERT INTO users (name,email,password) VALUES (%s,%s,%s)",(name,email,password))
        
        
        conn.commit()
        cursor.close()
        conn.close()
       
        return redirect(url_for('login'))

      

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True,port=8000)