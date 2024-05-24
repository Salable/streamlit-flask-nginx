from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/<route>', methods=['POST', 'GET'])
def index(route):
    if route == 'echo':
        data = request.get_json()  
        print(data)
        return jsonify(
            endpoint=route,
            success=True,
            data=data
        )
    if route == 'name':
        return jsonify(
            endpoint=route,
            success=True,
            data={'name': 'John Doe'}
        )
    else:
        print(f'{route} not found')
        return jsonify(
            endpoint=route,
            success=False
        )

if __name__ == '__main__':
    app.run(debug=True)