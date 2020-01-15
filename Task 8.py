list=[];
total=int(input("How many numbers do you want to enter:\n"));
k=0;
while(k<total):
    number=int(input("Enter each number one by one:\n"));
    list.append(number);
    k=k+1;

print(list);
prod=1;
m=0;
while(m<total):
    prod=prod*list[m];
    m=m+1;

print("\nThe product of the elements is:",prod);


    
