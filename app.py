from flask import Flask, render_template,request,redirect,url_for
from matching import find_matches_with_groups
from emailmatching import is_valid_email

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',ans=[])

@app.route('/results',methods=['POST','GET'])
def load_results():
    if request.method=='GET':
        return  redirect(url_for('index'))
    
    #take input from the html
    string=request.form['string']
    pattern=request.form['pattern']
    ans=find_matches_with_groups(string,pattern)
    return render_template('regex_matching.html',ans=ans)

@app.route('/email')
def email():
    return render_template('email.html',ans=[])

@app.route('/regex')
def regex():
    return render_template('regex_matching.html',ans=[])

@app.route('/valid_email_page',methods=['POST','GET'])
def valid_email_page():
    if request.method=='GET':
        return  redirect(url_for('index'))
    
    email=request.form['email']
    ans=str(is_valid_email(email))
    return render_template('email.html',ans=ans)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)
