# Question 1
sum = 0
for i in range (1,101):
    sum += i
print('Numbers 1-100 sum to ' + str(sum))

# Question 2
sum = 0
for i in range (1,1001):
    sum += i
print('Numbers 1-1000 sum to ' + str(sum))

# Question 3A
sum = 0
for i in range (1,1001):
    if i%2 == 1:
        sum += i
print('(Method A) Odd numbers 1-1000 sum to ' + str(sum))

# Question 3B
sum = 0
for i in range (1,1001,2):
    sum += i
print('(Method B) Odd numbers 1-1000 sum to ' + str(sum))



result = 1

for i in range (1,11):
    result *= i

print(result)