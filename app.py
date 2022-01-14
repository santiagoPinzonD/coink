from flask import Flask, render_template, request, jsonify
from Models import User, db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from logging import exception
import logging


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/user.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/users")
def users():
    users = User.query.all()
    users_serialized = [user.serialize() for user in users]
    return render_template('users.html', users=users_serialized)


@app.route("/api/adduser", methods=["POST"])
def add_user():
    try:
        name = request.form["name"]
        email = request.form["email"]
        city = request.form["city"]
        user = User(name, email, city)
        db.session.add(user)
        db.session.commit()

        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
            style='{',
            filename='logs.log',
            filemode='w')
        logging.info("Event of creation of  user")

        return jsonify(user.serialize()), 200
    except Exception:
        exception("error in creation of user")
        return jsonify({"msg": "Error in creation of user"}), 500


if __name__ == "__main__":
    """ Main Function """

    app.run(host='0.0.0.0', port=5000)
