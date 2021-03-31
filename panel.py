import requests


with open("siteler.txt", "r") as f:
    for line in f:
        url = line.strip("\n") + "/panel"
        r = requests.get(url)
        if r.status_code == 200:
            print(r.url)
        else:
            pass
