class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b # change from b-a

    def multiply(self, a, b):
        result = 0
        for i in range(b): # change from for i in range(b+1)
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        if a == b: # add if
            return 1
        elif a > b: #add if
            if b == 0: # add case dividied by zero
                return "error"
            else:
                if b > 0:
                    while a >= b:
                        a = self.subtract(a, b)
                        result += 1
                    return result



    
    def modulo(self, a, b):
        while a >= b: # change from a <= b
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))