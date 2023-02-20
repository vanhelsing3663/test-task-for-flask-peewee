from flask import Flask, render_template, request, make_response

app = Flask(__name__)
from models import Data


@app.route('/')
def index():
    return render_template('input.html')


@app.route('/submit', methods=['POST'])
def submit():
    id_list = [user.id for user in Data.select()]

    try:
        user_id = int(request.form['id'])
        if user_id in id_list:
            all = Data.select(Data).where(Data.id == int(user_id)).get()
            return render_template('out.html', name=all.name, age=all.age)
    except (ValueError):
        return make_response('<h2>Вы ввели не верные данные</h2>', 404)


if __name__ == '__main__':
    app.run(debug=True)
