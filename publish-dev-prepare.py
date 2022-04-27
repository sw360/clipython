import datetime
import requests
import os

# bump version number for dev package
lines = open("pyproject.toml").readlines()
with open("pyproject.toml", "w") as f:
    for line in lines:
        if line.startswith("version = "):
            version = line[10:].strip().strip('"').split('.')
            version[-1] = str(int(version[-1]) + 1)
            today = datetime.date.today().strftime("%Y%m%d")
            f.write('version = "' + '.'.join(version) + '.dev' + today + '"\n')
        else:
            f.write(line)

# delete old dev versions
# This requires an environment variable PKG_ACCESS_TOKEN
# containing a Gitlab access token capable of deleting packages.
# (Create it in Settings > Access Tokens > Project Access Tokens, for CI runs
#  store it in Settings > CI/CD > Variables (protected & masked!)).
r = requests.get(os.environ["REGISTRY_URL"])
if not r.ok:
    print("WARNING: No information about releases found at",
          os.environ["REGISTRY_URL"])
else:
    r = r.json()
    releases = [e for e in r if e["version"].find(".dev") > 0]
    for release in releases:
        print(requests.delete(os.environ["REGISTRY_URL"] + "/" + str(release["id"]),
                              headers={"PRIVATE-TOKEN": os.environ["PKG_ACCESS_TOKEN"]}))
