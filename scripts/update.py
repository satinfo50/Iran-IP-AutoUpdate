import os
import urllib.request
import urllib.error


URL = "https://raw.githubusercontent.com/HotCakeX/Official-IANA-IP-blocks/main/TXT/IPV4/IR.txt"


os.makedirs("data", exist_ok=True)
os.makedirs("output", exist_ok=True)

new_file = "data/current.txt"

print("Downloading:")
print(URL)

try:
    urllib.request.urlretrieve(
        URL,
        new_file
    )

except urllib.error.HTTPError as e:
    print("Download failed:", e)
    exit(1)


print("Download OK")


with open(new_file) as f:
    ips = [
        x.strip()
        for x in f.readlines()
        if x.strip()
    ]


with open("output/iran-full.rsc", "w") as f:

    f.write("/ip firewall address-list\n")

    for ip in ips:

        f.write(
            'add list=Iran address='
            + ip
            + ' comment="AUTO-IANA"\n'
        )


print("RSC generated:", len(ips))
