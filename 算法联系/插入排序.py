A = [16,4,6,3,77,22,10,6]
def insert_sort(A):
    for i in range(1, len(A)):

        key = A[i]

        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A

if __name__ == "__main__":
    result = insert_sort(A)
    print result
