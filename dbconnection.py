import mysql.connector as mysql

DATABASE_NAME="dockerdb"

config = {
        'user': 'adressbook',
        'password': 'root',
        'host': 'mysqldb',
        'port': '3306',
        'database': DATABASE_NAME
    }

con = mysql.connect(**config)

con.close()

def addPerson(personData):
    personNameResult= isPersonName(personData['name'])
    
    if personNameResult[0]:
        personNameResult[0]=False
        return personNameResult
    elif personNameResult[0] is None:
        return personNameResult

    checkConnection()
    cur = con.cursor()
    try:
        cur.execute("insert into "+DATABASE_NAME+".addressbook (name, address, phone, mobilePhone, email) values ('"+personData['name']+"','"+personData['address']+"',"+str(personData['phone'])+", "+str(personData['mobilePhone'])+",'"+personData['email']+"');")  
        con.commit()
        return [True,""]
    except:
        return [None,"It gives an error while adding it to the database."]
    finally:
        cur.close()
        con.close()

def deletePerson(personName):
    personNameResult= isPersonName(personName)
    
    if not personNameResult[0]:
        return personNameResult
    elif " gives an error" in personNameResult[1]:
        return personNameResult

    checkConnection()
    cur = con.cursor()
    try:
        cur.execute("delete from "+DATABASE_NAME+".addressbook WHERE name='"+personName+"';")  
        con.commit()
        return [True,""]
    except:
        return [False,"It gives an error while adding it to the database."]
    finally:
        cur.close()
        con.close()

def updatePerson(personName,data):
    dbData=getPerson(personName)
    if not dbData[0]:
        return dbData
    elif " gives an error" in dbData[1]:
        return dbData

    tempData = dbData[1].copy()
    k1 = set(tempData.keys())
    k2 = set(data.keys())
    common_keys = set(k1).intersection(set(k2))

    for key in common_keys:
        if tempData[key] != data[key] :
            tempData[key] = data[key]

    checkConnection()
    cur = con.cursor()
    try:
        cur.execute("UPDATE "+DATABASE_NAME+".addressbook SET name='"+tempData['name']+"', address='"+tempData['address']+"', phone="+str(tempData['phone'])+", mobilePhone="+str(tempData['mobilePhone'])+", email='"+tempData['email']+"' WHERE id = "+str(tempData['id'])+";")  
        con.commit()
        return [True,tempData]
    except:
        return [False,"It gives an error while adding it to the database."]
    finally:
        cur.close()
        con.close()

def getPerson(data):
    searchData= {}
    if isinstance(data, int):
        searchData['name']="#####"
        searchData['address']="#####"
        searchData['phone']=data
        searchData['mobilePhone']=data
        searchData['email']="#####"
    else:
        searchData['name']=data
        searchData['address']=data
        searchData['phone']="1111"
        searchData['mobilePhone']="1111"
        searchData['email']=data

    checkConnection()
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM "+DATABASE_NAME+".addressbook where name='"+searchData['name']+"' or address='"+searchData['address']+"' or phone="+str(searchData['phone'])+"  or mobilePhone="+str(searchData['mobilePhone'])+"  or email='"+searchData['email']+"';")
        row = cur.fetchone()
        if row is None:
            return [False,"There is not this person in the database."]
        else:
            currentData ={}
            currentData['id']="Null" if row[0] is None else row[0]
            currentData['name']="Null" if row[1] is None else row[1]
            currentData['address']="Null" if row[2] is None else row[2]
            currentData['phone']="Null" if row[3] is None else row[3]
            currentData['mobilePhone']="Null" if row[4] is None else row[4]
            currentData['email']="Null" if row[5] is None else row[5]
            return [True,currentData]
    except:
        return [False,"It gives an error while adding it to the database."]
    finally:
        cur.close()
        con.close()
    

def isPersonName(personName):
    checkConnection()
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM "+DATABASE_NAME+".addressbook where name='"+personName+"';")
        row = cur.fetchone()
        if row is None:
            return [False,"There is not this person in the database."]
        else:
            return [True,"There is this person in the database."]
    except:
        return [None,"It gives an error while adding it to the database."]
    finally:
        cur.close()
        con.close()

def checkConnection():
    if not con.is_connected():
        con.reconnect()


