from flask import Flask, render_template, request, session, redirect, url_for, g, flash
import hashlib
import sqlite3
import telegram
import smtplib


def heart_rate(gender,age,rate):
    if gender == 'male':
        if ((age>=18 and age <=25) and (rate>=49 and rate<=55)) or ((age>=26 and age <=35) and (rate>=49 and rate<=54)) or ((age>=36 and age <=45) and (rate>=50 and rate<=56)) or ((age>=46 and age <=55) and (rate>=50 and rate<=57)) or ((age>=56 and age <=65) and (rate>=51 and rate<=56)) or ((age>=65) and (rate>=50 and rate<=55)):
            res='Athlete'
        elif ((age>=18 and age <=25) and (rate>=56 and rate<=61)) or ((age>=26 and age <=35) and (rate>=55 and rate<=61)) or ((age>=36 and age <=45) and (rate>=57 and rate<=62)) or ((age>=46 and age <=55) and (rate>=58 and rate<=63)) or ((age>=56 and age <=65) and (rate>=57 and rate<=61)) or ((age>=65) and (rate>=56 and rate<=61)):
            res='Excellent'
        elif ((age>=18 and age <=25) and (rate>=62 and rate<=65)) or ((age>=26 and age <=35) and (rate>=62 and rate<=65)) or ((age>=36 and age <=45) and (rate>=63 and rate<=66)) or ((age>=46 and age <=55) and (rate>=64 and rate<=67)) or ((age>=56 and age <=65) and (rate>=62 and rate<=67)) or ((age>=65) and (rate>=62 and rate<=65)):
            res='Great'
        elif ((age>=18 and age <=25) and (rate>=66 and rate<=69)) or ((age>=26 and age <=35) and (rate>=66 and rate<=70)) or ((age>=36 and age <=45) and (rate>=67 and rate<=70)) or ((age>=46 and age <=55) and (rate>=68 and rate<=71)) or ((age>=56 and age <=65) and (rate>=68 and rate<=71)) or ((age>=65) and (rate>=66 and rate<=69)):
            res='Good'
        elif ((age>=18 and age <=25) and (rate>=70 and rate<=73)) or ((age>=26 and age <=35) and (rate>=71 and rate<=74)) or ((age>=36 and age <=45) and (rate>=71 and rate<=75)) or ((age>=46 and age <=55) and (rate>=72 and rate<=76)) or ((age>=56 and age <=65) and (rate>=72 and rate<=75)) or ((age>=65) and (rate>=70 and rate<=73)):
            res='Average'
        elif ((age>=18 and age <=25) and (rate>=74 and rate<=81)) or ((age>=26 and age <=35) and (rate>=75 and rate<=81)) or ((age>=36 and age <=45) and (rate>=76 and rate<=82)) or ((age>=46 and age <=55) and (rate>=77 and rate<=83)) or ((age>=56 and age <=65) and (rate>=76 and rate<=81)) or ((age>=65) and (rate>=74 and rate<=79)):
            res='Below Average'
        elif ((age>=18 and age <=25) and (rate>=82)) or ((age>=26 and age <=35) and (rate>=82)) or ((age>=36 and age <=45) and (rate>=83)) or ((age>=46 and age <=55) and (rate>=84)) or ((age>=56 and age <=65) and (rate>=82)) or ((age>=65) and (rate>=80)):
            res='Poor'
    elif gender == 'female':
        if ((age>=18 and age <=25) and (rate>=54 and rate<=60)) or ((age>=26 and age <=35) and (rate>=54 and rate<=59)) or ((age>=36 and age <=45) and (rate>=54 and rate<=59)) or ((age>=46 and age <=55) and (rate>=54 and rate<=60)) or ((age>=56 and age <=65) and (rate>=54 and rate<=59)) or ((age>=65) and (rate>=54 and rate<=59)):
            res='Athlete'
        elif ((age>=18 and age <=25) and (rate>=61 and rate<=65)) or ((age>=26 and age <=35) and (rate>=60 and rate<=64)) or ((age>=36 and age <=45) and (rate>=60 and rate<=64)) or ((age>=46 and age <=55) and (rate>=61 and rate<=65)) or ((age>=56 and age <=65) and (rate>=60 and rate<=64)) or ((age>=65) and (rate>=60 and rate<=64)):
            res='Excellent'
        elif ((age>=18 and age <=25) and (rate>=66 and rate<=69)) or ((age>=26 and age <=35) and (rate>=65 and rate<=68)) or ((age>=36 and age <=45) and (rate>=65 and rate<=69)) or ((age>=46 and age <=55) and (rate>=66 and rate<=69)) or ((age>=56 and age <=65) and (rate>=65 and rate<=68)) or ((age>=65) and (rate>=65 and rate<=68)):
            res='Great'
        elif ((age>=18 and age <=25) and (rate>=70 and rate<=73)) or ((age>=26 and age <=35) and (rate>=69 and rate<=72)) or ((age>=36 and age <=45) and (rate>=70 and rate<=73)) or ((age>=46 and age <=55) and (rate>=70 and rate<=73)) or ((age>=56 and age <=65) and (rate>=69 and rate<=73)) or ((age>=65) and (rate>=69 and rate<=72)):
            res='Good'
        elif ((age>=18 and age <=25) and (rate>=74 and rate<=78)) or ((age>=26 and age <=35) and (rate>=73 and rate<=76)) or ((age>=36 and age <=45) and (rate>=74 and rate<=78)) or ((age>=46 and age <=55) and (rate>=74 and rate<=77)) or ((age>=56 and age <=65) and (rate>=74 and rate<=77)) or ((age>=65) and (rate>=73 and rate<=76)):
            res='Average'
        elif ((age>=18 and age <=25) and (rate>=79 and rate<=84)) or ((age>=26 and age <=35) and (rate>=77 and rate<=82)) or ((age>=36 and age <=45) and (rate>=79 and rate<=84)) or ((age>=46 and age <=55) and (rate>=78 and rate<=83)) or ((age>=56 and age <=65) and (rate>=78 and rate<=83)) or ((age>=65) and (rate>=77 and rate<=84)):
            res='Below Average'
        elif ((age>=18 and age <=25) and (rate>=85)) or ((age>=26 and age <=35) and (rate>=83)) or ((age>=36 and age <=45) and (rate>=85)) or ((age>=46 and age <=55) and (rate>=84)) or ((age>=56 and age <=65) and (rate>=84)) or ((age>=65) and (rate>=85)):
            res='Poor'
    return res

