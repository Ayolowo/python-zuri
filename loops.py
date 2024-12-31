#value of num can range from 1 - 12
num = int(input("Enter a number: "))

#using for loop to iterate 12 times
for i in range(1, 13):
    for num in range(1, 13):
        print(num, 'x', i, '=', num*i)
    print('\n')