# python3


def build_heap(data, n):
    swaps = []
    steps = 0
    i = n // 2 - 1
    # TODO: Create heap and heap sort
    while i >= 0:
        try:
            if data[2 * i + 1] < data[2 * i + 2]:
                salidzinama_adrese = 2 * i + 1
            else:
                salidzinama_adrese = 2 * i + 2
        except IndexError:
            i = i - 1
            continue
        if data[salidzinama_adrese] < data[i]:
            data[i], data[salidzinama_adrese] = data[salidzinama_adrese], data[i]
            swaps.append((i, salidzinama_adrese))
            if i > steps:
                steps = i
        if i == 0 and steps != 0:
            i = steps
            steps = 0
            continue
        i = i - 1
    return swaps


def main():
    # TODO : add input and corresponding checks
    # add another input for I or F
    # first two tests are from keyboard, third test is from a file

    # input from keyboard
    text = input()

    if "I" in text[:1]:
        n = int(input())
        data = list(map(int, input().split()))
    else:
        text = input()
        f = open("./tests/" + text, "r")
        n = int(f.readline())
        data = list(map(int, f.readline().split()))
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
