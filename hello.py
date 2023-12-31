from flask import Flask, render_template, url_for
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')
    
@app.route("/second_page")
def second_page():
    return render_template('registration.html', subtitle='Second Page', text='This is the second page')
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")