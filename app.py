from flask import Flask, render_template, request, redirect, url_for,session,make_response
from routes.auth import auth


app = Flask(__name__)

app.register_blueprint(auth)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)