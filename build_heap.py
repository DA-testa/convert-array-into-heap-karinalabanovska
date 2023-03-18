# python3


def build_heap(data):
    swaps = []
    n = len(data)

    def sift_down(i):
        nonlocal swaps
        min_idx = i
        left = 2*i + 1
        right = 2*i +2

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
    
    mode = input().strip()
    if mode == 'F':
        filename = input().strip()
        with open(filename) as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().strip().split()))
    elif mode == 'I':
        n = int(input().strip())
        data = list(map(int, input().strip().split()))
    else:
        print("Invalid mode")
        return

    assert 1 <= n <= 100000
    assert len(data) == n
    assert all(0 <= ai <= 10**9 for ai in data)
    assert len(set(data)) == n

    swaps = build_heap(data)

    m = len(swaps)
    assert 0 <= m <= 4*n

    print(m)
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
