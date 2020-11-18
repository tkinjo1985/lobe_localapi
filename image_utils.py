from base64 import b64encode
from io import BytesIO
from PIL import Image


def png2base64(image):
    image = Image.open(image).convert('RGB')
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_b64 = b64encode(buffered.getvalue())
    return img_b64.decode('utf8')
