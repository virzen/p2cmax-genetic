from pcmax_genetic import encode, decode, fittness, selection, is_valid_genotype

sample_processes = [1, 2, 3, 1]
sample_individual = [
  [1],
  [2],
  [3, 1],
]
expected_genotype = [ 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1 ]
encoded_genotype = encode(sample_processes, sample_individual)

assert encoded_genotype == expected_genotype, "Encode broke, was: " + str(encoded_genotype)

decoded_individual = decode(sample_processes, encoded_genotype)

assert decoded_individual == sample_individual, "Decode doesnt work, was: " + str(decoded_individual)

expected_fittness = -4
actual_fittness = fittness(sample_processes, encoded_genotype)

assert expected_fittness == actual_fittness, "Fittness function is broken, was: " + str(actual_fittness)

fittest_genotype = encode(sample_processes, [[1, 1], [2], [3]])
sample_population = [encoded_genotype] * 9 + [fittest_genotype]
expected_selection = [encoded_genotype, fittest_genotype]
actual_selection = selection(sample_processes, sample_population)
print(expected_selection)
assert actual_selection == expected_selection, "Selection broke, was: " + str(actual_selection)

sample_invalid_genotype = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
valid_genotype = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1]
assert is_valid_genotype(sample_processes, sample_invalid_genotype) == False
assert is_valid_genotype(sample_processes, valid_genotype) == True
