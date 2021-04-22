from flask import Flask ,request , make_response, jsonify
import dbconnection as db
import re

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
  #  db.createSchema()
    return response_success(None,200)


@app.route("/addPerson" , methods = ["POST"])
def addPerson():
    data=request.get_json()

    if data is None:
        return response_error("There is not the json in the body!",400)

    resultCheck= check_addPerson(data)
    if resultCheck[0]:
       return response_error(resultCheck[1],400)

    dbResult= db.addPerson(data)
    if not dbResult[0]:
        return response_error(dbResult[1],400)
    return response_success(None,201)

@app.route("/deletePerson/<string:name>", methods = ["DELETE"])
def deletePerson(name):

    resultCheckName = check_name(name)
    if resultCheckName[0]:
       return resultCheckName

    dbResult= db.deletePerson(name)
    if not dbResult[0]:
        return response_error(dbResult[1],400) 
   
    return response_success(name+" is deleted",200)

@app.route("/updatePerson/<string:name>", methods = ["PUT"])
def updatePerson(name):

    data=request.get_json()

    if data is None:
        return response_error("There is not the json in the body!",400)

    resultCheck= check_updatePerson(data)
    if resultCheck[0]:
       return response_error(resultCheck[1],400)

    dbResult= db.updatePerson(name,data)
    if not dbResult[0]:
        return response_error(dbResult[1],400) 
   
    return response_success(None,204)


@app.route("/getPerson/<string:data>", methods = ["GET"])
def getPerson(data):

    dbResult= db.getPerson(data)
    if not dbResult[0]:
        return response_error(dbResult[1],400) 
   
    return response_success(dbResult[1],200)

def check_addPerson(data):
    resultCheckData= check_request_data(data)
    if resultCheckData[0]:
       return  resultCheckData

    resultCheckName = check_name(data['name'])
    if resultCheckName[0]:
       return resultCheckName

    if 'email' in data:
        resultCheckName = check_email(data['email'])
        if resultCheckName[0]:
            return resultCheckName
    else :
        data['email']='Null'

    return [False,""]

def check_updatePerson(data):
    if 'name' in data:
        resultCheckName = check_name(data['name'])
        if resultCheckName[0]:
            return resultCheckName

    if 'email' in data:
        resultCheckName = check_email(data['email'])
        if resultCheckName[0]:
            return resultCheckName

    return [False,""]

def check_request_data(data):
    message ="'"
    isError =False
    if not 'name' in data:
        message += "name, "
        isError =True

    if not 'address' in data:
        message += "address, "
        isError =True

    if not (('phone' in data) or ('mobilePhone' in data)) :
        message += "phone(or mobilePhone), "
        isError =True
    elif not 'phone' in data:
        data['phone'] ='Null'
    elif not 'mobilePhone' in data:
        data['mobilePhone'] ='Null'
    
    if isError:
        message = message[:-2] + "' request öğeleri boş bırakılamaz!"
    return [isError,message]

def check_name(name):
  #  '([A-Z][a-z][a-z]*)  *([A-Z][a-z]*)\\.?  *([A-Z][a-z][a-z][a-z]*)'
  # '[A-Za-z]{2,25}( [A-Za-z]{2,25})?( [A-Za-z]{2,25})?'
    message =""
    isError =False
    if not re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?( [A-Za-z]{2,25})?', name):
        message += "'name' is invalid!"
        isError =True
    
    return [isError,message]

def check_email(email):
  # '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    message =""
    isError =False
    if not re.fullmatch('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email):
        message += "'email' is invalid!"
        isError =True
    
    return [isError,message]

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
    app.run(debug=True)