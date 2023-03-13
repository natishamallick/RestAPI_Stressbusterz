from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

@app.route('/')
def hello():
	return('<h1> Hello World! </h1>')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 5000)

