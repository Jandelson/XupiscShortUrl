import redis
import dotenv
import os

dotenv.load_dotenv()
class XupiscRegister:
    __REDIS_HOST = os.getenv("REDIS_HOST", "localhost")

    def __init__(self, redis_host=__REDIS_HOST, redis_port=6379):
        self.redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

    def register_url(self, short_url, original_url, qrcode_url, expiration_time=3600):
        self.redis_client.setex(short_url, expiration_time, original_url)
        self.redis_client.setex(f"{short_url}_qrcode", expiration_time, qrcode_url)

    def get_original_url(self, short_url):
        return self.redis_client.get(short_url)

    def get_qrcode_url(self, short_url):
        return self.redis_client.get(f"{short_url}_qrcode")

    def delete_url(self, short_url):
        self.redis_client.delete(short_url)
        self.redis_client.delete(f"{short_url}_qrcode")

    def url_exists(self, short_url):
        return self.redis_client.exists(short_url) > 0