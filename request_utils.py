import requests
import json


def predict_from_base64(image_base64, url):
    data = {'inputs': {'Image': image_base64}}
    r = requests.post(url, data=json.dumps(data))
    label = json.loads(r.text)['outputs']
    return label
