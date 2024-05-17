import mysql.connector as mysql

mydb = mysql.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "countries"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM capital")
myresult = mycursor.fetchall()
table_countries = list()
for x in myresult:
    d = dict()
    d['id'] = x[0]
    d['name_country'] = x[1].title()
    d['capital_country'] = x[2].title()
    table_countries.append(d)

class Application:
    def __init__(self):
        self.countries = table_countries
    def find(self, tmp):
        for _countries in self.countries:
            if _countries["name_country"] == tmp:
                return _countries["capital_country"], 201
        return {"WARNING" : "Not Found this country"}, 202