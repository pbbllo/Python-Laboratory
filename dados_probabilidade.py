'''
Calculate the probability of 2 dices of the faces number n result number k

'''

def ProbilityCalculate(n,k):

    possibility = 0

    for face in range(1,n+1):
        if (k-face) <= 6:
            possibility += 1

    probability = (possibility) / (n ** 2)

    return probability 

print(ProbilityCalculate(6,10))


