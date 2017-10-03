# Odd number from 1 to 1000
for i in range(1,1000,2):
    print i

# Multiples of 5 from 5 to 1,000,000
for i in range (5, 1000000, 5):
    print i

# Sum of all in an array
a = [1, 2, 5, 10, 255, 3]
sum = 0
for data in a:
    sum = sum + data
print "sum:", sum

# Average of array
avg = sum/len(a)
print "Average: ", avg