## lobe_localapi
How to use Lobe Local API

After Training...

1, [File]-[Export]-[Local API]

2, copy URL(http://localhost:38100/predict/~~~~)

3, Try it with this sample code.

```
from image_utils import png2base64
from request_utils import predict_from_base64

url = 'Lobe LocalAPI URL'
x = png2base64('png file')
result = predict_from_base64(x, url)
print(result)
```
