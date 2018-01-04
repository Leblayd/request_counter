from flask import Flask, render_template, redirect, request
from data_manager import *

app = Flask(__name__)


@app.route('/')
def home_page():
    counts = get_dict_from_file()
    return render_template("main.html", counts=counts)


@app.route('/request-counter', methods=['POST', 'GET', 'PUT', 'DELETE'])
def request_counter():
    counts = get_dict_from_file()
    counts[request.method] += 1
    write_dict_to_file(counts)
    return redirect('/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )