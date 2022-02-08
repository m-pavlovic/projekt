from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

@app.route('/linkovi')
def linkovi():
    return render_template('linkovi.html')

@app.route('/obrazac')
def obrazac():
    return render_template('obrazac.html')

@app.route('/opgovi')
def opgovi():
    return render_template('opgovi.html')



if __name__ == '__main__':
    app.run(debug=True)