import mysql.connector
import requests
import json

def print_JSON(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DePult",
    database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("create table products (id varchar(255), name varchar(255), description varchar(255))"

# command = "INSERT INTO products (id, name, description) VALUES (%s, %s, %s)"
# var = ("1", "name", "first product")
# mycursor.execute("INSERT INTO products (id, name, description) VALUES (%s, %s, %s)", ("1", "name", "first product"))
# mydb.commit()

# mycursor.execute("SHOW products")

# for x in mycursor:
#     print(x)

link ="https://applifting-python-excercise-ms.herokuapp.com/api/v1/"


# response = requests.post('https://applifting-python-excercise-ms.herokuapp.com/api/v1/auth')
response = requests.get(link+"/products/0000123123/offers", headers={"Bearer": "7a300824-fe95-4308-b482-83a8203f12dd"})

print(response.status_code)
# print(response.json()["access_token"])

if 'json' in response.headers.get('Content-Type'):
    print_JSON(response.json())
else:
    print('Response content is not in JSON format.')
    print(response)

# items = {
#     "id": "1",
#     "name": "kek",
#     "description": "hoba"
# }
#
# print(f'Name = {items["name"]}, description = {items["description"]} Where Id = {items["id"]}')




