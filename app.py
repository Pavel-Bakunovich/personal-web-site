from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/my-story')
def my_story():
    return render_template('my-story.html')

if __name__ == '__main__':
    app.run(debug=True)
