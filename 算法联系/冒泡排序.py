def sort():
    a = [1,4,6,3,77,22,10]
    for i in range(0,len(a)):
        for j in range(0,len(a)-i-1):
            if a[j] > a[j+1]:
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
    print a

if __name__ == "__main__":
    sort()