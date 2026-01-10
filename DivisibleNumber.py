# Write to check a number is divisible by another number.

print ("Enter a Number (Numerator): ")
num_n = int(input())
print ("Enter a Number (Denominator): ")
num_d = int(input())

if num_n%num_d==0:
    print("/n" +str(num_n)+ "is divisible by" +str(num_d))
else:
    print("/n" +str(num_n)+ "is not divisible by" +str(num_d))