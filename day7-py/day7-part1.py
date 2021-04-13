from parser.graph_parser import parse_lines, find_valid_different_colors_holding_shiny_bag

def main():
    filename = "input"
    with open(filename) as f:
        lines = f.readlines()

    graph = parse_lines(lines)
    valid_colors = find_valid_different_colors_holding_shiny_bag(graph)
    print("Valid colors of outermost bags:", valid_colors)

if __name__ == "__main__":
    main()