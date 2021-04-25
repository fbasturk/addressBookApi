import re

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
