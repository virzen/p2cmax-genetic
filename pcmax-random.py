#!/usr/bin/env python3
from random import randint
from customio import getInput, visualize
from utils import create2dArray

def main():
  (processorsCount, processesCount, processesTimes) = getInput()
  result = create2dArray(processorsCount)

  for process in processesTimes:
    processor = randint(0, processorsCount - 1)
    result[processor].append(process)

  visualize(result)

if __name__ == "__main__":
  main()
