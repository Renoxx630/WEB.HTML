from flask import Flask, url_for

app = Flask(__name__)
@app.route('/')
def marce():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/image_sample')
def image():
    return f'''<h1>Жди нас, Марс!</h1><img src="{url_for('static', filename='Mars.jpg')}"\
    alt="здесь должна была быть картинка, но не нашлась"><p>Вот она, красная планета</p>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')