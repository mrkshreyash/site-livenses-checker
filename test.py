import requests

url = "https://taco-taskkatcon.in"

res = requests.get(url)

with open("Site.html", "w") as file:
    file.writelines(res.text)
