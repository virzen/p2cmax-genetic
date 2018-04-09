#!/usr/bin/env python3
from random import shuffle
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


def get_genotype_chunks(processes, genotype):
  return [genotype[i:i + len(processes)] for i in range(0, len(genotype), len(processes))]


def encode(original_processes, individual):
  processes = list(original_processes)
  genotype = []

  # O(n * m) >:(
  for processor in individual:
    bit_array = [0] * len(processes)

    for process in processor:
      if process in processes:
        index = processes.index(process)
        bit_array[index] = 1
        processes[index] = -1

    genotype += bit_array

  return genotype


def decode(processes, genotype):
  individual = []
  genotype_chunks = get_genotype_chunks(processes, genotype)

  for chunk in genotype_chunks:
    processor = [processes[index] for (index, process) in enumerate(chunk) if process == 1]
    individual.append(processor)

  return individual


# lower is better
def fitness(individual):
  return max([sum(times) for times in individual])


def selection(population):
  # TODO
  return population[0:3]


def crossover(individual1, individual2):
  # TODO
  return (individual1, individual2)


def mutation(individual):
  # TODO
  return individual


def main():
  (processorsCount, processesCount, processesTimes) = getInput()

  initial_population = []
  for i in range(POPULATION_SIZE):
    initial_population.append(pcmaxRandom(processesCount, processesTimes))

  genotypes = [encode(processesTimes, individual) for individual in initial_population]

  visualize(initial_population[0])
  print(genotypes[0])


if __name__ == '__main__':
  main()
