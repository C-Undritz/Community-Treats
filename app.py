import os
from flask import Flask
if os.path.exists("env.py"):
    import env


# Creates an instance of Flask stored in variable 'app'.
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World... again!"


# Tells the app how and where to run application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) # ****UPDATE TO "debug=False" PRIOR TO PROJECT SUBMISSION****


