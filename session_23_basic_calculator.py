class Calculator:
    def add(self,a,b):
        return a+b

    def subtract(self,a,b):
         return a-b

    def multiply(self,a,b):
          return a*b

    def divide(self,a,b):
          return a/b

        #object creation
mycalcus = Calculator()
while True:
 print("1.addition")
 print("2.subtraction")
 print("3.division")
 print("4.multiplication")
 print("5.exit")

 choice = int(input("select the operation"))
 if choice in (1,2,3,4,5):
  if (choice == 5):
   break
  a = int(input("Enter the 1st number"))
  b = int(input("Enter the 2nd number"))
  if (choice == 1):
   print("Result is: ",mycalcus.add(a,b))
  elif (choice == 2):
   print("Result is: ",mycalcus.subtract(a,b))
  elif (choice == 3):
   print("Result is: ",mycalcus.divide(a,b))    
  elif (choice == 4):
   print("Result is: ",mycalcus.multiply(a,b))
  else:
   print("Invalid inputs")
                    

                                
                    
                        
                        
                        


                    
            







                  
    
