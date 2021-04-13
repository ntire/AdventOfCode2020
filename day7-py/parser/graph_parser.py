import re

def parse_line(line):
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

def find_valid_different_colors_holding_shiny_bag(graph):
    bag_color = "shiny gold"
    unique_bag_colors = find_nodes_with_leave(graph, bag_color)
    return len(unique_bag_colors)
    
def find_nodes_with_leave(graph, searched_leave_id, unique_bag_colors = set()):
    for root in graph.keys():
        leaves = graph.get(root)
        for leave in leaves:
            # if a root leave contains the searched leave, than check if the root itself is another leave
            if searched_leave_id == leave[0]:
                unique_bag_colors.add(root)
                unique_bag_colors = unique_bag_colors.union(find_nodes_with_leave(graph, root, unique_bag_colors))
    return unique_bag_colors

def get_number_of_contained_bags(graph, target_bag = "shiny gold"):
    bag_count = 0

    for node_id in graph.keys():
        if node_id == target_bag:
            for leave in graph.get(node_id):
                leave_id = leave[0]
                leave_multiplier = leave[1]
                bag_count += leave_multiplier + leave_multiplier * get_number_of_contained_bags(graph, leave_id)
    return bag_count