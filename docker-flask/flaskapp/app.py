from flask import Flask, render_template, request, redirect, session, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "SecretKeyGoesHere" #can generate using os.urandom(24)

# db config, for help see https://docs.sqlalchemy.org/en/14/dialects/index.html
app.config['SQLALCHEMY_DATABASE_URI'] = "data base url goes here" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# database schema is example code, change to meet your schema requirements
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)


# index page
@app.route('/', methods=['POST', 'GET'])
def index():
    title = "Webapp Template"
    return render_template('index.html',title=title)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)