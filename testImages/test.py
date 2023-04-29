import requests

resp = requests.post("http://192.168.10.141:5000", files={'file': open('magnolia.jpg', 'rb')})

print(resp.text)