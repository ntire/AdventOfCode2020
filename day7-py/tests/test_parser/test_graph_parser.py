from parser.graph_parser import parse_line

def test_node_parse_2_leaves():
    line = "light red bags contain 1 bright white bag, 2 muted yellow bags."
    graph = parse_line(line)
    assert 1 == len(graph) # one root node with two leaves


def test_node_name():
    line = "light red bags contain 1 bright white bag, 2 muted yellow bags."
    graph = parse_line(line)
    
    # it's a hack, because dict.keys() is not subscriptable, so graph.keys()[0] does not work
    assert 1 == len(graph)
    for i in graph.keys():
        assert "light red" == i
    
def test_leaf_count():
    line = "light red bags contain 1 bright white bag, 2 muted yellow bags."
    graph = parse_line(line)
    
    assert 2 == len(graph.get("light red"))

def test_empty_node():
    line = "faded blue bags contain no other bags."
    graph = parse_line(line)

    assert 0 == len(graph.get("faded blue"))
    
def test_single_leaf_node():
    line = "bright white bags contain 1 shiny gold bag."
    graph = parse_line(line)
    
    assert 1 == len(graph.get("bright white"))
    
    assert 'shiny gold' == graph.get("bright white")[0][0]
    assert 1 == graph.get("bright white")[0][1]
    
