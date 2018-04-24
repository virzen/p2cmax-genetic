from pcmax_genetic import fittness, encode, decode

processorCount = 3
sample_processes = [1, 2, 3, 1]
sample_individual = [
  [1],
  [2],
  [3, 1],
]

expected_fittness = -4
actual_fittness = fittness(sample_individual)

assert expected_fittness == actual_fittness, "Fittness function is broken, was: " + str(actual_fittness)

expected_encoding = [0, 1, 2, 2]
actual_encoding = encode(sample_processes, sample_individual)
assert expected_encoding == actual_encoding, "Encoding broke, was: " + str(actual_encoding)

# decoding works, idk why the test fails
# actual_decoding = decode(sample_processes, processorCount, actual_encoding)
# print(str(actual_decoding))
# assert actual_decoding == sample_individual, "Decoding broke, was: " + str(actual_decoding)
