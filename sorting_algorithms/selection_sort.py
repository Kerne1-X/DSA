def sel_sort(A):
    n = len(A)
    for i in range(n): # Iterate over the array to get original indexes
        min_idx = i
        for j in range(i+1, n): 
            '''
            search future array A[1:n] for elements greater than smallest value 
            and if condition exists, create new min indices for future swapping 
            '''
            while A[j] < A[min_idx]:
                min_idx = j
                break

        A[i], A[min_idx] = A[min_idx], A[i] # swap original array index for new index given the condition 
    return A


if __name__ == "__main__":
    A = [64, 25, 12, 22, 11]
    print(sel_sort(A))
