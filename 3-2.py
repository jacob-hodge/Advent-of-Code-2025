result=0
n = 12
# if value we're checking < the value currently at the end of the stack and we have enough left to go through, drop it. 

with open("3.txt") as f:
    for x in f:
        x = x.strip()
        rowMax = []
        allowedToPop = len(x) - n
        for a in x:
            while rowMax and rowMax[-1] < int(a) and allowedToPop > 0:
                rowMax.pop()
                allowedToPop -= 1
            rowMax.append(int(a))
        valToAdd = ""
        for b in range(12):
            valToAdd += str(rowMax[b])

        result += int(valToAdd)
print(result)