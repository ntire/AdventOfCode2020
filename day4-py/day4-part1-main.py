from passport_check.passport_checker import count_valid_passports

if __name__ == "__main__":
    f = "input"
    counter = count_valid_passports(f)
    print("Result: {}".format(counter))
