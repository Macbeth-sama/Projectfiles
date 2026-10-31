
print("Hello and welcome to our calculator , here you can add stuff and subtract, future updates will be comming soon !")
running=True
print("enter + if you wish to add some 2 random digits and - if you wish to subtract two random digits , * if you want to multiply,/ if you need to divide and type quit to really quit ") 
while running:
 a=input("Enter command ")
 if (a=="quit"):
    quit=True
    print("Thanks for using our calculator , bye , we hope you come back ")
    break

 elif(a=="+"):
    s=float(input("Enter first number :"))
    d=float(input("Enter second number :"))
    sum=s+d
    print("The sum of your entered digits is = ",sum)
 elif(a=="-"):
    w=float(input("Enter the first number :"))
    e=float(input("Enter the second number :"))
    diff=w-e
    print("The difference of the two entered digits is ",diff)
 elif(a=="*"):
    q=float(input("Enter the first number :"))
    r=float(input("Enter the second number :"))
    product=q*r
    print("The product of the two entered digits is ",product)
 
 elif(a=="/"):
     u=float(input("Enter the first number :"))
     t=float(input("Enter the second number :"))

     if(t==0):
        print("Error, Cannot divide by 0")
     else:
        div=u/t
        print("The division of two numbers is =",div)

 else:
      print("Invalid inputs, try again.")
      