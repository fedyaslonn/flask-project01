from flask import Flask, request, render_template, redirect

app = Flask(__name__)

res_dict = []

@app.route('/index')
def index():
    return render_template("main.html", title="Добро пожаловать")


@app.route('/check_color', methods=['GET', 'POST'])
def check_color():
    return render_template("check_colors.html", title='Посмотреть цвета')


@app.route('/return_color', methods=['GET', 'POST'])
def return_color():
    colors = ['зеленый', 'черный', 'красный', 'Зеленый', 'Красный', 'Черный']
    if request.method == 'GET':
        query = request.args.get('query')
        if query in colors:
            res_dict.append(query)
            return render_template("return_color.html", color=query, title='Цвет')
        else:
            return f'Выбранный цвет недоступен'
    elif request.method == 'POST':
        selected_color = request.form.get('selection')
        if selected_color in colors:
            res_dict.append(selected_color)
            return render_template("return_color.html", color=selected_color, title='Цвет')
        else:
            return f'Выбранный цвет недоступен'


@app.route('/history', methods=['GET', 'POST'])
def history():
    colors = ['зеленый', 'черный', 'красный', 'Зеленый', 'Красный', 'Черный']
    if request.method == 'POST':
        if 'clear_history' in request.form:
            res_dict.clear()
            return render_template("colors_history.html", colors=res_dict, title='История просмотров')
    return render_template("colors_history.html", colors=res_dict, title='История просмотров')


if __name__ == '__main__':
    app.run()