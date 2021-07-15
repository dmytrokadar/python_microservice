import json
import mysql.connector
import requests
from OffersGetter import OffersGetter

LINK = "https://applifting-python-excercise-ms.herokuapp.com/api/v1"

# inspiration https://dzone.com/articles/python-rest-api-example-part-1
class Products:
    def __init__(self):
        response = requests.post(LINK+'/auth')
        self.access_token = response.json()["access_token"]

        self.offers_getter = OffersGetter(self.access_token)

        self.database = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="****",
            database="mydatabase"
        )

        self.cursor = self.database.cursor()

    def add_product(self, id, name=None, description=None):
        print(id,name,description)
        self.cursor.execute(f'INSERT INTO products (id, name, description) VALUES ({id}, {name}, {description})')
        self.database.commit()
        self.offers_getter.add_product_id(id)

        requests.post(LINK+"/products/register", headers={"Bearer": self.access_token}, data={
            "id": id,
            "name": name,
            "description": description
        })

    def del_product(self, **kwargs):
        for key, value in kwargs.items():
            self.cursor.execute(f'DELETE FROM products WHERE {key} = "{value}"')
        self.database.commit()

    def update_product(self, **kwargs):
        items = dict(kwargs.items())
        self.cursor.execute(f'UPDATE products SET name = "{items["name"]}", description = "{items["description"]}" WHERE id = "{items["id"]}"')
        self.database.commit()

    def get_products(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def get_products_json(self):
        self.cursor.execute("SELECT * FROM products")
        print("products geted")
        return json.dumps(self.cursor.fetchall(), sort_keys=True, indent=4, separators=(',', ': '))

    def get_offers_json(self):
        print()
        return self.offers_getter.get_offers()


if __name__ == "__main__":
    p = Products()

    # p.add_product("0000123123", "test product", "test product test product")
    # p.add_product("12323", "banana", "banana)")
    p.add_product('"5543"','"1122"','"hbdshsdhba"')

    # p.del_product(id="{id}")

    # p.update_product(id="123", name="ban", description="odssfmdsomfmsd")

    print(p.get_products_json())
    print(p.get_offers_json())

    while True:
        res = input()
        if res == "add":
            p.add_product('"5543"','"1122"','"hbdshsdhba"')
        elif res == "get":
            print(p.get_offers_json())

    # print(p.get_products())