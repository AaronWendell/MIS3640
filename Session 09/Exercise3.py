file = open("Session 09/words.txt")
contents = file.read().splitlines()


def checkdoubles(word):
    numdoubles = 0
    n = 0
    while n <= len(word) - 2:
        if word[n] == word[n+1]:
            numdoubles += 1
            n +=2
            if numdoubles == 3:
                return True
        else:
            numdoubles = 0
            n += 1
    return False


print("In the input file, the following words have 3 consecutive double letters:")
for i in range(len(contents)):
    if checkdoubles(contents[i]) == True:
        print("\t - " + contents[i])


def twodigit(age):
    if age < 10:
        return str(age).zfill(2)
    else:
        return str(age)

        
def findNumReverse(yearsApart):
    childAge = 0
    parentAge = childAge + yearsApart
    numReverse = 0

    childSwapAges = []

    while parentAge < 100:
        if (twodigit(childAge)[0] == twodigit(parentAge)[1]) and (twodigit(childAge)[1] == twodigit(parentAge)[0]):
            numReverse += 1
            childSwapAges.append(childAge)
        parentAge += 1
        childAge += 1
    
    return childSwapAges

gap = 0

for age_gap in range (90):
    if len(findNumReverse(age_gap)) == 8 :
        gap = age_gap
        break
    #print("  Number of Swaps total " + str(findNumReverse(age_gap)) + '  With '  + str(age_gap) + ' years between parent and child' )

print("If age reverse will happened 8 times, their mom had them at " + str(age_gap))
print("If this has happened 6 times, then the child must be an age between the 6th and 7th occurence; between " + str(findNumReverse(age_gap)[5]) + ' and ' + str(findNumReverse(age_gap)[6] + ' years old'))