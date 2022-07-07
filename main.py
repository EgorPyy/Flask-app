from flask import Flask, request
import json

with open('d:/data.json', 'r') as f:
    try:
        list = json.load(f)
    except ValueError:
        list = []
app = Flask(__name__)


@app.route('/')
def first_page():
    return """<html>
                <body>
                    <section>
                        <h2>Задонатить</h2>
                            <p>
                                <form action="/request/donate", method="post">
                                <input name = "name" type = text placeholder = "Введите вещь">
                                <input name = "amount" type = number placeholder = "Введите количество">
                                <button type="submit">Отправить</button>
                                </form>
                            </p>
                    </section>
                    <section>
                        <h2>Попросить вещь</h2>
                            <p>
                                <form action="/request/take", method="get">
                                <input name = "take" type = "text" placeholder = "what">
                                <button type="submit">Отправить</button>
                                </form>
                            </p>
                    </section>
                </body>
            </html>"""


@app.route('/request/donate', methods=['POST'])
def donate():
    name = request.form['name']
    amount = int(request.form['amount'])
    user_dict = dict(name=name, amount=amount)
    list.append(user_dict)
    with open('d:/data.json', 'w') as f:
        json.dump(list, f)
    return f"""<html>
                    <body>
                        <section>
                            <h2>Спасибо</h2>
                                <a href='/'>Вернуться на главную</a>
                        </section>
                    </body>
                </html>"""


@app.route('/request/take', methods=['GET'])
def take_thing():
    take = request.args.get('take')
    for i in list:
        if i['name'] == take:
            last_number = i.get('amount')
            if last_number > 1:
                i.update(amount=last_number - 1)
            else:
                list.remove(i)
            with open('d:/data.json', 'w') as f:
                json.dump(list, f)
            return f'Вот вам {take}'
    else:
        return f"""<html>
                    <body>
                        <section>
                            <h2>Извините,у нас нету {take}</h2>
                                <a href='/'>Вернуться на главную</a>
                        </section>
                    </body>
                </html>"""


if __name__ == '__main__':
    app.run(debug=True)

