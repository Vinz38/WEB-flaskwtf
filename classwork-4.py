from flask import Flask, render_template


app = Flask(__name__)

@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    survey = {
        'answers': 
        {
        'Фамилия': 'Иванов',
        'Имя': 'Иван',
        'Образование': 'высшее',
        'Профессия': 'инженер',
        'Пол': 'мужской',
        'Мотивация': 'Хочу исследовать Марс',
        'Готовы остаться на Марсе?': 'Да'
        }
    }
    return render_template('auto_answer--4class--.html', **survey)
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')