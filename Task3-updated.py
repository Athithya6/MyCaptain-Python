def maxlength(list):
    list=[];
    length=[];
    j=0;
    while(j<number):
        length.append(len(list[j]));
        j=j+1;

print("\nThe length of the longest word is: ",max(length));
print(max(list));


words_list=[];
number=int(input("How many words do you want to enter?:\n"));
i=0;
while(i<number):
    word=input("Enter the words one by one:\n");
    words_list.append(word);
    i=i+1;

print (words_list);
maxlength(words_list);


