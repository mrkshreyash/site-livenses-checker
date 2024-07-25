import requests

url = "https://www.google.com"

res = requests.get(url)

with open("Site.html", "w") as file:
    file.writelines(res.text)
