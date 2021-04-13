import re

def parse_bootcode(lines):
    bootcode = list()
    code_pattern = re.compile(r"(\w+) ([+-]\d+)")

    for line in lines:
        m = code_pattern.match(line)
        bootcode.append([m.group(1), int(m.group(2))])
    return bootcode