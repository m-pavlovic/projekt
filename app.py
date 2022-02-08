from flask import Flask, render_template

app = Flask(__name__)

@app.route('/blog')
def index():
    return render_template('blog.html')

@app.route('/faq')
def index():
    return render_template('faq.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kontakt')
def index():
    return render_template('kontakt.html')

@app.route('/linkovi')
def index():
    return render_template('linkovi.html')

@app.route('/obrazac')
def index():
    return render_template('obrazac.html')

@app.route('/opgovi')
def index():
    return render_template('opgovi.html')

if __name__ == '__main__':
    app.run(debug=True)