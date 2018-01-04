from flask import Flask, render_template, redirect, request

app = Flask(__name__)

counts = {'GET': 0, 'POST': 0, 'PUT': 0, 'DELETE': 0}


@app.route('/')
def home_page():
    return render_template("main.html", counts=counts)


@app.route('/request-counter', methods=['POST', 'GET', 'PUT', 'DELETE'])
def request_counter():
    global counts
    counts[request.method] += 1
    return redirect('/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )