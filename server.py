from flask import Flask, render_template, redirect, Request

app = Flask(__name__)

counts = 0


@app.route('/')
def home_page():
    return render_template("main.html", counts=counts)


@app.route('/request-counter')
def request_counter():
    global counts
    counts += 1
    return redirect('/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )