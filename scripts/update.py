import os
import json
import urllib.request


API = "https://stat.ripe.net/data/country-resource-list/data.json?resource=ir&v4_format=prefix"


os.makedirs("data", exist_ok=True)
os.makedirs("output", exist_ok=True)


print("Downloading Iran IP list...")


with urllib.request.urlopen(API) as response:
    data = json.loads(response.read())


ips = data["resources"]["ipv4"]


print("IPv4 count:", len(ips))


with open("data/current.txt", "w") as f:
    for ip in ips:
        f.write(ip + "\n")



with open("output/iran-full.rsc", "w") as f:

    f.write("/ip firewall address-list\n")

    for ip in ips:

        f.write(
            'add list=Iran address='
            + ip
            + ' comment="AUTO-RIPE"\n'
        )


print("iran-full.rsc created")
