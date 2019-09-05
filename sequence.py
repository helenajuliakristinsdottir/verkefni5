#plúsa saman síðustu 3 tölur
#Generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
n = int(input("Enter the length of the sequence: ")) # Do not change this line
count=3
num1=1
num2=2
num3=3
print(num1)
print(num2)
print(num3)

while count < n:
    summ=num1+num2+num3
    print(summ)
    num1=num2
    num2=num3
    num3=summ

    count += 1
    



    


  