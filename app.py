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


if __name__=="__main__":
    
    app.run(debug=True)
