number = int(input("Enter a number you want to find the sum of : "))
sum = 0
for i in range (1, number+1):
    sum = sum + i 
    print(i)
print("The sum of your chosen number is ", sum)
