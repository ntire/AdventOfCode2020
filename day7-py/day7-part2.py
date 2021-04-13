from parser.graph_parser import parse_lines, get_number_of_contained_bags

def main():
    filename = "input"
    with open(filename) as f:
       lines = f.readlines()
    
    graph = parse_lines(lines)
    no_of_bags = get_number_of_contained_bags(graph)

    print("Number of individual bags inside of shiny bag:", no_of_bags)

if __name__ == "__main__":
    main()