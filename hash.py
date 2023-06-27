import random
import math
sample = "YhdZsmnaxVlWQrzcPpIbBqXDvJuRStgyfiLeOCNHkFwEMTGjKLUoAZYxvncrI"


def calculateHash(string):
    baseval = ''
    answer = []  # stores all index values

    for ch in string:
        tempval = ord(ch)
        baseval += str(tempval)

    # getting the base number value og the url string
    basenum = int(baseval)
    r1 = random.randint(51, 100)
    #print("Baseval", basenum)
    # calculating base index
    basenum = basenum//r1
    # print("Basenum", basenum)
    # print()
    index0 = basenum % 52
    answer.append(index0)

    # calculating first index
    tempstr1 = str(basenum)
    r2 = random.randint(121, 321)  # second random value
    firstval = ''
    for number in tempstr1:
        tempval = ord(number)
        tempval = tempval ^ r2
        firstval += str(tempval)
    firstintval = int(firstval)
    # print("firstval", firstintval)
    # print()
    index1 = firstintval % 52
    answer.append(index1)

    # calculating second index
    r3 = random.randint(2, 69)
    secondintval = firstintval//r3
    # print("Second", secondintval)
    # print()
    index2 = secondintval % 52
    answer.append(index2)

    # calculating third index
    r4 = random.randint(1, 17)
    secondintval = secondintval*r4
    thirdval = ''
    for ch in str(secondintval):
        temp = ord(ch)
        temp = temp*r4
        thirdval += str(temp)
    thirdintval = int(thirdval)//(9999999999*999999999)
    # print("Third", thirdintval)
    # print()
    index3 = (thirdintval//r4) % 52
    answer.append(index3)

    # calculating fourth index
    r5 = random.randint(43, 890)
    thirdintval = thirdintval % r5
    fourthval = ''
    d = 7
    m = 3
    for ch in str(thirdintval):
        temp = ord(ch)
        temp = temp ^ r5
        temp = (temp*m)//d
        d += 2
        m += 1
        fourthval += str(temp)
    fourthintval = int(fourthval)
    # print("Fourth", fourthintval)
    # print()
    index4 = fourthintval % 52
    answer.append(index4)

    # calculating last index
    r6 = random.randint(69, 199)
    r7 = random.randint(89, 132)
    lastintval = fourthintval*r6*r7
    lastintval = lastintval ^ r7
    lastintval = int(math.sqrt(lastintval))
    # print("Last", lastintval)
    # print()
    indexlast = lastintval % 52
    answer.append(indexlast)

    hashval = ""
    for i in answer:
        hashval += sample[i]
    # print(hashval)

    return(hashval)


