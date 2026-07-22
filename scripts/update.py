import os
import json
import urllib.request


API = "https://stat.ripe.net/data/country-resource-list/data.json?resource=IR"


os.makedirs("data", exist_ok=True)
os.makedirs("output", exist_ok=True)


print("Downloading Iran IP list...")


with urllib.request.urlopen(API) as response:
    raw = response.read()


# ذخیره پاسخ خام برای بررسی
with open("data/ripe-response.json", "wb") as f:
    f.write(raw)


data = json.loads(raw)


print("JSON keys:")
print(data.keys())


if "resources" not in data:
    print("No resources key found")
    print(json.dumps(data, indent=2)[:2000])
    exit(1)


ips = data["resources"].get("ipv4", [])


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


print("Done")
