# WAP which make a new list contain square of each list's element
def doubling(li):
    newList = []
    for i in range(0,len(li)):
        result = li[i]*li[i]
        newList.append(result)
    return newList

print(doubling([1,2,3,4]))