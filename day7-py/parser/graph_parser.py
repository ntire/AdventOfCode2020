import re

def parse_line(line):
    graph = dict()
    # Extract graph data from string
    node_pattern = re.compile(r"^((\w+ \w+) bag[s]* contain)")
    m = node_pattern.match(line)
    node = m.groups()[1]
    
    graph[node] = []

    leaf_pattern = re.compile(r"((\d+) (\w+ \w+))")
    leaf_matches = leaf_pattern.findall(line)

    for leaf in leaf_matches:
        leaf_count = int(leaf[1])
        leaf_id = leaf[2]
        graph[node].append([leaf_id, leaf_count])

    return graph