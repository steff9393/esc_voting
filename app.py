from flask import Flask
from .routes import bp

app = Flask(__name__, template_folder="templates")

app.register_blueprint(bp)

# Definition of starting
if __name__ == "__main__":
    app.run()
