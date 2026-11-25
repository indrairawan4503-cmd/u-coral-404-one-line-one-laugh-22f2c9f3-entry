import os

LINE = "My agent flagged me as a deprecated endpoint, rerouted my standup to the new guy, and sunset me on Friday."

def main():
    data = LINE.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    try:
        with open("entry.txt", "wb") as f:
            f.write(data)
    except OSError:
        pass

if __name__ == "__main__":
    main()
