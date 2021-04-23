from parser.graph_parser import parse_lines, find_valid_different_colors_holding_shiny_bag

def test_hold_one_bag():
    lines = ["bright white bags contain 1 shiny gold bag."]
    graph = parse_lines(lines)
    valid_colors = find_valid_different_colors_holding_shiny_bag(graph)
    assert 1 == valid_colors


def test_two_colors_holding_bag():
    lines = ["bright white bags contain 1 shiny gold bag.",\
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags."]
    graph = parse_lines(lines)
    valid_colors = find_valid_different_colors_holding_shiny_bag(graph)
    assert 2 == valid_colors

def test_three_colors():
    lines = ["bright white bags contain 1 shiny gold bag.",\
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "faded brown bags contain 1 muted yellow bag."]
    graph = parse_lines(lines)
    valid_colors = find_valid_different_colors_holding_shiny_bag(graph)
    assert 3 == valid_colors

def test_input_test_file():
    filename = "day7-py/input_test"
    with open(filename) as f:
       lines = f.readlines()
    
    graph = parse_lines(lines)
    valid_colors = find_valid_different_colors_holding_shiny_bag(graph)

    assert 4 == valid_colors

