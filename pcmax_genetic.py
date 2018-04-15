#!/usr/bin/env python3
from random import shuffle, random, randint
from customio import getInput
from customio import visualize
from pcmax_random import pcmaxRandom
from math import ceil, inf

# START
# Generate the initial population
# Compute fitness
# REPEAT
#     Selection
#     Crossover
#     Mutation
#     Compute fitness
# UNTIL population has converged
# STOP


# Data structure:
# individual = [
#   [processTime1, processTime2], <-- processor0 queue
#   [processTime3, processTime4]  <-- processor1 queue
# ]


GUARD_VALUE = -1
POPULATION_SIZE = 10
SELECTION_RATE = 0.2
CROSSOVER_PROBABILITY = 0
MUTATION_PROBABILITY = 0


def fittness(individual):
  return -1 * max([sum(processor) for processor in individual])


def selection(population):
  sorted_by_fittest = sorted(population, key=lambda chromosome: fittness(chromosome))
  quantity = ceil(POPULATION_SIZE * SELECTION_RATE)
  return sorted_by_fittest[-1 * quantity:]


def crossover(individual_a, individual_b):
  # TODO
  return


# swap at most 2 processes between 2 random processors
def mutation(individual):
  indices = list(range(len(individual)))
  shuffle(indices)
  [src_processor_index, dest_processor_index] = indices[:2]

  if len(individual[src_processor_index]) < 1:
    return

  src_processor = individual[src_processor_index]
  dest_processor = individual[dest_processor_index]


  process = src_processor[0]
  src_processor.remove(process)
  dest_processor.append(process)



def setup(processesCount, processes):
  initial_population = []

  for i in range(POPULATION_SIZE):
    individual = pcmaxRandom(processesCount, processes)
    initial_population.append(individual)

  return initial_population


def loop(initial_population):
  return



def main():
  (processorsCount, processesCount, processes) = getInput()

  initial_population = setup(processesCount, processes)
  loop(initial_population)


if __name__ == '__main__':
  main()
