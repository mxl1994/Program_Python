def sort():
    a = [16,4,6,3,77,22,10,6]
    for i in range(len(a)):
        x = i
        min = a[x]
        for j in range(i,len(a)-1):
            if min > a[j+1]:
                x = j+1
                min = a[x]
            else:
                continue
        if x!=i:
            temp = a[x]
            a[x] = a[i]
            a[i] = temp
        else:
            continue
    return a

if __name__ == "__main__":
    result = sort()
    print result