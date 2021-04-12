from parser.graph_parser import parse_line

def test_node_parse_2_leaves():
    line = "light red bags contain 1 bright white bag, 2 muted yellow bags."
    _, leaves = parse_line(line)
    assert 2 == len(leaves) # one root node with two leaves


def test_node_name():
    line = "light red bags contain 1 bright white bag, 2 muted yellow bags."
    root_id, _ = parse_line(line)
    assert "light red" == root_id

def test_empty_node():
    line = "faded blue bags contain no other bags."
    _, leaves = parse_line(line)

    assert 0 == len(leaves)
    
def test_single_leaf_node():
    line = "bright white bags contain 1 shiny gold bag."
    _, leaves = parse_line(line)
    
    assert 1 == len(leaves)
    
    assert 'shiny gold' == leaves[0][0]
    assert 1 == leaves[0][1]
    
