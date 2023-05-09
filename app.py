from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/even-odd', methods=['POST'])
def even_odd():
    num = request.form['num']
    if int(num) % 2 == 0:
        result = 'Even'
    else:
        result = 'Odd'
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
