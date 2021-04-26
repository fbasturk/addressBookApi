from flask import Flask ,request , make_response, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import re
import os
import dbconnection as db
import utils

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/documentapi.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Adressbook Api"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route("/", methods = ["GET","POST"])
def index():
    return response_success([True,"Connection Address Book API"],200)

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
   
    return response_success(name+" is deleted",204)

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
   
    return response_success(dbResult[1],200)

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
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=False)