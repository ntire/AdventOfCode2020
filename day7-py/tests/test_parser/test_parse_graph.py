from parser.graph_parser import parse_lines


def test_parse_simple_graph():
    lines = ["light red bags contain 1 bright white bag, 2 muted yellow bags."]
    graph = parse_lines(lines)
    assert 1 == len(graph.keys())
    
    for k in graph.keys():
        assert k == "light red"

def test_parse_two_nodes():
    lines = ["light red bags contain 1 bright white bag, 2 muted yellow bags.",\
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags."]
    graph = parse_lines(lines)

    test_keys = ["light red", "dark orange"]
    for k in graph.keys():
        test_keys.remove(k)
    
    assert 0 == len(test_keys) # test if all test keys are removed

def test_two_leaves_same_node():
    lines = ["dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "dark olive bags contain 3 bright white bags, 4 muted yellow bags."]
    
    graph = parse_lines(lines)

    assert 1 == len(graph.keys())
    
def test_one_node_four_leaves():
    lines = ["dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "dark olive bags contain 3 bright white bags, 4 muted yellow bags."]
    
    graph = parse_lines(lines)

    assert 4 == len(graph.get("dark olive"))
    
