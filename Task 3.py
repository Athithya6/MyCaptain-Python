words_list=[];
length=[];
number=int(input("How many words do you want to enter?:\n"));
i=0;
while(i<number):
    word=input("Enter the words one by one:\n");
    words_list.append(word);
    i=i+1;

print (words_list);

j=0;
while(j<number):
    length.append(len(words_list[j]));
    j=j+1;

maximum=length[0];
for k in range(0,number):
    if(maximum>length[k]):
        maximum=length[k];
    
print("\nThe length of the longest word is: ",length[0]);
print(max(words_list));
