import math

def mysqrt(a, epsilon = 0.001, x = 3):
    while True:
        #print(x)
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return y

print('a\tmysqrt(a)\tmath.sqrt(a)\tdiff')
print('-\t---------\t------------\t----')
for i in range(1,10):
    print(str(format(i,'.1f')) + '\t' + str(format(mysqrt(i),'8f')) + '\t' + str(format(math.sqrt(i),'.8f')) + '\t' + str(format(mysqrt(i) - math.sqrt(i), '.8f')))
