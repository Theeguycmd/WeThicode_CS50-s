import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    embed = re.search(r'(https?)(://)(?:www.)?(youtu)(be).com(/)embed/(\w+)"', s)
    if embed:
        if "s" in embed.group(1):
            return f"{embed.group(1)}{embed.group(2)}{embed.group(3)}.{embed.group(4)}{embed.group(5)}{embed.group(6)}"
        return f"{embed.group(1)}s{embed.group(2)}{embed.group(3)}.{embed.group(4)}{embed.group(5)}{embed.group(6)}"
    return None


if __name__ == "__main__":
    main()
