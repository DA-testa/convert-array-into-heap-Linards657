# python3
import math
import numpy as np


def build_heap(data, n):
    swaps = []
    steps = 0
    levels = math.floor(math.log2(n + 1))
    i = 2 ** (levels + 1) - 1
    # TODO: Create heap and heap sort

    while i >= 1:
        if i < 2:
            if steps < 1:
                break
            else:
                i = steps - 1
                steps = 0
        try:
            if data[i - 1] < data[i // 2 - 1]:
                swaps.append((i // 2 - 1, i-1))
                data_save = data[i // 2 - 1]
                data[i // 2 - 1] = data[i-1]
                data[i-1] = data_save
                if i > steps:
                    steps = i
                i = i // 2
                continue
        except IndexError:
            pass
        try:
            if data[i - 2] < data[i // 2 - 1]:
                swaps.append((i // 2 - 1, i - 2))
                data_save = data[i // 2 - 1]
                data[i // 2 - 1] = data[i - 2]
                data[i - 2] = data_save
                if i > steps:
                    steps = i
                i = i // 2
                continue
        except IndexError:
            pass
        i = i - 2
    # try to achieve  O(n) and not O(n2)

    return swaps


def main():
    # TODO : add input and corresponding checks
    # add another input for I or F
    # first two tests are from keyboard, third test is from a file

    # input from keyboard
    text = input()

    if "I" in text[:1]:
        n = int(input())
        data = np.asarray(list(map(int, input().split())))
    else:
        text = input()
        f = open("./tests/" + text, "r")
        n = int(f.readline())
        data = np.asarray(list(map(int, f.readline().split())))
        f.close()

    # checks if length of data is the same as the said length
    assert len(data) == n

    # calls function to assess the data
    # and give back all swaps

    swaps = build_heap(data, n)

    # TODO: output how many swaps were made,
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
