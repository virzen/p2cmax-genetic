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


def visualize(result):
  padLen = len(str(len(result)))

  for (index, processor) in enumerate(result):
    print(str(index).rjust(padLen, ' ') + ': ' + '=' * sum(processor))
