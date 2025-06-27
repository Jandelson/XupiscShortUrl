import qrcode
import hashlib
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from services.XupiscShort import XupiscShort

class XupiscQrcode:
    __QRCODE_PATH = "qrcode/"

    def __init__(self, shortner: XupiscShort):
        self._shortner = shortner
        self._size = 1
        self.__error_correction = qrcode.constants.ERROR_CORRECT_L
        self._box_size = 10
        self._border = 4

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value: int):
        if value < 1 or value > 40:
            raise ValueError("Version must be between 1 and 40.")
        self._size = value

    @property
    def box_size(self):
        return self._size

    @box_size.setter
    def box_size(self, value: int):
        if value < 10 or value > 40:
            raise ValueError("Version must be between 10 and 40.")
        self._box_size = value

    def generate_qrcode(self):
        qr = qrcode.QRCode(
            version=self._size,
            error_correction=self.__error_correction,
            box_size=self._box_size,
            border=self._border
        )

        qr.add_data(self._shortner.short_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        imagename = datetime.now().strftime("%Y%m%d%H%M%S") + "_" + hashlib.md5(self._shortner.short_url.encode()).hexdigest()[:6]
        img = img.convert("RGB")
        img.save(f"{self.__QRCODE_PATH+imagename}.png")

        return f"{self._shortner.BASE_URL+self.__QRCODE_PATH+imagename}.png"