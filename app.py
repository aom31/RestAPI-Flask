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