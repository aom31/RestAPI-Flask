from crypt import methods
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import json
import mysql.connector

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False         #result by ascii convert can show thai language
CORS(app)
host = "localhost"
user= "root"
password= ""
db = "flaskapi"

@app.route("/attractions/read")
def read():
    mydb = mysql.connector.connect(host=host, user = user, password=password, db=db)  #connrct database 
    mycursor = mydb.cursor(dictionary=True)                             #point data to dict for easy {json}
    mycursor.execute("SELECT * FROM attractions ")                      #use command sql
    myresult = mycursor.fetchall()                                      #get result with dictionary
    
    return make_response(jsonify(myresult), 200)                        #send data result on webpage

@app.route("/attractions/read/<id>")
def readbyid(id):
    mydb = mysql.connector.connect(host=host, user = user, password=password, db=db)  #connrct database 
    mycursor = mydb.cursor(dictionary=True)                             #point data to dict for easy {json}
    sql = "SELECT *FROM attractions WHERE id = %s"
    val = (id, )
    mycursor.execute(sql, val)              #map id to %s 
    
    myresult = mycursor.fetchall()                                      #get result with dictionary
    
    return make_response(jsonify(myresult), 200)                        #send data result on webpage


@app.route("/attractions/create", methods = ['POST'])
def create():
    data = request.get_json()
    mydb = mysql.connector.connect(host=host, user = user, password=password, db=db)  #connrct database 
    mycursor = mydb.cursor(dictionary=True)
    sql = "INSERT INTO  attractions (name,  detail) VALUES (%s , %s)"
    val = (data['name'], data['detail'] )
    mycursor.execute(sql, val)  
    mydb.commit()
    
    return make_response(jsonify({ " rowcount": mycursor.rowcount }), 200)

@app.route("/attractions/update/<id>", methods = ['PUT'])
def update(id):
    data = request.get_json()
    mydb = mysql.connector.connect(host=host, user = user, password=password, db=db)  #connrct database 
    mycursor = mydb.cursor(dictionary=True)
    sql = "UPDATE attractions SET name= %s, detail =%s WHERE id = %s"
    val = (data['name'], data['detail'] )
    mycursor.execute(sql, val)  
    mydb.commit()
    
    return make_response(jsonify({ " rowcount": mycursor.rowcount }), 200)

@app.route("/attractions/delete/<id>", methods = ['DELETE'])
def delete(id):
  
    mydb = mysql.connector.connect(host=host, user = user, password=password, db=db)  #connrct database 
    mycursor = mydb.cursor(dictionary=True)
    sql = "DELETE FROM attractions WHERE id =%id"
    val = (id,  )
    mycursor.execute(sql, val)  
    mydb.commit()
    
    return make_response(jsonify({ " rowcount": mycursor.rowcount }), 200)