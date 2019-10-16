
cents=int(input("Please enter the change in Cents: "))
Quarter= int(cents/25)#25cents=1 Quarter
Dime =int (cents%25/10)# 10 cents=1 Dime
cents =(cents%25)%10
print(Quarter,"quarters",Dime,"dimes and",cents,"cents")

