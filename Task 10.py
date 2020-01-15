class Rectangle:
    l=int(input("Enter the length of the rectangle:\n"));
    b=int(input("Enter the breadth of the rectangle:\n"));
    area=l*b;
    def Area(self):
        print("The area of the rectangle is: ",self.area);
        return;

rectangle1=Rectangle();
rectangle1.Area();
