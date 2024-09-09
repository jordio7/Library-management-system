import mysql.connector

def myconnections():
    con = mysql.connector.connect(user='root', password='qwerty', host='localhost')
    mycursor = con.cursor()
    mycursor.execute("USE signup")
    return con,mycursor
#myconnections()
