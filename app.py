from flask import Flask,jsonify

app=Flask(__name__)

data ={
    "name": "john Doe",
    "age" : 30,
    "city": "New York"
}

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ =='__main__':
    app.run(debug=True)
