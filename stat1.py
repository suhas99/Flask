from flask import Flask, abort, request
from flask_sqlalchemy import SQLAlchemy
from dbalchemy import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)


@app.route("/suhas/<id>")
@app.route("/suhas/")
def hello(id=None):
    if id is None:
        id = request.args.get('id')
        if id:
            return "your id is " + " " + id
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
