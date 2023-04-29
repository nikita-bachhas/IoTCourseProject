import requests

resp = requests.post("http://192.168.10.141:8000", files={'file': open('/Users/nikitabachhas/IoTCourseProject/IoTCourseProject/TestImages/water_lily.jpg', 'rb')})

print(resp.text)