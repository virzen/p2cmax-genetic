#!/usr/bin/env python3
from random import randint
from customio import getInput, visualize

def create2dArray(size):
  return [[] for _ in range(size)]

def main():
  (processorsCount, processesCount, processesTimes) = getInput()
  result = create2dArray(processorsCount)

  for process in processesTimes:
    processor = randint(0, processorsCount - 1)
    result[processor].append(process)

  print('processors: ' + str(processorsCount))
  print('processes: ' + str(processesTimes))
  print(result)
  print(visualize(result))

if __name__ == "__main__":
  main()
