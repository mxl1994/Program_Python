A = [16,4,6,3,77,22,10,6]
def quick_sort(A):
    # print len(A)//2
    if len(A) < 2:
        return A
    mid = A[len(A)//2]
    left,right = [],[]
    A.remove(mid)
    for item in A:
        if item < mid:
            left.append(item)
        else:
            right.append(item)
    # quick_sort(left)
    # quick_sort(right)
    return quick_sort(left) + [mid] + quick_sort(right)

if __name__ == "__main__":
    result = quick_sort(A)
    print result
