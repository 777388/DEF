from flask import Flask, request

app = Flask(__name__)

# Handle all requests on all ports and routes
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
@app.route('/<path:path', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
def handle_all(path):
    headers = dict(request.headers)
    data = request.get_data()
    response = {
        'headers': headers,
        'data': data.decode()
        'pom=d-input': "https://www.youtube.com/watch?v=kVjrSKPCq_A"
    }
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=0)
