import re


with open("input.txt") as file:
    input = file.read()


def is_abba(s: str) -> bool:
    for i in range(len(s) - 3):
        if s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]:
            return True
    return False


def part1(ip) -> bool:
    parts = re.split(r"\[|\]", ip)
    supernets = parts[::2]
    hypernets = parts[1::2]

    if any(is_abba(part) for part in supernets):
        if not any(is_abba(part) for part in hypernets):
            return True
    return False


def get_aba_sequences(s):
    aba_sequences = []
    for i in range(len(s) - 2):
        if s[i] == s[i + 2] and s[i] != s[i + 1]:
            aba_sequences.append(s[i : i + 3])
    return aba_sequences


def has_corresponding_bab(aba, hypernets):
    bab = aba[1] + aba[0] + aba[1]
    return any(bab in hypernet for hypernet in hypernets)


def part2(ip):
    parts = re.split(r"\[|\]", ip)
    supernets = parts[::2]
    hypernets = parts[1::2]

    for supernet in supernets:
        for aba in get_aba_sequences(supernet):
            if has_corresponding_bab(aba, hypernets):
                return True
    return False


print(sum(part1(ip) for ip in input.splitlines()))
print(sum(part2(ip) for ip in input.splitlines()))
