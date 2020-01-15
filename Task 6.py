a=int(input("Enter the first side of the triangle\n"));
b=int(input("Enter the second side of the triangle\n"));
c=int(input("Enter the third side of the traingle\n"));

if(a==b==c):
    print("\nEquilateral triangle");
elif(a==b or a==c or b==c):
    print("\nIsoscles triangle");
elif(c*c==a*a+b*b):
    print("\nRight triangle");
else:
    print("\nScalene traingle");
