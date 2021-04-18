from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    number = random.randint(1, 9)
    current_year = datetime.datetime.now().year
    return render_template("index.html", number=number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    url = f"https://api.genderize.io/?name={name}"
    url_response = requests.get(url)
    info = url_response.json()
    gender = info["gender"]
    age_url = f"https://api.agify.io/?name={name}"
    age_url_res = requests.get(age_url)
    age_info = age_url_res.json()
    age = age_info["age"]
    return render_template("guess_nam.html", name=name, age=age, gender=gender)


@app.route('/blogpost/<num>')
def post(num):
    url = requests.get("https://api.npoint.io/a39eb8afe421d9932f84")
    blogs = url.json()
    return render_template("blog.html", all_blog=blogs)


if __name__ == "__main__":
    app.run(debug=True)


