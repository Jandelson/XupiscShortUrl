import hashlib
import dotenv
import os

dotenv.load_dotenv()
class XupiscShort:
    _HOST = os.getenv("APPLICATION_HOST", "localhost")
    _PORT = os.getenv("APPLICATION_PORT", "8086")
    _BASE_URL = f"http://{_HOST}:{_PORT}/"

    def __init__(self, url:str):
        self.__url = url
        self.__short_url = None

    @property
    def BASE_URL(self):
        return self._BASE_URL

    @property
    def short_url(self):
        return self.__short_url

    def generate_short_url(self):
        if not self.__url:
            raise ValueError("URL cannot be empty.")
        if not self.__url.startswith("http://") and not self.__url.startswith("https://"):
            raise ValueError("A URL deve começar com 'http://' ou 'https://'.")

        hash_object = hashlib.md5(self.__url.encode())
        self.__short_url = self._BASE_URL + hash_object.hexdigest()[:6]