import os
import urllib.request


URL = "https://raw.githubusercontent.com/HotCakeX/Official-IANA-IP-blocks/main/IPv4/IR.txt"


os.makedirs("data", exist_ok=True)
os.makedirs("output", exist_ok=True)


print("Downloading Iran IP list...")

urllib.request.urlretrieve(
    URL,
    "data/current.txt"
)


print("Download finished")


with open("data/current.txt") as f:
    ips = f.read().splitlines()


with open("output/iran-full.rsc","w") as f:

    f.write("/ip firewall address-list\n")

    for ip in ips:

        if ip.strip():

            f.write(
                'add list=Iran address='
                + ip.strip()
                + ' comment="AUTO-IANA"\n'
            )


print("RSC generated")
