from flask import Flask
import routes

app = Flask(__name__, template_folder="templates")

app.add_url_rule('/', view_func=routes.run)
app.add_url_rule('/vote', view_func=routes.save_vote)
app.add_url_rule('/delete/<int:id>', view_func=routes.del_vote)
app.add_url_rule('/update/<int:id>', view_func=routes.update_vote)

# Definition of starting
if __name__ == "__main__":
    app.run()
