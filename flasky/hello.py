from flask import Flask, request, make_response, render_template
import debugger 

debugger.initializeFlaskServiceDebuggerIfNeeded()

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')

     # response = make_response('<h1>This document carries a cookie!</h1>')
     # response.set_cookie(42)
     # return response
     # userAgent = request.headers.get('User-Agent')
     # return f'<p>Your browser is {userAgent}</p>'


@app.route('/user/<name>')
def user(name): 
     return render_template('user.html', name=name)
     # return f'<h1>Hello, {name}!</h1>'

