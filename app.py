from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Python Flask! This is Version 3 – added /health check.'

@app.route('/health')
def health():
    return 'OK - app is healthy'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
