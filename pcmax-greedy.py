#!/usr/bin/env python3
from random import randint
from customio import getInput, visualize
from utils import create2dArray

def main():
  (processorsCount, processesCount, processesTimes) = getInput()
  result = create2dArray(processorsCount)

  for process in processesTimes:
    lowestLenProcessor = result.index(min(result, key=sum))
    result[lowestLenProcessor].append(process)

  visualize(result)

if __name__ == "__main__":
  main()
