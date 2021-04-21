from flask import Flask
import dbconnection as db

app = Flask(__name__)

@app.route("/")
def index():
   # db.addUser()
    return "Anasayfa"

if __name__ == "__main__":
    app.run(debug=True)