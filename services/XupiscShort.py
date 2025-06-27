import hashlib

class XupiscShort:
    __BASE_URL = "http://localhost:8086/"

    def __init__(self, url:str):
        self.__url = url
        self.__short_url = None

    @property
    def BASE_URL(self):
        return self.__BASE_URL

    @property
    def short_url(self):
        return self.__short_url

    def generate_short_url(self):
        if not self.__url:
            raise ValueError("URL cannot be empty.")
        if not self.__url.startswith("http://") and not self.__url.startswith("https://"):
            raise ValueError("A URL deve começar com 'http://' ou 'https://'.")

        hash_object = hashlib.md5(self.__url.encode())
        self.__short_url = self.__BASE_URL + hash_object.hexdigest()[:6]