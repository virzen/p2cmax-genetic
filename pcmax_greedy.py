#!/usr/bin/env python3
from random import randint
from customio import getInput, getParams, visualize
from utils import create2dArray


def pcmaxGreedy(processorsCount, processesCount, processesTimes):
    result = create2dArray(processorsCount)

    for process in processesTimes:
        lowestLenProcessor = result.index(min(result, key=sum))
        result[lowestLenProcessor].append(process)

    return result


def main():
    (processorsCount, processesCount, processesTimes) = getInput()
    _, should_display_chart = getParams()

    result = pcmaxGreedy(processorsCount, processesCount, processesTimes)
    max_time = max([sum(times) for times in result])

    print(str(max_time))

    if should_display_chart:
        visualize(result)


if __name__ == "__main__":
    main()
