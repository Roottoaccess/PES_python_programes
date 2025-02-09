from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"

# Pages (route)
@app.route("/")
def hello_world():
    # return "<h2><p>Hello, World!</p><h2>"
    return render_template('index.html')

# Just creating another route
@app.route("/products")
def products():
    return "this is the product page"

if __name__ == "__main__":
    app.run(debug=True, port = 8000)