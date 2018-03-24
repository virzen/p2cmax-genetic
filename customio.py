from sys import argv


def getInput():
  if (len(argv) < 2):
    print("Usage: ")
  filename = argv[1]
  file = open(filename)
  lines = file.read().split('\n')
  nonEmptyLines = [x for x in lines if x != ""]
  numbers = [int(x) for x in nonEmptyLines]
  processorsCount = numbers[0]
  processesCount = numbers[1]
  processesTimes = numbers[2:]
  return (processorsCount, processesCount, processesTimes)


def visualizeLines(result):
  padLen = len(str(len(result)))

  for (index, queue) in enumerate(result):
    tasks = ' '.join(['=' * x for x in queue])
    print(str(index).rjust(padLen, ' ') + ': ' + tasks)

def visualizeNumbers(result):
  padLen = len(str(len(result)))

  for (index, queue) in enumerate(result):
    print(str(index).rjust(padLen, ' ') + ': ' + str(sum(queue)))

def visualize(result):
  maxQueueLen = max([sum(queue) for queue in result])
  if maxQueueLen <= 80:
    visualizeLines(result)
  else:
    visualizeNumbers(result)
