import tornado.web
import Product
import json
from abc import ABC


# inspiration https://dzone.com/articles/python-rest-api-example-part-3
class HandlerInit(tornado.web.RequestHandler, ABC):
    def initialize(self, products):
        self.set_header("Content-Type", "application/json")
        self.products = products


class CreateHandler(HandlerInit, ABC):
    def get(self):
        id = self.get_argument('id')
        name = self.get_argument('name')
        description = self.get_argument('description')
        self.products.add_product(id, name, description)
        self.content_type = 'application/json'
        print("hoba")
        self.set_header("id", id)
        self.set_status(201)


class ReadHandler(HandlerInit, ABC):
    def get(self):
        self.set_header("Content-Type", "application/json")
        self.write(self.products.get_products_json())
        self.set_status(200)


class ReadOffersHandler(HandlerInit, ABC):
    def get(self):
        self.set_header("Content-Type", "application/json")
        self.write(self.products.get_offers_json())
        self.set_status(200)


class UpdateHandler(HandlerInit, ABC):
    def get(self):
        id = self.get_argument('id')
        name = self.get_argument('name')
        description = self.get_argument('description')
        result = self.products.update_product(id, name, description)
        if result:
            self.write(f"Updated product id: {id}, succsessfully")
            self.set_status(200)


class DeleteHandler(HandlerInit, ABC):
    def get(self):
        id = self.get_argument('id')
        result = self.products.del_product_by_id(id)
        if result:
            self.write(f"Deleted product id: {id}, succsessfully")
            self.set_status(200)
        else:
            self.write(f"Product with id {id} is not found")
            self.set_status(404)
