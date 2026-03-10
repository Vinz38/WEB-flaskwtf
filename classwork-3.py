from flask import Flask, render_template


app = Flask(__name__)

@app.route('/list_prof/<sp_type>', methods=['GET'])
def list_prof(sp_type="ERROR"):
    professions = [
        "Инженер-строитель",
        "Пилот",
        "Биолог",
        "Медик",
        "Геолог",
        "Программист"
    ]
    return render_template("base-classwork-3.html", sp_prof = professions, sp_type = sp_type)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')