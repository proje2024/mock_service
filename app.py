from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = [
        {
            'id': 1,
            'hiyerid': 1,
            'ataid': 0,
            'adi': 'CEO'
        },
        {
            'id': 2,
            'hiyerid': 2,
            'ataid': 1,
            'adi': 'CTO'
        }
    ]
    
    # id=1 olan kaydın ataid değerini None olarak güncelle
    for item in data:
        if item['id'] == 1:
            item['ataid'] = None

    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
