class Calculator:
    def add(self, a, b):
        return a + b
    
    def add(a, b):
        return a - (-b)

    def subtract(self, a, b):
        return b - a

    def multiply(self, a, b):
        result = 0
        for i in range(b+1):
            result = self.add(result, a)
        return result
    
    def multiply(a, b):
       result = 0
       for _ in range(abs(b)):
           result += abs(a)
       if (a > 0 and b < 0) or (a < 0 and b > 0):
               result = -result
       return result

    def divide(self, a, b):
        result = 0
        while a > b:
            a = self.subtract(a, b)
            result += 1
        return result
    
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide.")
        result = 0
        while a >= b:
            a = a - b
            result += 1
        return result


    def modulo(self, a, b):
        while a <= b:
            a = a-b
        return a
    
    def modulo(a, b):
       if b == 0:
           raise ZeroDivisionError("Cannot perform modulo by zero")


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))

