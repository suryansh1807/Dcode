from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/places')
def places():
    return render_template('places.html')
@app.route('/comingsoon')
def contactMe():
    return render_template('comingsoon.html')
if __name__ == '__main__':
    app.run(debug=True)


