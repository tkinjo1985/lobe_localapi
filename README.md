## How to use Lobe Local API

After Training...

1, [File]-[Export]-[Local API]

2, copy URL(http://localhost:38100/predict/xxxx)

3, Try it with this sample code.

```
from image_utils import image2base64
from request_utils import predict_from_base64

url = 'Lobe LocalAPI URL'
x = image2base64('image file(jpeg or jpg or png)')
result = predict_from_base64(x, url)
print(result)
```
