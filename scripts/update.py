import os
import urllib.request
import difflib


URL = "https://raw.githubusercontent.com/HotCakeX/Official-IANA-IP-blocks/main/IPv4/IR.txt"


os.makedirs("data", exist_ok=True)
os.makedirs("output", exist_ok=True)


old_file = "data/previous.txt"
new_file = "data/current.txt"


# دانلود لیست جدید

print("Downloading...")

urllib.request.urlretrieve(
    URL,
    new_file
)


# خواندن لیست قبلی

old_ips = []

if os.path.exists(old_file):
    with open(old_file) as f:
        old_ips = [
            x.strip()
            for x in f.readlines()
            if x.strip()
        ]


# خواندن لیست جدید

with open(new_file) as f:
    new_ips = [
        x.strip()
        for x in f.readlines()
        if x.strip()
    ]


old_set = set(old_ips)
new_set = set(new_ips)


added = sorted(new_set - old_set)
removed = sorted(old_set - new_set)



print("Added:", len(added))
print("Removed:", len(removed))



# ساخت فایل کامل

with open(
    "output/iran-full.rsc",
    "w"
) as f:

    f.write("/ip firewall address-list\n")

    for ip in new_ips:

        f.write(
            'add list=Iran address='
            + ip
            + ' comment="AUTO-IANA"\n'
        )



# ساخت فایل تغییرات

with open(
    "output/iran-update.rsc",
    "w"
) as f:


    f.write("/ip firewall address-list\n\n")


    for ip in removed:

        f.write(
            ':do {remove [find list=Iran address="'
            + ip
            + '"]} on-error={}\n'
        )


    for ip in added:

        f.write(
            'add list=Iran address='
            + ip
            + ' comment="AUTO-IANA"\n'
        )



# ذخیره نسخه جدید برای فردا

with open(
    old_file,
    "w"
) as f:

    for ip in new_ips:
        f.write(ip+"\n")



print("Done")
