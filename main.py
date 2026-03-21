from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Mars Mission')

@app.route('/index/<title>')
def index_with_title(title):
    return render_template('base.html', title=title)



@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    PROFESSIONS = [
    'Инженер-конструктор',
    'Строитель',
    'Биолог',
    'Геолог',
    'Физик',
    'Химик',
    'Врач',
    'Психолог',
    'Программист',
    'Робототехник'
]

    return render_template('list_prof.html', 
                         title='Список профессий',
                         professions=PROFESSIONS,
                         list_type=list_type)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')