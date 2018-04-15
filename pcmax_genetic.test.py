from pcmax_genetic import fittness, selection

sample_processes = [1, 2, 3, 1]
sample_individual = [
  [1],
  [2],
  [3, 1],
]

expected_fittness = -4
actual_fittness = fittness(sample_individual)

assert expected_fittness == actual_fittness, "Fittness function is broken, was: " + str(actual_fittness)

fittest_individual = [[1, 1], [2], [3]]
sample_population = [sample_individual] * 9 + [fittest_individual]
expected_selection = [sample_individual, fittest_individual]
actual_selection = selection(sample_population)
assert actual_selection == expected_selection, "Selection broke, was: " + str(actual_selection)
