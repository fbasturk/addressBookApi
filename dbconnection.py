import mysql.connector as mysql

con = mysql.connect(user='root', password='root',
                host='127.0.0.1',database='TestDB')

con.close()

def createSchema():
    checkConnection()
    cur = con.cursor()
    try:
        cur.execute("create database TestDB")
        cur.execute("create table ")
    except:
        con.rollback()
    cur.close()

def addUser():
    checkConnection()
    cur = con.cursor()
    try:
        cur.execute("insert into deneme (aa, bb, cc) values ('Bill','Gates','test')")  
        con.commit()
    except:
        con.rollback()
    cur.close()
    con.close()

def checkConnection():
    if not con.is_connected():
        con.reconnect()


