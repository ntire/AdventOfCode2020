from passport_check.passport_checker import count_passports_with_valid_fields_and_valid_count

if __name__ == "__main__":
    f = "input"
    counter = count_passports_with_valid_fields_and_valid_count(f)
    print("Result: {}".format(counter))
