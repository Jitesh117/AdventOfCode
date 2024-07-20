import re
from collections import Counter


def parse_room(room):
    match = re.match(r"([a-z-]+)-(\d+)\[([a-z]+)\]", room)
    if match:
        name, sector_id, checksum = match.groups()
        return name.replace("-", ""), int(sector_id), checksum
    return None


def is_real_room(name, checksum):
    char_counts = Counter(name)
    sorted_chars = sorted(char_counts.items(), key=lambda x: (-x[1], x[0]))
    calculated_checksum = "".join([char for char, _ in sorted_chars[:5]])
    return calculated_checksum == checksum


def decrypt_name(name, sector_id):
    return "".join([
        " " if c == "-" else chr((ord(c) - ord("a") + sector_id) % 26 + ord("a"))
        for c in name
    ])


def part1(rooms):
    total = 0
    for room in rooms:
        parsed = parse_room(room)
        if parsed and is_real_room(parsed[0], parsed[2]):
            total += parsed[1]
    return total


def part2(rooms):
    for room in rooms:
        parsed = parse_room(room)
        if parsed and is_real_room(parsed[0], parsed[2]):
            decrypted = decrypt_name(parsed[0], parsed[1])
            if "northpole" in decrypted:
                return parsed[1]
    return None


with open("input.txt", "r") as file:
    rooms = file.read().splitlines()

print("Part 1:", part1(rooms))
print("Part 2:", part2(rooms))
