from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

about_me = {
"name": "Вадим",
"surname": "Шиховцов",
"email": "vshihovcov@specialist.ru"
}

@app.route("/about")
def about():
    return about_me

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)