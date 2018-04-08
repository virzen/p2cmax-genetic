from pcmax_genetic import encode, decode

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
