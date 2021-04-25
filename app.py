from flask import Flask ,request , make_response, jsonify
import re
import dbconnection as db
import utils

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():

    return response_success(None,200)

@app.route("/createDB", methods = ["GET","POST"])
def createDB():
    db.createSchema()
    return response_success(None,200)

@app.route("/address-books" , methods = ["POST"])
def addAddressbooks():
    data=request.get_json()

    if data is None:
        return response_error("There is not the json in the body!",400)

    resultCheck= utils.check_addPerson(data)
    if resultCheck[0]:
       return response_error(resultCheck[1],400)

    dbResult= db.addPerson(data)
    if not dbResult[0]:
        return response_error(dbResult[1],400)
    return response_success(None,201)

@app.route("/address-books/<string:name>", methods = ["DELETE"])
def deleteAddressbooks(name):

    resultCheckName = utils.check_name(name)
    if resultCheckName[0]:
       return resultCheckName

    dbResult= db.deletePerson(name)
    if not dbResult[0]:
        return response_error(dbResult[1],400) 
   
    return response_success(name+" is deleted",200)

@app.route("/address-books/<string:name>", methods = ["PUT"])
def updateAddresbooks(name):

    data=request.get_json()

    if data is None:
        return response_error("There is not the json in the body!",400)

    resultCheck= utils.check_updatePerson(data)
    if resultCheck[0]:
       return response_error(resultCheck[1],400)

    dbResult= db.updatePerson(name,data)
    if not dbResult[0]:
        return response_error(dbResult[1],400) 
   
    return response_success(None,204)

@app.route("/address-books/<string:data>", methods = ["GET"])
def getAddressbooks(data):

    dbResult= db.getPerson(data)
    if not dbResult[0]:
        return response_error(dbResult[1],400) 
   
    return response_success(dbResult[1],200)

def response_error(message, status_code): 
    if " gives an error" in message:
        status_code=500
    message = {'errorCode': status_code, 'errorMessage': message}
    return make_response(jsonify(message), status_code)

def response_success(message, status_code): 
    if None is not  message:
        message = {'succesCode': status_code, 'data': message}
    return make_response(jsonify(message), status_code)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)