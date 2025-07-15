from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html') #this is the home page
    

@app.route('/add',methods=['GET','POST'])
def add():
    result=None
    error=None
    if request.method == 'POST':
        try:
            a = int(request.form['num1'])
            b = int(request.form['num2'])
            result = f"{a}+{b}={a+b}"
        
        except:
            error = 'Invalid'

    return render_template('add.html', result=result, error=error)

@app.route('/sub',methods=['GET','POST'])
def sub():
    result=None
    error=None
    if request.method == 'POST':
        try:
            a = int(request.form['num1'])
            b = int(request.form['num2'])
            result = f"{a}-{b}={a-b}"


            

        except:
            error = 'Invalid'

    return render_template('sub.html', result=result, error=error)

@app.route('/mul',methods=['GET','POST'])
def mul():
    result=None
    error=None

    if request.method == 'POST':
        try:
            a = int(request.form['num1'])
            b = int(request.form['num2'])
            result = f"{a}*{b}={a*b}"


        except:
            error = 'Invalid'

    return render_template('mul.html',result=result,error=error)

@app.route('/div',methods=['GET','POST'])
def div():
    result=None
    error=None

    if request.method == 'POST':
        try:
            a = int(request.form['num1'])
            b = int(request.form['num2'])
            if b == 0:
                result = '0 is not divisible'
            else:
                result = f"{a}/{b}={a/b}"

        except:
            error = 'Invalid'
    return render_template('div.html', result=result, error=error)

@app.route('/cutoff',methods=['GET','POST'])
def cutoff():
    result=None
    error=None

    if request.method == 'POST':
        try:
            a=int(request.form['math'])
            b=int(request.form['phy'])           
            c=int(request.form['chem'])
            result = f"{a}+ {b/2}+ {c/2}={a+b/2+c/2}"

        except:
            error='Invalid input'

    return render_template('cutoff.html',result=result, error=error,)


if __name__ == '__main__':
    app.run()