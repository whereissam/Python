from flask import Flask
app = Flask(__name__)

# print(app)

def make_center(function):
    def center():
        return f"<h1 style='text-align: center'> {function()} </h1>"

    return center
@app.route('/')
@make_center
def hello_world():
    return 'Hello, World!' \
           '<p> This is paragraph </p>' \
           '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8qY-fjzbU3eY60grVgnkK7ZuHp8PQNmy9lg&usqp=CAU">'


@app.route('/3')
def three():
    return 'This is three'

@app.route('/users/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/sam')
def sam():
    return f"Serverless architecture management"

@app.route('/username/<name>/<int:id>')
def greet_user(name, id):
    return f"Hello {name} {id}"

if __name__ == "__main__":
    #run in debug mode to auto reload
    app.run(debug=True)

# run flask
# 1.set FLASK_APP=main.py
# 2.flask run
