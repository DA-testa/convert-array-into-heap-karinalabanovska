# python3


def build_heap(data):
    swaps = []
    n = len(data)

    def sift_down(i):
        nonlocal swaps
        min_idx = i
        left = 2*i + 1
        right = 2*i + 2

        if left < n and data[left] < data[min_idx]:
            min_idx = left
        if right < n and data[right] < data[min_idx]:
            min_idx = right

        if i != min_idx:
            data[i], data[min_idx] = data[min_idx], data[i]
            swaps.append((i, min_idx))
            sift_down(min_idx)

    last_non_leaf = (n-2)//2

    for i in range(last_non_leaf, -1, -1):
        sift_down(i)

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    
    n = input().strip()
    if n == 'I':
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
            
    elif n == 'F':
        file = input()
        with open("tests/" + file, 'r') as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().split()))
            assert len(data) == n
            swaps = build_heap(data)
            print(len(swaps))
            for i, j in swaps:
                print(i, j)


if __name__ == "__main__":
    main()
