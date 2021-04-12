import re

def parse_line(line):
    graph = dict()
    # Extract graph data from string
    node_pattern = re.compile(r"^((\w+ \w+) bag[s]* contain)")
    m = node_pattern.match(line)
    root_id = m.groups()[1]
    
    leaves = []

    leaf_pattern = re.compile(r"((\d+) (\w+ \w+))")
    leaf_matches = leaf_pattern.findall(line)

    for leaf in leaf_matches:
        leaf_count = int(leaf[1])
        leaf_id = leaf[2]
        leaves.append([leaf_id, leaf_count])

    return root_id, leaves

def parse_lines(lines):
    graph = dict()
    for line in lines:
        root_id, leaves = parse_line(line)
        if root_id not in graph.keys():
            graph[root_id] = leaves
        else:
            for leave in leaves:
                graph.get(root_id).append(leave)
    return graph