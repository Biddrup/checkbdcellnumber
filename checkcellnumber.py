#This will check given cell number is for Bangladesh or not

# This function will check
def check(cellnumber):
    for i in range(3, 13):
        if not cellnumber[i].isdecimal():
            return'Please, put only number'
    else:
        return'Yes, this one is perfect'

#Will take a number from user
print('Please, give me a number')
number = input()

if number[0:3] == '880' and len(number) == 13:
    print(check(number))
else:
    print('Cell number should be only 13 digits')
