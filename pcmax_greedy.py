#!/usr/bin/env python3
from random import randint
from customio import getInput, visualize
from utils import create2dArray


def pcmaxGreedy(processorsCount, processesCount, processesTimes):
  result = create2dArray(processorsCount)

  for process in processesTimes:
    lowestLenProcessor = result.index(min(result, key=sum))
    result[lowestLenProcessor].append(process)

  return result


def main():
  (processorsCount, processesCount, processesTimes) = getInput()

  result = pcmaxGreedy(processorsCount, processesCount, processesTimes)
  max_time = max([sum(times) for times in result])

  visualize(result)

  print('Maximum processor time: ' + str(max_time))


if __name__ == "__main__":
  main()
