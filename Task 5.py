month1=["January", "March", "May", "July", "August", "October", "December"];
month2=["April", "June", "September", "November"];

month= input("Enter a month name:\n");
if month == "February":
    print("No.of days=28(non-leap year) and 29(leap year)");
elif month in month1:
    print("No.of days=31");
elif month in month2:
    print("No.of days=30");
else:
    print("Invalid month name");
 

