import tornado.ioloop
import tornado.web
from Product import Products
from Handlers import *


products = Products()
port = 5555


class MainHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.write("Products holder")


def run_service():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/add_product", CreateHandler, dict(products=products)),
        (r"/v1/get_products", ReadHandler, dict(products=products)),
        (r"/v1/get_product_offers", ReadOffersHandler, dict(products=products)),
        (r"/v1/update_product", UpdateHandler, dict(products=products)),
        (r"/v1/delete_product", DeleteHandler, dict(products=products)),
        ])


def start():
    service = run_service()
    service.listen(port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    start()
