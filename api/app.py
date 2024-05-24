from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/<route>', methods=['POST'])
def index(route):
    if route == 'store':
        data = request.get_json()  
        print(data)
        return jsonify(
            endpoint=route,
            success=True,
            data=data
        )
    else:
        print(f'{route} not found')
        return jsonify(
            endpoint=route,
            success=False
        )

if __name__ == '__main__':
    app.run(debug=True)