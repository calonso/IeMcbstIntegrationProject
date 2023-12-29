from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/getStockInfo', methods=['GET'])
def get_stock_info():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)
