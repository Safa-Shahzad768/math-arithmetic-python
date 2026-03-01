class calculator:

    #additionFunction
    def add(self,a,b):
        return a+b
    
    #subtractionFunction
    def sub(self,a,b):
        return a-b
    
    #multiplyFunction
    def mul(self,a,b):
        return a*b
    
    #divisionfunction
    def div(self,a,b):
        if b==0:
            print("Cannot divide by zero")
        return a/b

    #floordivideFunction
    def floordiv(self,a,b):
        if b==0:
            print("Cannot divide by zero")
        return a//b
        
    #modulasfunction
    def modulus(self,a,b):
         if b==0:
            print("Cannot divide by zero")
         return a%b

    #powerFunction
    def power(self,a,b):
        return a*b
    
#objectCreation
cal = calculator()

#callingFunctions
print("Sum:", cal.add(16,2))
print("Subtrat:", cal.sub(16,2))
print("Multily:", cal.mul(16,2))
print("Divide:", cal.div(16,2))
print("Floor Divide:", cal.floordiv(16,2))
print("modulas:", cal.modulus(16,2))
print("Power:", cal.power(16,2))