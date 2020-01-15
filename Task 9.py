numbers=[];
count1=0;
count2=0;
count=int(input("How many numbers do you want to enter:\n"));
for i in range(0,count):
    number=int(input("Enter each number one by one:\n"));
    numbers.append(number);
    if(numbers[i]%2==0):
        count1=count1+1;
    else:
        count2=count2+1;
print(numbers);
print("\nNo.of even numbers= ",count1);
print("\nNo. of odd numbers= ",count2);
