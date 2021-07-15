import requests
import json
import threading
from time import sleep

LINK = "https://applifting-python-excercise-ms.herokuapp.com/api/v1"


class OffersGetter:
    def __init__(self, token, interval=60):
        self.offers = {}
        self.token = token
        self.ids = []
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def add_product_id(self, id):
        self.ids += [id]

    def get_offers(self):
        return self.offers

    def run(self):
        while True:
            response = []
            for id in self.ids:
                response += requests.get(LINK+f"/products/{id}/offers", headers={"Bearer": self.token}).json()
                print(response)
            self.offers = json.dumps(response, sort_keys=True, indent=4)
            print("offers getted")
            sleep(self.interval)


if __name__ == "__main__":
    og = OffersGetter("e81ef14b-ae30-42ac-8b2c-15ff557771d1", 1)
    og.get_offers("1")