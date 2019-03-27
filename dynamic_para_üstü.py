# dynamic yöntem ile para üstü verme
# sadece olası durumları kontrol eder, gereksiz kontrol yapmaz

def recMC(coinValueList,change,knownResults):
    minCoins=change
    if (change in coinValueList):
        knownResults[change]=1
        return 1
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recMC(coinValueList,change-i,knownResults)
            if(numCoins<minCoins):
                minCoins=numCoins
                knownResults[change]=minCoins
    return minCoins
for i in range(8,20):
    print(i,"  ",recMC([1,5,10,25,50],i,[0]*(i+1)))
