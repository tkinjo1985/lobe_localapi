from image_utils import image2base64
from request_utils import predict_from_base64

#
url = 'http://localhost:38100/predict/xxxxx'
x = image2base64('cat.102.png')
if x is not None:
    result = predict_from_base64(x, url)
    print(result)
