from image_utils import png2base64
from request_utils import predict_from_base64

url = 'Lobe LocalAPI URL'
x = png2base64('png file')
result = predict_from_base64(x, url)
print(result)
