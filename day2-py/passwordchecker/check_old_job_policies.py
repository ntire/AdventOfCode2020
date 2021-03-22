def is_password_compliant(raw_rule):
    result = False

    # Step 1. Split input into three tokens 
    #   (   first: min-max length of letter, 
    #       second: letter, 
    #       third: password to be checked)
    tokens = raw_rule.split(" ")

    minmax = tokens[0].split("-")
    min_ = int(minmax[0])
    max_ = int(minmax[1])
    
    letter = tokens[1].split(":")[0]
    password = tokens[2]
    
    if len(password) < min_:
        result = False
    else:
        counter = 0
        for i in range(len(password)):
            if password[i] == letter:
                counter+=1
        result = counter >= min_ and counter <= max_

    return result
