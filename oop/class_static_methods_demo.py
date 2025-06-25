class Calculator:
    calculation_type = "Arithmetic Operations" 

    @staticmethod
    def add(a, b):
        """return the sum of two numbers."""
        return a + b 

    @classmethod
    def multiply(cls, a,b):
        print(f"Calculation Type: {cls.calculation_type}")

if __name__=="__main__":
    sum_result = Calculator.add(10, 5)
    print(f"Sum: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"Product: {product_result}")