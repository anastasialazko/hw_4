import json
import keyword


class ColorizeMixin:
    repr_color_code = 33  # yellow

    def __repr__(self):
        return f'\033[1;{self.repr_color_code};40m{self.title} | {self.price} ₽'

class Advert(ColorizeMixin):

    def __init__(self, advert: dict):
        for key, value in advert.items():
            if keyword.iskeyword(key):
                key_ = '{}_'.format(key)
                self.__dict__[key_] = value
            elif isinstance(value, dict):
                self.__dict__[key] = Advert(value)
            else:
                self.__dict__[key] = value

    @property
    def price(self):
        if 'price' not in self.__dict__:
            self.__dict__['price'] = 0
        if self.__dict__['price'] < 0:
            raise ValueError('price cannot be negative')
        return self.__dict__['price']


if __name__ == '__main__':
    corgi_str = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs",
    "location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
    }
    }"""
    phone_str = """{
  "title": "iPhone X",
  "location": {
    "address": "город Самара, улица Мориса Тореза, 50",
    "metro_stations": ["Спортивная", "Гагаринская"]
  }
    }"""
    corgi = json.loads(corgi_str)
    phone = json.loads(phone_str)
    corgi_ad = Advert(corgi)
    phone_ad = Advert(phone)

    print(corgi_ad.title)
    print(corgi_ad.class_)
    print(corgi_ad)
    print(phone_ad)
    print(corgi_ad.location.address)
    print(phone_ad.price)

