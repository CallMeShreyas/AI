def selection_sort(arr):
    print(arr)

    boundry = 0
    while(boundry != len(arr)-1):
        for i in range(boundry+1, len(arr)):
            if arr[boundry] > arr[i]:
                arr[boundry], arr[i] = arr[i], arr[boundry]
                # print(arr)
                

        boundry = boundry+1
        
    print(arr)


A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
selection_sort(A)
