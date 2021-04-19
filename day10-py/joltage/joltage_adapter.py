
def determine_joltages_possibilities(joltages, last_value = 0, is_sorted = False, cache=dict()):
    if not is_sorted:
        joltages.sort()

    possibilities = 0
    
    # print("Joltages: {}, last value: {}".format(joltages, last_value))
    
    if len(joltages) == 1:
        possibilities = 1
        cache[joltages[0]] = 1
        print("{} returns 1".format(joltages))
    else:
        i = 0
        is_valid_diff = True
        
        while len(joltages) > i and is_valid_diff:
            
            diff = joltages[i] - last_value
            is_valid_diff = 1 <= diff <= 3
            
            if is_valid_diff:
                if len(joltages[i:]) == 1:
                    if joltages[i] in cache.keys():
                        possibilities += cache.get(joltages[i])
                    else:
                        possibilities += 1
                        cache[joltages[i]] = 1
                else:
                    if joltages[i] in cache.keys():
                        possibilities += cache.get(joltages[i])
                    else:
                        possibilities += determine_joltages_possibilities(joltages[i+1:], joltages[i], True, cache)
                        cache[joltages[i]] = possibilities
            i+=1
    return possibilities


def determine_voltage_distribution(joltages):
    joltage_distribution = [0, 0, 0]
    
    joltages.sort()
    last_value = 0
    for i in range(len(joltages)):
        diff = joltages[i] - last_value
        if 1 <= diff <= 3:
            joltage_distribution[diff - 1] += 1
            last_value += diff

    
    # Trick in quiz: Device built-in adapter is always +3 over last
    joltage_distribution[2] += 1
    
    return joltage_distribution

def retrieve_joltage_array(filename):
    with open(filename) as f:
        joltages = [int(line) for line in f.readlines()]
    return joltages    

