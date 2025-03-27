#WAP TO CHECK IF THE ENTERED NUMBER IS EVEN OR ODD
#WAP TO FIND THE GREATEST OF THE 3 NUMBERS ENTERED BY THE USER
#WAP TO CHECK IF A NUMBER IS A MULTIPLE OF 7 OR NOT

#program 1:
print("Program 1 - checking odd or even number")
num=int(input("enter any number: "))

if(num%2==0):
    print("the number",num,"is even")

else:
      print("the number",num,"is odd")  
      
#Program 2:
print("\nProgram 2 - greatest among three numbers")

num1=float(input("enter first number: "))
num2=float(input("enter second number: "))
num3=float(input("enter third number: "))

if(num1>num2 and num1>num3):
     print(num1,"is greatest among the three numbers")

elif(num2>num1 and num2>num3):
      print(num2,"is greatest among the three numbers")

else:
     print(num3,"is the greatest among the three numbers")     

# Program 3:
print("\nProgram 3 - checking factor of 7")
number=int(input("Enter any number: "))

if(number%7==0):
    print(number,"is a multiple of 7")
    

else:
    print(number,"is not a multiple of 7")
    
        