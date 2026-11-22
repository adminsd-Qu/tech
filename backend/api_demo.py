import requests

resp = requests.get("https://uapis.cn/api/v1/misc/weather?city=济南")
print(resp.json())
