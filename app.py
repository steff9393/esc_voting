from flask import Flask

app = Flask(__name__, template_folder="templates")


# Definition of starting
if __name__ == "__main__":
    app.run()
