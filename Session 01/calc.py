#Time (in seconds)
t = 42 * 60 + 42
print("\n\n42 minutes and 42 seconds is equal to " + str(t) + " seconds")

#Distance (in miles)
d = 10 / 1.61
print("10 kilometers is equal to " + str(round(d,1)) + " miles\n")

#Pace (in seconds per mile)
p = t / d

#Speed (in miles per hour)
s = d / (t/3600)

print("Average Computations:")
print("\tPace: " + str(int(p/60)) + " minutes, " + str(int(p % 60)) + " seconds" )
print("\tSpeed: " + str(round(s,1)) + " miles per hour\n")

