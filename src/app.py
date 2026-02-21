from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')

def details():
#    return '<h1>Hello World</h1>'
    return jsonify({
        'message': 'hello_new_world',
        'hostname': socket.gethostname(),
        'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'real_hostname': 'newserver'
    })

@app.route('/api/v1/health')

def health():
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0")


# '/api/v1/details'
# '/api/v1/healthz'
# 'message': 'hello_world' - change to 'hello_new_world'