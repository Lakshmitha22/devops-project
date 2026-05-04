from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return {
        "status": "healthy",
        "message": "DevOps App Running!",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }

@app.route('/health')
def health():
    return {"status": "ok"}, 200

@app.route('/metrics')
def metrics():
    return {
        "app_name": "devops-demo",
        "uptime": "running",
        "requests_processed": 100
    }

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)