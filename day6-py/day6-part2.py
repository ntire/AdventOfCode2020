from questions.yes_counter import count_unique_answers_of_everyone

def main():
    groups = list()
    with open("input") as f:
        group = list()
        for line in f.readlines():
            if line == "\n" and len(group) > 0:
                groups.append(group)
                group = list()
            else:
                group.append(line.rstrip("\n"))
        # last group
        if len(group) > 0:
            groups.append(group)
    
    unique_answers_counter = 0
    for group in groups:
        unique_answers_counter += count_unique_answers_of_everyone(group)
    
    print("Sum of unique counts:", unique_answers_counter)


if __name__ == "__main__":
    main()