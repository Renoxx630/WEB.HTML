from flask import request, url_for, Flask

app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='style.css')}"/>
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета претендента на участие в миссии</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите фамилию" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите имя" name="password">
                                    <div style="padding: 20px 0px 0px 0px;">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    </div>
                                    <div class="form-group" style="padding: 20px 0px 0px 0px;">
                                    
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>начальное</option>
                                          <option>среднее</option>
                                          <option>высшее</option>                                          
                                        </select>
                                     </div>
                                     <p style="padding: 20px 0px 0px 0px;">Какие у Вас профессии?</p>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
                                          <label class="form-check-label" for="defaultCheck1">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="defaultCheck2">
                                          <label class="form-check-label" for="defaultCheck2">
                                            Пилот
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked">
                                          <label class="form-check-label" for="flexCheckChecked">
                                            Строитель
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked1">
                                          <label class="form-check-label" for="flexCheckChecked1">
                                            Экзобиолог
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked2">
                                          <label class="form-check-label" for="flexCheckChecked2">
                                            Врач
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked3">
                                          <label class="form-check-label" for="flexCheckChecked3">
                                          Инженер по терраформированию
                                          </label>
                                     </div>
                                     <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
