import faker
import faker_commerce
from models import Product
from database import session
import time
import random

fake = faker.Faker()
fake.add_provider(faker_commerce.Provider)


def create_product():
    name = fake.ecommerce_name()
    price = fake.ecommerce_price()
    product = Product(name=name, price=price)
    with session:
        session.add(product)
        session.commit()

    choices = [1, 2, 3]
    time.sleep(random.choice(choices))


def main():
    try:
        while True:
            create_product()
    except KeyboardInterrupt:
        print("Script interrupted")


if __name__ == "__main__":
    main()
