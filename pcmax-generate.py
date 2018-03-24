#!/usr/bin/env python3
from sys import argv
from random import randint
from utils import create2dArray


MAX_QUEUE_LEN = 20


def main():
  if (len(argv) < 2):
    print('Provide length as the second argument')

  processorsCount = int(argv[1])
  queues = create2dArray(processorsCount)

  for queue in queues:
    randProcess = randint(1, MAX_QUEUE_LEN - 1)
    completingProcess = MAX_QUEUE_LEN - randProcess
    queue.append(randProcess)
    queue.append(completingProcess)

  processesCount = sum([len(queue) for queue in queues])

  print(processorsCount)
  print(processesCount)
  for queue in queues:
    for item in queue:
      print(item)

if __name__ == "__main__":
  main()
