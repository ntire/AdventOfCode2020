from joltage.joltage_adapter import determine_joltages_possibilities, retrieve_joltage_array

joltages = retrieve_joltage_array('input')
p = determine_joltages_possibilities(joltages)

print ("Total distinct ways:", p)