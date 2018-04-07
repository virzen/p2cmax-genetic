#!/usr/bin/env python3
from random import randint
from customio import getInput, visualize
from utils import create2dArray
from pcmax_greedy import pcmaxGreedy
from itertools import permutations


def main():
  (processorsCount, processesCount, processesTimes) = getInput()
  results = [pcmaxGreedy(processorsCount, processesCount, list(instance)) for instance in permutations(processesTimes)]

  final_result = min(results, key=lambda result: max([sum(times) for times in result]))
  max_time = max([sum(times) for times in final_result])

  print(final_result)
  visualize(final_result)
  print('Time: ' + str(max_time))


if __name__ == "__main__":
  main()
