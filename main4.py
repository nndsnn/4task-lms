from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Mars Mission')
@app.route('/answer')
@app.route('/auto_answer')
def answer():
    user_data = {
        'title': 'Анкета участника миссии',
        'surname': 'Иванов',
        'name': 'Иван',
        'education': 'Высшее техническое',
        'profession': 'Инженер-исследователь',
        'sex': 'Мужской',
        'motivation': 'Всегда мечтал участвовать в космических исследованиях и вносить вклад в развитие науки',
        'ready': 'Готов к любым испытаниям'
    }
    
    return render_template('auto_answer.html', **user_data)

@app.route('/distribution')
def distribution():
    astronauts = [
        'Ридли Скотт',
        'Энди Уир',
        'Марк Уотни',
        'Венката Капур',
        'Тедди Сандерс',
        'Шон Бин'
    ]
    return render_template('distribution.html', astronauts=astronauts)

if __name__ == '__main__':
    app.run(port=5000)