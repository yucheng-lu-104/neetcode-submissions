import math

class AreaCalc:
    
    @staticmethod
    def calculate(*args):
        if len(args) == 1:
            radius = args[0]
            return round(math.pi * radius ** 2, 2)
        
        elif len(args) == 2:
            length, width = args
            return length * width
        
        else:
            raise TypeError("calculate() expects 1 or 2 arguments")
    

# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
