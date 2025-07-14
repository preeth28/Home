from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])

def calculate():
    result=None
    error=None
    if request.method == 'POST':
        try:
            choice = request.form['operator']
            a = int(request.form['num1'])
            b = int(request.form['num2'])

            if choice == '+':
                result = f"{a}+{b}={a+b}"
            else:
                error = 'Invalid input'

        except:
            error = 'Invalid'

    return render_template('add.html', result=result, error=error)

if __name__ == '__main__':
    app.run()