import requests


url = "https://www.superheroapi.com/api"
method = "/search/{}"
token = "/2619421814940190"

heros = ['Hulk', 'Captain America', 'Thanos']
res_list = []
rang_list = []

for name in heros:
    res = requests.get("".join([url,token,method.format(name)]))
    res_list.extend(res.json()["results"])

for i in res_list:
    name = i['name']
    intel = int(i['powerstats']['intelligence'])
    if name in heros:
        rang_list.append((name, intel))

rang_list = (sorted(rang_list, key=lambda p: p[1]))

print(f"Cамый умный {rang_list[-1][0]}!")