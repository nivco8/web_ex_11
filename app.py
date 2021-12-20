from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)

@app.route('/home_page')
@app.route('/home')
@app.route('/')
def home_page():
    return render_template('cv.html')

@app.route('/assignment8')
def details():
    return render_template('assignment8.html',
                           degrees='bsc',
                           hobbies=('playing soccer', 'playing guitar', 'swimming'),
                           visited_places=['costa rica', 'brazil', 'Peru', 'argentina', 'amsterdam'],
                           like_the_course=True)


if __name__ == '__main__':
    app.run(debug=True)
