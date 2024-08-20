from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Signin')
def Signin():
    return render_template('Signin.html')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/kota')
def kota():
    return render_template('kota.html')

@app.route('/chips')
def chips():
    return render_template('chips.html')

@app.route('/archaar')
def archaar():
    return render_template('archaar.html')

@app.route('/plate')
def plate():
    return render_template('plate.html')


if __name__=="__main__":
    
    app.run(debug=True)
