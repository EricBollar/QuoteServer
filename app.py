from flask import Flask, render_template, request
import quoteAPI

app = Flask(__name__)
searchTerm = ""

@app.route('/')
def index():
    return render_template('index.html', title = "Enter a search term :)")

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    searchTerm = projectpath
    return render_template('index.html', title = quoteAPI.getQuote(searchTerm))

if __name__ == '__main__':
    if (quoteAPI.isServer()):
        app.run(host='0.0.0.0')
    else:
        app.run(host='127.0.0.1')