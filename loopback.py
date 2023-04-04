from flask import Flask, request
import re

app = Flask(__name__)

# Get your own IP address
def get_own_ip():
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

# Handle all requests on all ports and routes
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
def handle_all(path):
    headers = dict(request.headers)
    data = request.get_data()
    
    # Replace IP addresses with your own IP address in headers and data
    own_ip = get_own_ip()
    for key in headers:
        headers[key] = re.sub(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', own_ip, headers[key])
    data = re.sub(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', own_ip, data.decode())
    
    response = {
        'headers': headers,
        'data': data,
        'pom=d-input': "https://www.youtube.com/watch?v=kVjrSKPCq_A"
    }
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=0)
