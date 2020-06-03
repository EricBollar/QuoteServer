from flask import Flask, render_template, request, jsonify
import quoteAPI

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', quote = "Test Quote", author = "Test Author")

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

@app.route('/test', methods=['POST'])
def test():
    keyword = list(request.form.to_dict())[0]
    print(keyword)
    tupl = quoteAPI.getQuoteWithKeyword(keyword)
    print(tupl[0])
    print(tupl[1])
    return jsonify(tupl)

if __name__ == '__main__':
    if (quoteAPI.isServer()):
        app.run(host='0.0.0.0')
    else:
        app.run(host='127.0.0.1')