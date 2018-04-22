#!/usr/bin/env python3
from random import randint
from customio import getInput, visualize
from utils import create2dArray


def pcmaxRandom(processorsCount, processesTimes):
  result = create2dArray(processorsCount)

  for process in processesTimes:
    processor = randint(0, processorsCount - 1)
    result[processor].append(process)

  return result



def main():
  (processorsCount, processesCount, processesTimes) = getInput()
  result = pcmaxRandom(processorsCount, processesTimes)
  visualize(result)


if __name__ == "__main__":
  main()
