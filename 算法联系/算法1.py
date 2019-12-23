def StringSort(data):
    startIndex=0
    endIndex=0
    count=len(data)
    while startIndex+endIndex<count:
        if data[startIndex]=='-':
            data[startIndex],data[count-endIndex-1] = data[count-endIndex-1],data[startIndex]
            print startIndex,endIndex
            endIndex+=1
        else:
            print startIndex, endIndex
            startIndex+=1
        print data
    return data
data=['-','-','+','-','+','+','-','+','+','-','-','+','-']
print(StringSort(data))