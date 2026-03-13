from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/table_param/<sex>/<age>')
def index(sex, age):
    return render_template('base-homework-2.html', sex=sex, age=int(age))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

