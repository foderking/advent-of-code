import requests, os

def getInput(year, day):
    if os.path.exists(f"input{day}.txt"):
        print("[+] Retrieving input...")
        return open(f"input{day}.txt", "r").read().rstrip()

    print("[+] Downloading input...")
    cookie = open("cookie.txt", "r").read().strip()
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    req = requests.get(url, cookies={'session': cookie})
    text = req.text

    with open(f"input{day}.txt", "w") as f:
        f.write(text)
    return text


if __name__=="__main__":
    print(getInput(2016,1))
