import requests
import mysql.connector as mysql
url = "http://127.0.0.1:6000/countries"
while True:
    name = input().title()
    myobj = {
        "name_country" : name
    }
    response = requests.post(url, json = myobj)
    if response.status_code == 201:
        print("The capital of " + name + " is", response.text)
    else:
        print(response.text)
        print("Please provide us with the capital")
        the_capital = input().title()
        mydb = mysql.connect(
            host = "localhost",
            user = "root",
            password = "1234",
            database = "countries"
        )
        mycursor = mydb.cursor()
        code1 = "SELECT name_country FROM capital"
        mycursor.execute(code1)
        results = mycursor.fetchall()
        row_count = len(results)
        code2 = "INSERT INTO capital(id, name_country, capital_country) VALUES(%s, %s, %s)"
        val = (row_count + 1, name, the_capital)
        mycursor = mydb.cursor()
        mycursor.execute(code2, val)
        mydb.commit()
        print("Thank you for providing us")