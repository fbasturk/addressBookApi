from flask import Flask
import dbconnection as db

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    return "Anasayfa"


@app.route("/addPerson" , methods = ["POST"])
def addPerson():
   # db.addUser()
    return "Anasayfa"


@app.route("/deletePerson/<string:name>", methods = ["DELETE"])
def deletePerson(name):
   
    return "Anasayfa"


@app.route("/updatePerson/<string:name>", methods = ["PUT"])
def updatePerson():
   
    return "Anasayfa"


@app.route("/searchPerson", methods = ["GET"])
def searchPerson():
   
    return "Anasayfa"

if __name__ == "__main__":
    app.run(debug=True)