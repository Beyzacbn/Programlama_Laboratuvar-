list = [-4,-3,-2,-1,29,22,-2,-6,-5]

def max_sequential (liste):
    max = liste[0]
    maxSumIndexs = []

    for i in range (len(liste)):
        sum_n=0
        for j in range (i,len(liste)):
            sum_n += liste[j]
            if max < sum_n :
                max = sum_n
                
    return max

print(max_sequential(list))

