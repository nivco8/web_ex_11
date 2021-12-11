from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello! this is my main page'

@app.route('/MF')
def mf_func():
    return "this is MF page"

@app.route('/next')
def next_func():
    print('where are you going next redirect?')
    return redirect('/MF')

@app.route('/urlNext')
def next_url_func():
    print('where are you goin next url redirect?')
    return redirect(url_for('mf_func'))


if __name__ == '__main__':
    app.run(debug=True)
