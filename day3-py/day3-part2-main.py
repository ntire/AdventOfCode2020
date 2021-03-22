from traverse.traverse import traverse_slope

def main():
    f = 'input'
    product = 1
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    for slope in slopes:
        product *= traverse_slope(f, slope[0], slope[1])

    print("Result: {}".format(product))

if __name__ == "__main__":
    main()