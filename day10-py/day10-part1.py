
from joltage.joltage_adapter import retrieve_joltage_array, determine_voltage_distribution

joltages = retrieve_joltage_array('input')
jdis = determine_voltage_distribution(joltages)

result = jdis[0] * jdis[2]

print("Result:", result)