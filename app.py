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
#session = session()
app.config['SECRET_KEY']='super secret key'
conn=mysql.connector.connect(host="localhost",user="root",password="jaynil",database="mydatabase")
cursor = conn.cursor(buffered=True)
conn1=mysql.connector.connect(host="localhost",user="root",password="jaynil",database="feedback")
cursor1=conn1.cursor()
# email1=''

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

@app.route('/feedback.html',methods=["GET","POST"])
def feedback():
    
    if (request.method=="POST"):
        
        name=request.form['name']
        email=request.form['email']
        textarea=request.form['message']
       
      
    # store data into database  
        cursor1.execute("INSERT INTO users (name,emaill,message) VALUES (%s,%s,%s)",(name,email,textarea))
        
        
        conn1.commit()
        cursor1.close()
        conn1.close()
       
        return redirect(url_for('feedback'))


    return render_template('feedback.html')

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
        
        if(gender=="1"):
            gender1=1
        else:
            gender1=0    
        

# Load the model from the .pkl file
        with open('svc.pkl', 'rb') as file:
            loaded_model = pickle.load(file)
        result=loaded_model.predict(np.array([[cpi,projects,hackathon,skills,branch,gender1]]))
        return render_template('analytics.html',result=result)
    return render_template('analytics.html')

@app.route('/page.html')
def page():
    mainemail = session.get('emailm', None)
    cursor.execute('SELECT name FROM users WHERE email = %s',(mainemail,))
    name= cursor.fetchone()
    # for names in name:
    #     name1=names
    cursor.execute('SELECT enroll FROM users WHERE email = %s',(mainemail,))
    enroll= cursor.fetchone()
    cursor.execute('SELECT program FROM users WHERE name = %s',('patel jaynil',))
    program= cursor.fetchone()
    cursor.execute('SELECT course FROM users WHERE name = %s',('patel jaynil',))
    course= cursor.fetchone()
    cursor.execute('SELECT gender FROM users WHERE name = %s',('patel jaynil',))
    gender= cursor.fetchone()
    cursor.execute('SELECT email FROM users WHERE name = %s',('patel jaynil',))
    email= cursor.fetchone()
    cursor.execute('SELECT phone FROM users WHERE name = %s',('patel jaynil',))
    phone= cursor.fetchone()
    cursor.execute('SELECT dob FROM users WHERE name = %s',('patel jaynil',))
    dob= cursor.fetchone()
    cursor.execute('SELECT address FROM users WHERE name = %s',('patel jaynil',))
    address= cursor.fetchone()
    cursor.execute('SELECT city FROM users WHERE name = %s',('patel jaynil',))
    city= cursor.fetchone()
    cursor.execute('SELECT state FROM users WHERE name = %s',('patel jaynil',))
    state= cursor.fetchone()
    cursor.execute('SELECT tenth FROM users WHERE name = %s',('patel jaynil',))
    tenth= cursor.fetchone()
    cursor.execute('SELECT twelfth FROM users WHERE name = %s',('patel jaynil',))
    twelfth= cursor.fetchone()
    cursor.execute('SELECT year FROM users WHERE name = %s',('patel jaynil',))
    year= cursor.fetchone()
    cursor.execute('SELECT avggpa FROM users WHERE name = %s',('patel jaynil',))
    avggpa= cursor.fetchone()
    cursor.execute('SELECT institute FROM users WHERE name = %s',('patel jaynil',))
    institute= cursor.fetchone()
    cursor.execute('SELECT teckskills FROM users WHERE name = %s',('patel jaynil',))
    teckskills= cursor.fetchone()
    cursor.execute('SELECT nontechskills FROM users WHERE name = %s',('patel jaynil',))
    nontechskills= cursor.fetchone()
    cursor.execute('SELECT internships FROM users WHERE name = %s',('patel jaynil',))
    internships= cursor.fetchone()
    cursor.execute('SELECT projects FROM users WHERE name = %s',('patel jaynil',))
    projects= cursor.fetchone()

    return render_template('page.html',projects=projects ,internships=internships,nontechskills=nontechskills,teckskills=teckskills,institute=institute,avggpa= avggpa,year=year,name=name,enroll=enroll,program=program,course=course,gender=gender,email=email,phone=phone,dob=dob,address=address,city=city,state=state,tenth=tenth,twelfth=twelfth)

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
        session['emailm']=email1
        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email1, password1, ))
        user = cursor.fetchall()
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
        username=request.form['username']
        phone=request.form['phone']
        address=request.form['address']
        dob=request.form['dob']
        gender=request.form['gender']
        city=request.form['city']
        state=request.form['state']
        tenthPercentage=request.form['tenthPercentage']
        twelfthPercentage=request.form['twelfthPercentage']
        program=request.form['program']
        graduationCourse=request.form['graduationCourse']
        yearOfPassing=request.form['yearOfPassing']
        institute=request.form['institute']
        enrollmentnumber=request.form['Enrollment number']
        averageGPA=request.form['averageGPA']
        technicalSkills=request.form['technicalSkills']
        nonTechnicalSkills=request.form['nonTechnicalSkills']
        internships=request.form['internships']
        projects=request.form['projects']
        email=request.form['email']
        password=request.form['confirmPassword']
       
      
    # store data into database  
        cursor.execute("INSERT INTO users (name,email,password,username,phone,address,dob,gender,city,state,tenth,twelfth,program,course,year,institute,enroll,avggpa,teckskills,nontechskills,internships,projects) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,email,password,username,phone[4],address,dob,gender,city,state,tenthPercentage,twelfthPercentage,program,graduationCourse,yearOfPassing,institute,enrollmentnumber,averageGPA,technicalSkills,nonTechnicalSkills,internships,projects))
        
        
        conn.commit()
        cursor.close()
        conn.close()
       
        return redirect(url_for('login'))

      
    return render_template('profile1.html')
    #return render_template('signup.html')

if __name__ == '__main__':
    # app.secret_key = 'super secret key'
    # app.config['SESSION_TYPE'] = 'filesystem'

    # session.init_app(app)
    app.run(debug=True,port=8000)