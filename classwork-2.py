from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/training/<prof>')
def training(prof):
    return render_template('base-classwork-2.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')