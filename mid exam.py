def myRange(start,end,hop=1):
    retVal=start
    while retVal < end:
        yield retVal
        retVal+=hop
hap=1
for i in myRange(1,10,3):
    hap*=i
print(hap)


a_list=[12,34,25,8]
print(a_list[::-1])
print(a_list[-1])