def BMI(W,H):
    bmi=(W/(H**2))*10000
    if bmi<=18.5:
        res='Under Weight'
    elif (bmi>18.5 and bmi<=24.9):
        res='Normal Weight'
    elif (bmi>=25 and bmi<=29.9):
        res='Over Weight'
    elif (bmi>=30):
        res='Obesity'
    return bmi,res

def SBP(gender,age,weight,height):
    if gender=='male':
        sbp=109.3+(0.5*age)+(0.1*weight)-(0.6*height)
    else:
        #sbp=106.3+(0.5*age)+(0.1*weight)-(0.6*height)
        sbp=70+(2*age)
    return sbp
def DBP(age,weight,height):
    dbp=63.7+(0.1*age)+(0.2*weight)-(0.1*height)
    #
    return dbp
def BP(gender,age,weight,height):
    sbp=SBP(gender, age, weight, height)
    dbp=DBP(age, weight, height)
    bp=dbp+((1/3)*(sbp-dbp))
    return bp


app = Flask(__name__)
app.secret_key = 'secret_key'

DATABASE = 'users.db'

# Get a database connection for the current request
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    if 'username' in session:
        return f'Welcome, {session["username"]}! <a href="/logout">Logout</a>'
    else:
        return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if user:
            return render_template('signup.html', error='Username already exists.')
        else:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            db.commit()
            session['username'] = username
            return redirect(url_for('home'))
    else:
        return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if user and user[2] == hashlib.sha256(password.encode()).hexdigest():
            session['username'] = username
            flash('You were successfully logged in.')
            return redirect(url_for('calc'))
        else:
            return render_template('login.html', error='Invalid username or password.')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You were successfully logged out.')
    return redirect(url_for('home'))

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        global norm
        gender = request.form.get('gender')
        age = int(request.form['age'])
        rate = int(request.form['heart_rate'])
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        temp = float(request.form['temperature'])
        email=str(request.form['email'])
        if (temp>=97 and temp<=99):
            norm='Normal'
        else:
            norm='not Normal'
        if not all([gender, age, rate, weight, height]):
            flash('Please fill in all fields.')
            return render_template('form.html')
        elif 0 in [age, rate, weight, height]:
            flash('Please enter valid inputs.')
            return render_template('form.html')
        else:
            global bmi
            global bp
            global hr 
            bmi = BMI(weight,height)
            bp=BP(gender, age, weight, height)
            hr=heart_rate(gender,age,rate)
            print('mail')
            email = str(request.form['email'])
            # Add code to send an email using the email address entered by the user
            # Here's an example using the smtplib library
            sender_email = 'MAIL_ID'
            password = 'PASSWORD'
            message = f'Subject: Results\n\nBMI: {bmi}, BP: {bp}, Heart Rate: {hr}, Temperature: {norm}'
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login(sender_email, password)
                smtp.sendmail(sender_email, email, message)
            flash('Email sent successfully')
            return render_template('result.html', bmi=bmi,bp=bp,hr=hr,tem=temp,nor=norm)
    return render_template('form.html')



if __name__ == '__main__':
    app.run(debug=True,port=1500)