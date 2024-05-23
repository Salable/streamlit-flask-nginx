from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/api/time', methods=['GET'])
def get_time():
    current_time = int(time.time())
    return jsonify(status="ok", timestamp=current_time)

if __name__ == '__main__':
    app.run(debug=True)