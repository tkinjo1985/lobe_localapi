from image_utils import png2base64
from request_utils import predict_from_base64

url = 'http://localhost:38100/predict/d86112fe-cb1f-401d-8cdf-7c49896c0805'
x = png2base64('cat.102.png')
result = predict_from_base64(x, url)
print(result)
