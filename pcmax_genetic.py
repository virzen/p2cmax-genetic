#!/usr/bin/env python3
from random import shuffle, random, randint
from customio import getInput
from customio import visualize
from pcmax_random import pcmaxRandom
from math import ceil, inf
from utils import create2dArray

from os import environ
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

POPULATION_SIZE = int(environ.get('POPULATION_SIZE'))
MUTATION_PROBABILITY = float(environ.get('MUTATION_PROBABILITY'))
SELECTION_QUANTITY = int(environ.get('SELECTION_QUANTITY'))
NO_PROGRESS_BAILOUT_COUNT = int(environ.get('NO_PROGRESS_BAILOUT_COUNT'))

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
# processes = [1, 2, 4, 3]
# individual = [
#   [1, 4], <-- processor0 queue
#   [2],    <-- processor1 queue
#   [3]
# ]
# genotype = [0, 1, 0, 2]


def encode(processes, individual):
  genotype = []

  for process in processes:
    for processor_index, processor in enumerate(individual):
      if process in processor:
        genotype.append(processor_index)
        process_index = processor.index(process)
        processor[process_index] = -1
        break

  return genotype


def decode(processes, processorsCount, genotype):
  processors = create2dArray(processorsCount)

  for process_index, processor_index in enumerate(genotype):
    processors[processor_index].append(processes[process_index])

  return processors


def fittness(processes, processorsCount, genotype):
  individual = decode(processes, processorsCount, genotype)
  max = 0
  for processor in individual:
    time = sum(processor)
    if time > max:
      max = time
  return -1 * max


def selection(processes, processorsCount, population):
  by_fittest = sorted(population, key=lambda genotype: fittness(processes, processorsCount, genotype), reverse=True)
  return by_fittest[:SELECTION_QUANTITY]


def crossover(genotype_a, genotype_b):
  length = len(genotype_a)
  half_length = round(length)
  first_child = genotype_a[:half_length] + genotype_b[half_length:]
  second_child = genotype_a[half_length:] + genotype_b[:half_length]

  return (first_child, second_child)


def mutation(processorsCount, population):
  for genotype in population:
    if random() < MUTATION_PROBABILITY:
      index = randint(0, len(genotype) - 1)
      new_processor_index = randint(0, processorsCount - 1)
      genotype[index] = new_processor_index


def setup(processorsCount, processes):
  initial_population = []

  for i in range(POPULATION_SIZE):
    individual = pcmaxRandom(processorsCount, processes)
    genotype = encode(processes, individual)
    initial_population.append(genotype)

  return initial_population


def loop(initial_population, generate_random_individual, processes, processorsCount):
  population = initial_population
  best = inf
  no_progress_counter = 0
  generation_counter = 0

  while no_progress_counter < NO_PROGRESS_BAILOUT_COUNT:
    # selection
    fittest_individuals = selection(processes, processorsCount, population)

    # crossover
    first_child, second_child = crossover(fittest_individuals[0], fittest_individuals[1])

    population = fittest_individuals + [first_child, second_child]

    # mutation
    mutation(processorsCount, population)

    # new individuals
    for i in range(POPULATION_SIZE - len(population)):
      population.append(encode(processes, generate_random_individual()))

    current_best = abs(fittness(processes, processorsCount, fittest_individuals[0]))
    if current_best < best:
      best = current_best
      print(best)
      no_progress_counter = 0
    else:
      no_progress_counter += 1

    generation_counter += 1

  print(best)


def make_pcmaxrandom_generator(processorsCount, processes):
  return lambda : pcmaxRandom(processorsCount, processes)


def main():
  (processorsCount, processesCount, processes) = getInput()

  initial_population = setup(processorsCount, processes)
  generate_random_individual = make_pcmaxrandom_generator(processorsCount, processes)
  loop(initial_population, generate_random_individual, processes, processorsCount)


if __name__ == '__main__':
  main()
