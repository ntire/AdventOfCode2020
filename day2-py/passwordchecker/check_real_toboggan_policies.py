def is_password_compliant(raw_rule):
    result = False

    # Step 1. Split input into three tokens 
    #   (   first: first and second position of letter, 
    #       second: letter, 
    #       third: password to be checked)
    tokens = raw_rule.split(" ")

    positions = tokens[0].split("-")
    first = int(positions[0])
    second = int(positions[1])
    
    letter = tokens[1].split(":")[0]
    password = tokens[2]
    
    if len(password) < first:
        result = False
    elif (len(password) >= first and len(password) < second):
        result = password[first - 1] == letter
    elif (len(password) >= second):
        # print("Letter: {}, First: {}, Second: {}".format(letter, password[first-1], password[second-1]))
        result = ((password[first - 1] == letter) and (password[second - 1] != letter)) or ((password[first -1 ] != letter) and (password[second - 1] == letter))
    
        
    return result
