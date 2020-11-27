from base64 import b64encode
from io import BytesIO
from PIL import Image
import os


def image2base64(image):
    if os.path.exists(image):
        file_extension = os.path.splitext(os.path.basename(image))[-1]
        if file_extension == '.jpg' or file_extension == '.jpeg' or file_extension == '.png':
            try:
                image = Image.open(image).convert('RGB')
            except Exception as e:
                print(e)
            else:
                buffered = BytesIO()
                image.save(buffered, format="JPEG")
                img_b64 = b64encode(buffered.getvalue())
                return img_b64.decode('utf8')
        else:
            print('Not Image File')
    else:
        print('Image Not Found')
