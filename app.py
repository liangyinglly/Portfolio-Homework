from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/experiences')
def experiences():
    return render_template('experiences.html')

@app.route('/moreInfo')
def moreInfo():
    return render_template('moreInfo.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('user.html', username = username)
        
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)