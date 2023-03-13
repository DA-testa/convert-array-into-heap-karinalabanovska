# python3


def build_heap(data):
    swaps = []
    n = len(data)
    
    last_non_leaf = (n-2)//2
    
    for i in range(last_non_leaf, -1, -1):
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
            
            child_swaps = build_heap(data[min_idx:])
            swaps += [(i+cs[0], i+cs[1]) for cs in child_swaps]
       


    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

   

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
 mode = input()
    if "F" in mode:
         filename = input()
    
    else:
            print("error")
    elif "I" in mode:
        n = int(input())
        parentOfNode = list(map(int, input().split()))
    else:
        print("invalid mode")
    print(swaps(n, parentOfNode))
    # input from keyboard
    #n = int(input())
    #data = list(map(int, input().split()))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
