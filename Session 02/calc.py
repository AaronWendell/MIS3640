import math

print("\nSession 01 Work")

#Time (in seconds)
t = 42 * 60 + 42
print("42 minutes and 42 seconds is equal to " + str(t) + " seconds")

#Distance (in miles)
d = 10 / 1.61
print("10 kilometers is equal to " + str(round(d,1)) + " miles")

#Pace (in seconds per mile)
p = t / d

#Speed (in miles per hour)
s = d / (t/3600)

#Average Print Outs
print("Average Computations:")
print("\tPace: " + str(int(p/60)) + " minutes, " + str(int(p % 60)) + " seconds" )
print("\tSpeed: " + str(round(s,1)) + " miles per hour\n\n")



print("Session 02 Work")

#Sphere Volume with radius of 5
r = 5
v = (4/3) * math.pi * (r ** 3)
print("The volume of a sphere with a radius of 5 is " + str(v))

#Wholesale Cost
#Set b as the number of books (60)
b = 60
#Book Cost
w_b = 24.95 * 0.6 * b
#Shipping Cost
w_s = 3 + (0.75 * (b - 1))
#Total Wholesale Cost
w = w_b + w_s
print("The wholesale cost of 60 books is $" + str(round(w,2)))

#Time Arriving Home
#Convert starting time to seconds since midnight
start = 6 * 60 * 60 + 52 * 60
#Convert durations of run portions to seconds
run_A = 8 * 60 + 15
run_B = 3 * (7 * 60 + 12)
#Add two of run A and one run B to start time
end = start + 2 * run_A + run_B
end_hours = int(end / 3600)
end_minutes = int((end % 3600) / 60)
print("You will get home at " + str(end_hours) + ":" + str(end_minutes))

#Average Grade Change
percent = round((89-82)/82 * 100,1)
print("A grade rising from 82 to 89 is a " + str(percent) + "% increase\n")