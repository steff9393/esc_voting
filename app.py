from flask import Flask, render_template
from . import routes

app = Flask(__name__, template_folder="templates")


# Main route. Welcome Screen with formular
@app.route("/")
def run():
    return render_template("index.html")


# Definition of starting
if __name__ == "__main__":
    app.run()
