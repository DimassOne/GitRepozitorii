from flask import Flask, session
from checker import chek

app = Flask(__name__)
app.secret_key='KJKDlkjl'

def func()->bool:
    if 'user' in session:
        return True
    return False

@app.route('/')
def page()->str:
    return "Это главная страница"

@app.route('/login')
def login():
    session['user'] = True
    return "Вы вошли в систему"

@app.route('/logout')
def logout():
    session.pop('user')
    return "Вы вышли из системы"

@app.route('/page1')
@chek
def page1():
    if func():
        return "Это первая страница"
    return "Вы не авторизованны"

@app.route('/page2')
@chek
def page2():
    return "Это вторая страница"




if __name__ == '__main__':
    app.run(debug=True)


























##from flask import Flask, session
##from pprint import pprint
##from checker import check_logged_in
##
##app=Flask(__name__)
##
##
##@app.route('/login')
##def do_login()->str:
##    session['logged_in'] = True
##    return "Теперь вы в системе"
##
##app.secret_key = 'LsdfASFASDFA'
##
##def func()->bool:
##    if 'logged_in' in session:
##        return True
##    return False
##    
##
##@app.route('/logout')
##def do_logout()->str:
##    if 'logged_in' in session:
##        session.pop('logged_in')
##        return "Вы вышли из системы"
##    return "Вы вышли из системы"
##    
##    
##
##@app.route('/status')
##def check_status()->str:
##    if 'logged_in' in session:
##        return "Вы в системе"
##    return "Вы не в системе"
##
##
##
##@app.route('/')
##def hello()->str:
##    return "Эта главная страница"
##
##@app.route('/page1')
##@check_logged_in
##def page1()->str:
##    return "Эта вторая страница"
##   
##        
##    
##@app.route('/page2')
##@check_logged_in
##def page2()->str:
##    return "Ну а это третья страница"
##
##
##
##if __name__ == '__main__':
##    app.run(debug=True)
           
