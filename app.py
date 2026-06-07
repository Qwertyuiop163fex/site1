from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

POSTS = [
    {
        "id": 1,
        "title": "Добро пожаловать на мой сайт",
        "body": "Это первая запись. Сайт работает на Flask — минималистичном Python-фреймворке.",
        "date": "2026-06-01",
    },
    {
        "id": 2,
        "title": "Почему Flask?",
        "body": "Flask не навязывает структуру проекта, легко расширяется и отлично подходит для небольших сервисов.",
        "date": "2026-06-05",
    },
    {
        "id": 3,
        "title": "Следующий шаг",
        "body": "Можно подключить базу данных, добавить авторизацию или развернуть через Docker на Raspberry Pi.",
        "date": "2026-06-07",
    },
]


@app.route("/")
def index():
    return render_template("index.html", posts=POSTS)


@app.route("/post/<int:post_id>")
def post(post_id):
    p = next((p for p in POSTS if p["id"] == post_id), None)
    if not p:
        return "Запись не найдена", 404
    return render_template("post.html", post=p)


@app.route("/api/time")
def api_time():
    return jsonify({"time": datetime.now().strftime("%H:%M:%S")})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
