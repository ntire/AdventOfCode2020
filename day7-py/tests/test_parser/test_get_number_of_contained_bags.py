from parser.graph_parser import get_number_of_contained_bags, parse_lines


def test_simple_file():
    lines = ["shiny gold bags contain 2 dark red bags.",
            "dark red bags contain 2 dark orange bags."]
    graph = parse_lines(lines)
    no_of_bags = get_number_of_contained_bags(graph)

    assert 6 == no_of_bags

def test_part1_test_file():
    filename = "day7-py/input_test"
    with open(filename) as f:
       lines = f.readlines()
    
    graph = parse_lines(lines)
    no_of_bags = get_number_of_contained_bags(graph)

    assert 32 == no_of_bags

def test_part2_test_file():
    filename = "day7-py/input_test_part2"
    with open(filename) as f:
       lines = f.readlines()
    
    graph = parse_lines(lines)
    no_of_bags = get_number_of_contained_bags(graph)

    assert 126 == no_of_bags
